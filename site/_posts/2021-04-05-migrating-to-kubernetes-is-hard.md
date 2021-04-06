---
layout: post
title:  "Migrating to Kubernetes is hard"
date:   2021-04-05 13:06:00 -0700
categories: general tech
excerpt: |
    Over the last few years, I've worked on
    migrations at several companies- Airbnb, Stripe, and Segment (my current employer). In this
    post, I want to talk about why these migrations are done, what they involve, and why they can
    be hard.
---

Over the last few years, I've worked on
[Kubernetes](https://kubernetes.io/) migrations at several companies-
Airbnb, Stripe, and Segment (my current employer). In this post, I want to talk about why
these migrations are done, what they involve, and why they can be hard.

Unlike my previous post on [why service meshes are hard](/posts/service-meshes), my goal
here is not to dissuade you from doing the migration in the first place, but rather to
make it clear that there are a lot of decisions to be made and lots of work to be done.
Migrating to Kubernetes can be very valuable, but you need to be prepared!

## Why migrate?

Kubernetes is an open-source, compute orchestration framework that was originally developed
by Google but has recently gotten lots of contributions from and adoption by other
organizations.

There are tons of materials available online about what Kubernetes is and how it works (e.g.,
[this one](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)), so
I won't cover those here. It is worth noting, however, the primary reasons that many companies
decide to migrate to Kubernetes from their legacy platforms (discussed more in the next section):

1. *The ecosystem:* A vast ecosystem of tools and apps has developed around
  Kubernetes over the last few years. By using Kubernetes internally, it's easier to take
  advantage of the work that others have done, both in the infrastructure layer (e.g.,
  in terms of networking, service discovery, etc.) and in the applications that are
  being run on top.
2. *Vendor agnosticism:* Kubernetes provides a layer of abstraction on top of whatever
  you're using to provision individual machines and the associated infrastructure (networking,
  persistent disks, etc.). In theory, switching to Kubernetes makes it easier to do things
  like switch between cloud providers, although in practice this is still hard because
  of all the non-Kubernetes-related infrastructure you need to migrate as well.
3. *Easier, more self-service workload management:* Kubernetes exposes a rich set of APIs
  and controllers for deploying applications, ensuring that they run reliably, and enabling
  developers to debug them when things go wrong. In theory, developers can take advantage
  of these features "out of the box", without worrying about low-level machine details,
  writing lots of custom tooling, or depending on a separate "infra" team in the organization
  to set things things up.

## Legacy service platforms

The process for migrating to Kubernetes depends a lot on what you're migrating from.
This includes not just whatever is being used to build and deploy applications, but
also the associated infrastructure and tooling used for running and managing these
applications in production.

I call this pre-Kubernetes "bundle of stuff" a *legacy service platform* or *LSP* for
short. Normally I hate the term "platform" since it's so overused (seems like it's super trendy
at the moment for companies to be building "platforms" instead of "products"), but in this case I
think it's actually appropriate- the LSP literally a base on which applications in an
organization are created and run.

The exact details of the LSP will vary a lot from company to company. Typically, though,
they have some common characteristics.

#### It's all about machines

