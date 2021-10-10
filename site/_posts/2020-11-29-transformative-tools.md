---
layout: post
title:  "Transformative tools"
date:   2020-11-29 13:06:00 -0700
tags: tooling
related_posts:
    - slug: "jira-makes-me-want-to-cry"
excerpt: |
    Since I switched into engineering 8 years ago, I've witnessed a few productivity and
    organization tools that have really been "transformative" in terms of how I do my day-to-day
    work. In this post, I want to share my personal, before-and-after experiences with these.
---

One of the cool things about software engineering is that the associated technologies
are constantly changing. This applies not just to the technical things we build with (i.e., the
programming languages, frameworks, hardware, etc.), but also the tools that we use to
make ourselves better organized and more productive.

Since I switched into engineering 8 years ago, I've witnessed a few tools in the latter
category that have really been "transformative" in terms of how I do my day-to-day work. In this
post, I want to share my personal, before-and-after experiences with these.

#### Ground rules

For the basis of this post, I'm only considering things that are related to process or
productivity, i.e. not specific languages, frameworks, technical systems, etc. Also,
I'm skipping tools that came to prominence more than 8 years ago, which includes Github, GMail,
Google Docs, and many other things that are still very popular and useful today.

## Transformative tools

### Slack

<img src="/assets/slack_logo.png" alt="Slack logo" height="50"/>

When I started my career, email was everything. I spent hours each day reading through reams
of messages and crafting well-written, doubly-proofread replies in long, back-and-forth threads
with colleagues and executives.

