---
layout: post
title:  "Migrating to Kubernetes, part 2: Why it's hard"
date:   2021-04-18 16:47:00 -0700
categories: general tech
excerpt: |
    Blah blah blah.
---

Over the last few years, I've worked on
[Kubernetes](https://kubernetes.io/) migrations at several companies-
Airbnb, Stripe, and Segment (my current employer). In this post, I want to talk about why
these migrations are done, what they involve, and why they can be hard.

Unlike my previous post on [why service meshes are hard](/blog/service-meshes), my goal
here is not to dissuade you from doing the migration in the first place, but rather to
make it clear that there are a lot of decisions to be made and lots of work to be done.
Migrating to Kubernetes can be very valuable, but you need to be prepared!

## Why it's hard

### You're migrating a platform, not a system

The main reason that migrating to Kubernetes is hard is that you're not just updating a single
component- you're migrating to an entirely new *platform*, the KUSP, that
has its own set of assumptions, requirements, and interfaces.

As described previously, the biggest shift in going from an LESP to a KUSP is in the use of
containers. Containers require images, which means that you need new workflows for defining,
building, testing, and storing these. Containers usually have a different networking setup than
that of "regular" LESP application processes, which means that your networking infrastructure
(how you allocate IPs, how service discovery works, how certs are provisioned, etc.) may have to
change.

Having containers and orchestrating them via Kubernetes will typically also require changes to
whatever frameworks you're using for logging, metrics, secrets, performance monitoring, deploys,
and other app lifecycle tooling. Although it's possible to keep using the LESP
equivalents for these, at a minimum the interfaces will be slightly different; logs, for
instance, will be written into a different place in the file system, and in a different format,
which means that whatever log collector/forwarder you're using will need to be reconfigured.

Many of these updates aren't scary when considered independently. However, there are a lot of
them to do and there are a lot of problems that can be encountered along the way, so the whole
process can take a long time from end-to-end. And, it's hard to any run mission-critical services in
the KUSP in production before you have at least some basic implementations in place for each of the
core platform components.

### Identity is at a different granularity

As mentioned previously, a KUSP typically separates machine identity from application identity.
While this is nice from a security and isolation standpoint, it can be a huge pain, particularly
if legacy systems have ingrained the idea that machines map 1:1 to identities.

In the AWS world, for instance, IAM roles and network interfaces (with their associated IP
addresses and security group designations) are typically tied to EC2 instances. Supporting
container-level roles, externally addressable IPs, security groups, etc. is possible and has been
getting slightly better over time, but is not yet super easy.

If you're running a service mesh, then you'll need to worry about pod-level certificates
and proxies. Third party frameworks like [Istio](https://istio.io/) can help here, but
they're non-trivial to deploy and operate.

### Configuration is complex

The Kubernetes configuration for a simple, single-container application is
[not too terrible](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/#creating-and-exploring-an-nginx-deployment).
However, as you add in init and sidecar containers, shared volumes, scheduling constraints,
health probes, and other features that production systems might need, these configs can get
pretty hairy.

This complexity leads to at least two problems when adopting Kubernetes. First, you need
to figure out how to set all of the knobs that the configs expose, which can require reading a
lot of documentation and going through a lot of trial and error. Second, when multiplied out across
dozens (or hundreds) of apps running across different environments, manually creating and updating
the corpus of Kubernetes configs for an organization can become really tedious- you need some
tooling to help.

Most companies address the second issue with a combination of YAML templating (via systems like
[Helm](https://helm.sh/)) and higher-level, organization-specific config generation tools. These
help, but none of the existing options here is really perfect. See
[this post](https://segment.com/blog/kubernetes-configuration/) that
I wrote for the Segment engineering blog last year for more detail.

As part of the migration process, you need to evaluate the various approaches here and either
adopt a third-party tool or write you own, which can be a non-trivial amount of work.

### Some batteries not included

Kubernetes includes a powerful set of base API primitives and tooling. However, the pieces it
includes don't cover 100% of what you need to run Kubernetes in production. Several big chunks,
most significantly
[service networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/), are
specified in high-level terms but not actually implemented.

Thankfully, there are solid, third-party solutions available for these missing pieces. As with the
identity mapping issues described above, however, there may be a lot of work involved to
evaluate the various options, make a decision about which ones to use, and deploy them in your
clusters.

## Tips for a smooth migration

###

## Conclusion

Migrating to Kubernetes is a big deal because it's a complicated system, and it touches on so many
different aspects of the "platform" that apps run on in an organization. As with
[migrating to a service mesh](http://localhost:4000/blog/service-meshes), my advice here is to
allocate lots of time, plan out the work carefully, and use third-party solutions (e.g., clusters
managed by cloud providers) whenever possible as opposed to building things from scratch.

Even with strong execution, the migration can take years and require contributions from
engineering teams across the company. It's hard work, and there are definitely still some rough
edges in the Kubernetes ecosystem, but I think the end result can really improve developer
happiness and productivity if implemented in a sensible way. Good luck!