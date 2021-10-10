---
layout: post
title:  "Migrating to Kubernetes, part 2: Why it's hard"
date:   2021-04-18 16:47:00 -0700
tags: kubernetes
excerpt: |
    In my previous post, I described how migrating to Kubernetes involves transitioning an
    organization's infrastructure from a legacy service platform (LeSP) to a Kubernetes service
    platform (KuSP). In this post, I want to go into more details on why this migration is hard and
    what you can do to reduce the pain associated with this transition.
---

In my [previous post](/blog/migrating-to-kubernetes-legacy-service-platforms), I described
how migrating to Kubernetes involves transitioning an organization's infrastructure from a
legacy service platform (LeSP) to a Kubernetes service platform (KuSP). In this post, I want
to go into more details on why this migration is hard and what you can do to reduce the pain.

Unlike my previous post on [why service meshes are hard](/blog/service-meshes), my goal
here is not to dissuade you from doing the migration in the first place, but rather to
make it clear that there are a lot of decisions to be made and lots of work to be done.
Migrating to Kubernetes can be very valuable, but you need to be prepared!

## Why it's hard

### You're migrating a platform, not a system

The main reason that migrating to Kubernetes is hard is that you're not just updating a single
component- you're migrating to an entirely new *platform*, the KuSP, that
has its own set of assumptions, requirements, and interfaces.

As described in [part 1](/blog/migrating-to-kubernetes-legacy-service-platforms), the biggest shift
in going from a LeSP to a KuSP is in the use of containers. Containers require images, which means
that you need new workflows for defining, building, testing, and storing these. Containers usually
have a different networking setup than that of "regular" LeSP application processes, which means
that your networking infrastructure (how you allocate IPs, how service discovery works, how certs
are provisioned, etc.) may have to change.

Having containers and orchestrating them via Kubernetes will typically also require changes to
whatever frameworks you're using for logging, metrics, secrets, performance monitoring, deploys,
and other app lifecycle tooling. Although it's possible to keep using the LeSP
equivalents for these, at a minimum the interfaces will be slightly different; logs, for
instance, will be written into a different place in the file system, and in a different format,
which means that whatever log collector/forwarder you're using will need to be reconfigured.

Many of these updates aren't scary when considered independently. However, there are a lot of
them to do and there are a lot of problems that can be encountered along the way, so the whole
process can take a long time from end-to-end. And, it's hard to run any mission-critical services in
the KuSP in production before you have at least some basic implementations in place for each of the
core platform components.

### Identity is at a different granularity

As mentioned in [part 1](/blog/migrating-to-kubernetes-legacy-service-platforms), a KuSP typically
separates machine identity from application identity.
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

## Tips for a smoother migration

### Pad your estimates

Migrating to Kubernetes in any medium-to-large organization is a really big, multi-year
project. If you estimate that it will only take two quarters of work from two engineers, then
you're probably a bit off the mark unless you're at a small company.

Estimating realistically at the beginning isn't just for the team's sanity- it's also really
important for setting expectations among your (internal) customers, who may be eagerly awaiting
Kubernetes to address the pain points they're facing in the organization's LeSP. If they
believe that the KuSP can be flicked on with a switch and that it will magically wash away
all of their infrastructure management woes, then they're bound to be disappointed when
reality sets in down the line.

### Identify key customers

Rather than make Kubernetes work for everyone from the beginning, it's helpful to initially
focus on a small number of "key customers". Ideally, these are engineering teams that are:

1. Frustrated by one or more limitations in the existing LeSP
2. Technically savvy when it comes to infrastructure
3. Enthusiastic about Kubernetes in general
4. Eager to get their hands dirty and make the project a success!

By working with just these customers, the team running the migration can focus on a limited
subset of use cases and get active help on improving the associated tools and processes.
Once these customers are migrated and happy with the results (hopefully), they can serve as examples
of how to use the KuSP and also help evangelize the migration within the organization.

At Airbnb, we initially worked with the team that was running
[Superset](https://airbnb.io/projects/superset/) internally. At Stripe, we partnered with the teams
that were building the company's
[machine learning training pipelines](https://stripe.com/blog/railyard-training-models) and
using these models to detect fraud in incoming charge requests. At both companies, doing these
initial migrations was critical for proving that Kubernetes could work and provide value.

### Involve the entire organization

Migrating customers in a 1:1, "white glove" manner is fine, but unless you have a 30 person
migration team, this high-touch approach won't efficiently scale. Once you're migrated
the initial "key customers", proved that Kubernetes will work, and worked out the initial bugs, you
need to get help from the larger organization.

Ideally, most teams are responsible for migrating their services themselves. This frees up the
Kubernetes team to answer questions, monitor the shared infrastructure, improve general usability
and reliability, and focus on the hairier migrations that need more hand-holding.

Unfortunately, some teams might prioritize other things above helping out with a messy
infrastructure migration that doesn't directly benefit them. This is where management really needs
to step in, set priorities, and make it clear that product features will be pushed back to
make room for migration work. If management isn't willing to this this, then that's fine, but
they'll need to understand that the project will go on for a very, very long time without this
help.

### Don't just focus on the long tail

It's tempting when doing a Kubernetes migration to start with small, non-critical services and then
gradually work up to the big, "monster" services that lots of people work on and are key for
delivering the company's products.

While it's fine to focus on the long tail at the beginning, I think procrastinating too much on
attacking whatever "the beasts" are at an organization (e.g., that old, crufty service that
handles all the API requests) can really be a detriment and reduce the project's momentum.

First, these larger services are typically where there's the most pain and where a migration
can have the biggest impact on engineer productivity. Second, the only way to really flush out
the bugs and rough edges, both in terms of usability and also in terms of the performance and
reliability of the technology, is to exercise the KuSP in a high-usage, high-traffic environment.

If you're only using Kubernetes for the less critical components of your stack, then it's hard
to claim that Kubernetes (and, by extension, your team's work) is critical to the success of your
company.

### Avoid scope creep

Handling just the "must haves" in a Kubernetes migration is hard enough. Resist the temptation
to treat this as an opportunity to fix every other legacy platform component that's in a
non-optimal state, particularly if the migration makes these things no worse than before.

While it would be great to get Kubernetes bundled with a new networking stack, a new secrets system,
a new logging system, etc. each of these extra dimensions adds more things that will be
unfamiliar to users, and more things that can break in production. Focus on what is needed to
migrate successfully, then handle the "nice to haves" in later phases of the project.

## Conclusion

Migrating to Kubernetes is a big deal because it's a complicated system, and it touches on so many
different aspects of the "platform" that apps run on in an organization.

Even with strong execution, the migration can take years and require contributions from
engineering teams across the company. It's hard work, and there are definitely still some rough
edges in the Kubernetes ecosystem, but I think the end result can really improve developer
happiness and productivity if implemented in a sensible way. Good luck!