Now, I write maybe one email a month at work. The vast majority of the back-and-forth conversation
that used to happen in email is now in [Slack](https://www.slack.com), a cloud-based communication
system that provides instant group and 1:1 chat. These technologies have been around for a while
(I remember them from my dial-up AOL account in the 1990's), but Slack packages them in a pretty,
feature-rich way and has been very successful at getting adoption inside tech companies over the
last few years.

Having a conversation in Slack is obviously faster than having one over email. However, the key
benefit for me with Slack is that I can edit or delete messages after I've posted them. Now,
I can just say what's on my mind and if I'm wrong about something (as I often am), I can go
back and correct myself. Gone is the fear around referring to the wrong system when debugging
a problem, making a spelling mistake, expressing an opinion too forcefully, or other things
that obsessive people like me used to worry about and get slowed down by when drafting emails.

These features, combined with all the other bells and whistles that Slack offers, have really
transformed how I communicate at work. Of course, there are some downsides, particularly in that it
enables more frequent, lower-quality interruptions. On the whole, though, I think Slack and its
competitors (e.g.,
[Microsoft Teams](https://www.microsoft.com/en-us/microsoft-365/microsoft-teams/group-chat-software))
have been a net positive and can really transform communication in other industries as well.

### VSCode

<img src="/assets/vscode_logo.png" alt="VSCode logo" height="50"/>

Software engineers spend a lot of time writing and editing text files. These include not just
code but also the configuration files and documentation that live alongside the former.

When I started my career, the choices here were either to use a very lightweight, bare-bones
text editor on the one hand, or a heavyweight, bloated
[integrated developer environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)
on the other. Many of these tools were not free software
(I remember [Sublime text](https://www.sublimetext.com/) in particular), required hours
to set up correctly, and would often have performance issues when working in large projects.

Now, I use [VSCode](https://code.visualstudio.com/) for nearly all text editing. VSCode is developed
by Microsoft, but unlike most of their historical products, it's
free and open-source. I was a little skeptical when it first came out- I haven't enjoyed any
Microsoft products since [Flight Simulator 2004](https://en.wikipedia.org/wiki/Microsoft_Flight_Simulator_2004:_A_Century_of_Flight)- but since then I've been won over.

The transformational thing about VSCode for me is that it strikes the right balance between
a lightweight text editor and an IDE. I can use it for the plain Markdown of this blog
but then switch into a golang or Python project and get code completion, error checking,
and other, IDE-ish features without the associated bloat.

VSCode is far from perfect, and there are some situations in which I still wouldn't use it;
in large Java or Scala projects, I would probably stick with
[IntelliJ](https://www.jetbrains.com/idea/), for instance. But, it's continually improving,
super extensible, and has a robust and growing third-party developer community. It's significantly
improved my productivity and happiness, and I imagine that it will only get more adoption over time.

### Docker Compose

<img src="/assets/docker_logo.png" alt="Docker logo" height="50"/>

Containerization, i.e. the ability to easily run processes in semi-isolated environments, has
had a big impact on how software is deployed in production. [Docker](https://www.docker.com/)
popularized the technology, and since then it's played a key role in
[Kubernetes](https://kubernetes.io/) and other large-scale, orchestration frameworks.

Personally, though, I think the biggest benefit to containerization has been in how I run
software on my local machine. Here's why.

Many software projects that engineers work on depend on other, third-party systems to run locally-
the most common examples here are relational databases like MySQL or Postgres; others that I often
see are caches (Redis, Memcached), message brokers (NSQ, Kafka, etc.), and non-relational storage
backends (S3, DynamoDB, etc.).

Prior to Docker, the choices for running these things locally weren't great. You could install
and run them as standard applications, but the directions for doing this would vary based on your
OS, OS version, and other tools running on your system. After installing, your drive would be
forever corrupted with whatever junk these tools needed (shared libraries, etc.), and the
tools themselves would be silently running in the background, consuming resources and doing
who knows what else with your network and file system.

Alternatively, you could run all these things in a virtual machine (VM),
e.g. with [Virtualbox](https://www.virtualbox.org/). VMs are better at providing isolation, but
they're pretty heavyweight. They required monolithic, multi-hundred megabyte image files
(which were often created by someone else by hand), took minutes to boot up, and were a pain to
share files and network access with.

Now, with Docker, and in particular the [Docker Compose](https://docs.docker.com/compose/)
utility, all of this setup is a breeze. With a single YAML file, I can configure
a relational database, a multi-node Kafka cluster, a fake S3 backend, or nearly anything else
for local development and testing. Whether you're running Mac, Linux, Windows, or whatever else,
this same bundle of services can be started by typing `docker-compose up` into the terminal.

In addition to making running apps locally easier, which, depending on the project, may not really
be attainable, Docker Compose allows one to write more realistic tests. Instead of mocking out
access to S3, Kafka, or other complex dependencies, I can just let my tests hit these things using
their "real" APIs (but pointed at compose-hosted instances). This makes me more confident that the
software works and reduces the amount of manual testing I have to do in a remote, pre-production
environment.

### Lucidchart

<img src="/assets/lucidchart_logo.png" alt="Lucidchart logo" height="50"/>

Software systems can be complicated. Beyond text descriptions, it's very common to create
stylized diagrams to show what the main components are and how they interact. These can be
created before the system is built, i.e., as part of design document, or afterwards, as part of
the documentation for the people who have to maintain the system.

Up until a year ago, my go-to tool for making these diagrams was
[Omnigraffle](https://www.omnigroup.com/omnigraffle). Omnigraffle creates pretty diagrams, but
it's a desktop-based application that isn't collaborative. Sharing the outputs is like
sharing Excel spreadsheets in 2003- you have to email the files around and have
[token-ring-like](https://en.wikipedia.org/wiki/Token_ring) rules for deciding who is allowed
to make edits at any given time.

When I started at my current job, I made the usual request for an Omnigraffle license. Instead
of providing one, however, the IT team told me to just use [Lucidchart](https://www.lucidchart.com),
a cloud-based, collaborative alternative. As with the other examples in this blog post, I was
initially resistant to change but then warmed up after getting more familiar with the tool.

Lucidchart is not the first cloud-based diagramming tool. However, it's the first one
I've used that actually creates Omnigraffle-quality (i.e., beautiful, professional) outputs.
Moreover, the interface is super intuitive and the collaboration features are actually a pleasure to
use- one feature that's particularly nice for remote meetings is that if I'm in a diagram with one
of my colleagues, they can see where my mouse is hovering and I can see theirs.

At my current employer ([Segment](https:/segment.com/)), we've used Lucidchart for creating very
large system diagrams, with hundreds of components and dozens of collaborators, without running into
any problems. Lucidchart has enabled these types of collaborations, which previously would have been
much harder, and also made it much less of a hassle for me to create non-collaborative diagrams
for my work-related design docs and documentation pages.

If and when I switch employers, I'm going to strongly request that they adopt Lucidchart for their
internal diagramming.

## Conclusion

Over the last few years, I've incorporated several tools into my day-to-day work that have
really transformed how I get things done. That being said, these tools aren't perfect and,
moreover, there are several other areas of software engineering work that have yet to be
transformed for the better. I'll address the latter in a future post!