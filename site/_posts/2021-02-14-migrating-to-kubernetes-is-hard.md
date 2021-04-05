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

I'll call this pre-Kubernetes "bundle of stuff" a *legacy service platform* or *LSP* for
short. Normally I hate the term "platform" since it's so overused (seems like it's super trendy
at the moment for companies to be building "platforms" instead of "products"), but in this case I
think it's actually appropriate- the LSP literally a base on which applications in an
organization are created and run.

The exact details of the LSP will vary a lot from company to company. Typically, though,
they have some common characteristics.

First, the main unit of compute is a *machine*, either a virtual machine (VM) like
one provided by [AWS EC2](https://aws.amazon.com/ec2) or a physical box sitting in a data
center somewhere.

Machines are provisioned from a *base image* that includes the operating system and other,
low-level software. There is then a *configuration management* process that installs the
higher-level tools and configs needed to run applications on the machine- these might include
language runtimes for things like Python and Ruby, log and metrics collectors, performance
monitoring tools, and company-specific automation scripts, among many other possibilities. The
latter process is typically orchestrated by third-party frameworks like
[Chef](https://www.chef.io) or [Puppet](https://puppet.com/).

Each machine is configured and provisioned for a specific application. So, if we have ten different
services running in production, we'll typically have ten different machine variants, each
running in a separate pool. The "zeebra" service will have "zeebra instances" that contain
the specific things it needs to run (maybe a
[JRE](https://www.infoworld.com/article/3304858/what-is-the-jre-introduction-to-the-java-runtime-environment.html)),
the "cheetah" service will have "cheetah instances" that contain what it needs (maybe a Ruby
interpreter and an Nginx process), and so forth.



## Migrating to Kubernetes

### Building images

Kubernetes workloads run in *containers*, i.e. semi-isolated processes managed by a runtime
like [Docker](https://www.docker.com/products/container-runtime). Each container runs
from an *image* which is an immutable, layered bundle of

Many LSPs don't

### Creating configs

Kubernetes workloads are declared as *resources* that are configured through the Kubernetes
API. There are a variety of formats in use here, but usually the configuration is defined
in YAML which

Simple

### Deploys



### Logging



### Metrics

### Secrets

### Networking and service discovery

### Developer debugging


## Conclusion