In an LSP, the main unit of compute is a *machine*, either a virtual machine (VM) like
one provided by [AWS EC2](https://aws.amazon.com/ec2) or a physical box sitting in a data
center somewhere.

Machines are provisioned from a *base image* that includes the operating system and other,
low-level software. There is then a *configuration management* process that installs the
higher-level tools and configs needed to run applications on the machine- these might include
language runtimes for things like Python and Ruby, log and metrics collectors, performance
monitoring tools, and company-specific automation scripts, among other possibilities. The
latter process is typically orchestrated by third-party frameworks like
[Chef](https://www.chef.io) or [Puppet](https://puppet.com/).

#### Applications and identities

Each machine is configured and provisioned for a specific application. So, if you have ten different
services running in production, you'll typically have ten different machine variants, each
running in a separate pool. The "zeebra" service will have "zeebra machines" that contain
the specific things it needs to run (maybe a
[JRE](https://www.infoworld.com/article/3304858/what-is-the-jre-introduction-to-the-java-runtime-environment.html)),
the "cheetah" service will have "cheetah machines" that contain what it needs (maybe a Ruby
interpreter and an Nginx process), and so forth.

Identity, as it pertains to networking and authentication, is at the granularity of a
machine. All processes running on the same host use the same IP address(es), the same cloud role,
the same x509 certificates, etc. So, the "zeebra machines" will run with the "zeebra" role,
use a "zeebra" certificate, live in a "zeebra" network security group, etc.

#### Deploys

The primary application processes on each instance are typically managed and updated by a
higher-level, centralized *deploy system*. So, for instance, if a developer wants to update the
"zeebra" service in production from version 1234 to version 1235, they would give the deploy system
the new version (or this would be automatically detected), and then the latter system would then
handle getting onto each of the "zeebra machines", pulling down an updated artifact, extracting out
whatever binaries, scripts, and/or configs the application needs to run the new version, and then
restarting the app process.

These deploy systems are typically pretty complicated because they need to support all of the
various rules, workflows, and infrastructure quirks specific to each organization. A few have been
open-sourced, like Netflix's [Spinnaker](https://spinnaker.io/), but many companies still end
up building their own because of the amount of customization required.

## Kubernetes service platforms

When you migrate to Kubernetes, you're replacing the LSP with a new, Kubernetes-based service
platform. Following the same naming style, let's call this thing a *Kubernetes service platform*
or *KSP* for short.

KSPs have a few big differences from LSPs, which are described in the sections below.

#### It's all about containers

In the KSP, as opposed to the LSP, the main unit of compute is a *container*, not a machine.
At a high level, a container is just a semi-isolated process. Each container runs from an *image*,
which is effectively a layered, read-only bundle that contains the binaries, tools, configs, etc.
needed create the environment in which the container runs.

Containers run in machines, so you still need to provision them, but configuration for these
machines can be simpler and more generic. The main requirement is to install
a container runtime such as [Docker](https://www.docker.com/). Once you have this runtime, you can
then use it to run containers for your applications and helper services (logs, metrics, networking,
etc.). You can still use Chef or Puppet if you want to, but these are less important because
much of the heavy lifting is now done in the higher-level container and orchestration layers.

#### Applications and identities

In a container-based service platform, applications are less coupled to specific
machine variants. The "zeebra" service can still have its own, "zeebra machine" pool, but this
is less necessary than before because many of the service-specific components can be baked into the
service image as opposed to being installed on the instances on which the container runs.

Identity also moves from the machine to the container layer. Each container can now have its own
IP address, x509 certificate, cloud service role, etc. independent of the identity of the host
that it's running on. This isn't a drop-dead requirement (containers can use the host network,
for instance), but it's considered best practice from a security and isolation standpoint to
enforce this separation.

#### Orchestration via Kubernetes

Containers by themselves are fairly low-level and specific to individual machines. Kubernetes
adds yet another level of abstraction on top of containers that *orchestrates* changes across
containers in a *cluster* of machines. With Kubernetes, applications are updated by changing
the associated resources in the Kubernetes API. The Kubernetes control plane then figures
out which containers on which instances need to be changed, and a special agent on each machine,
the *kubelet*, actually carries out the updates.

Although it's still possible to have a custom deploy system for managing workflows and such,
this system ends up delegating most of the low-level details of the update to the Kubernetes API.

Kubernetes doesn't just handle image updates for individual containers. It does a ton of other
things including bundling containers together as a shared unit (i.e. a *pod*), configuring container
networking, configuring container disk, storing and exposing application secrets (e.g., DB
passwords), monitoring container health and responding to failures, exposing APIs for viewing logs,
allowing developers to "exec" into containers for debugging purposes, etc.

Not all of these things are required. You may, for instance, be able to keep using your LSP
secrets system instead of migrating to Kubernetes secrets. But, there are a lot of choices to
be made here, and using non-standard or non-Kubernetes-aware solutions here might require some
extra work.

## Why migrating is hard

### You're migrating a platform, not a system

The main reason that migrating to Kubernetes is hard is that you're not just updating a single
component- you're migrating to an entirely new *platform*, the KSP, that
has its own set of assumptions, requirements, and interfaces.

As described previously, the biggest shift in going from an LSP to a KSP is in the use of
containers. Containers require images, which means that you need new processes for defining,
building, testing, and storing these. Containers usually have a different networking setup than
that of "regular" LSP application processes, which means that your networking infrastructure
(how you allocate IPs, how service discovery works, how certs are provisioned etc.) may have to
change.

Having containers and orchestrating them via Kubernetes will typically also require changes to the
frameworks you use for logging, metrics, secrets, performance monitoring, and deploys. Although it's
possible to keep using the LSP equivalents for these, the interfaces will be slightly different;
logs, for instance, will be written into a different place in the file system, and in a different
format, which means that whatever log collector/forwarder you're using will need to be reconfigured.

Many of these updates aren't difficult when considered independently. However, there are a lot of
them to do and there are a lot of problems that can be encountered along the way, so the whole
process can take a long time from end-to-end. And, it's hard to any run mission-critical services in
the KSP in production before you have some basic implementations in place for each of the
core platform components.

### Identity at a different granularity

As mentioned previously, a KSP typically separates machine identity from application identity.
While this is nice from a security and isolation standpoint, it can be a huge pain, particularly
if legacy systems have ingrained the idea that machines map 1:1 to identities.

In the AWS world, for instance, IAM roles and network interfaces (with their associated IP
addresses and security group designations) are typically tied to EC2 instances. Supporting
container-level roles, externally addressable IPs, security groups, etc. is possible and has been
getting slightly better over time, but is still not completely trivial. Many companies
depend on third-party tools like [kube2iam](https://github.com/jtblin/kube2iam), which work but
aren't perfect and are often a hassle to set up.

### Configuration is complex

The Kubernetes configuration for a simple, single-container application is not too terrible.
However, as you add in init and sidecar containers, shared volumes, scheduling constraints,
health probes, and other features that production systems might need, these configs can become
fairly complex.

This complexity leads to at least two problems when adopting Kubernetes. First, you need
to figure out how to set all of the knobs that the configs expose, which can require a lot
of trial-and-error. Second, when multiplied out across dozens (or hundreds) of apps running
in different environments, manually creating and updating the corpus of Kubernetes configs
for an organization can become really tedious- you need some tooling to help.

Most companies address the second issue with a combination of YAML templating (via systems like
[Helm](https://helm.sh/)) and higher-level, company-specific config generation tools. These help,
but there really aren't any perfect solutions here. See
[this post](https://segment.com/blog/kubernetes-configuration/) that
I wrote for the Segment engineering blog last year for more detail.

As part of the migration process, you need to evaluate the various approaches here and either
adopt a third-party tool or write you own, which can be a non-trivial amount of work.

### Some batteries not included

Kubernetes includes a powerful set of base API primitives and tooling. However, the pieces it
includes don't cover 100% of what you need to run Kubernetes in production. Several big chunks, in
particular
[service networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/), are
specified in high-level terms but not actually implemented.

Thankfully, there are solid third-party solutions available for these missing pieces. As with the
identity mapping issues described above, however, there may be a lot of work involved to
evaluate the various options, make a decision about which ones to use, and deploy them in your
clusters.

## Conclusion

