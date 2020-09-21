---
layout: post
title:  "Service meshes are hard"
date:   2020-09-20 13:44:00 -0700
categories: networking
excerpt: |
    Blah blah blah.
---

I've worked on deploying "service meshes" at multiple companies. Although
they look great on paper, deploying them is a huge pain, with very high
risk of serious outages. In this post, I want to share some of my war stories
and caution against diving into the "service mesh" hype too quickly.

## Aside: What's a service mesh?

A common pattern in software engineering is to provide a product or feature
via multiple, semi-independent components. This blog, for instance, is hosted
in Github Pages. When your browser requests the HTML for this page, your
request most likely hits some sort of frontend proxy (e.g.,
[Nginx](https://www.nginx.com/)), which then sends the request to a backend
server (e.g., in Ruby), which then might send out requests to even more
services, e.g. to record stats or fetch user
information.

Without a service mesh, these various component services communicate directly;
here's a simple picture:

<div style="text-align:center"><img src="/assets/service_meshes1.png" alt="service mesh simple" width="400"/></div>

The communication over the arrows is typically HTTP, but might be a more
specialized, binary protocol instead, e.g. when using something like
[Apache Thrift](http://thrift.apache.org/). The communication can be encrypted
but it's often not since this would require the clients and servers to
handle protocols like TLS, which adds complexity and reduces performance.

The picture above doesn't show how service A "discovers" the addresses of B and C.
These might be hard-coded, looked up in [DNS](https://en.wikipedia.org/wiki/Domain_Name_System),
or fetched from a centralized service registry like [Consul](https://www.consul.io/).The important thing to note, though, is that the details of doing this are
handled by A itself.

A service mesh is a dedicated infrastructure layer for handling the details
of this inter-service communication. Although the exact architecture varies,
with a mesh the picture above might become:

<div style="text-align:center"><img src="/assets/service_meshes2.png" alt="service mesh simple" width="500"/></div>

Now, service A doesn't communicate directly with B and C. Instead, it sends requests
to a local (outbound) proxy that then sends the requests to the (inbound) proxies
for B and C. The latter then forward to the requests to the service instances on
their respective hosts. The links between proxies can be, and often are, encrypted
via [mTLS](https://developers.cloudflare.com/access/service-auth/mtls/).

The control plane is needed so that the proxy configurations can stay up-to-date.
If host 2 disappears, for instance, and is replaced with host 2a, then all
of the proxies on the hosts talking to B need to be updated with the new
address.

### Benefits

The nice thing about the mesh architecture is that your services no longer need to
handle the low-level details of communicating with others. This makes a lot of things
substantially easier, at least in theory:

1. **Service discovery:** Service A doesn't need to discover the addresses of B and C,
it can just let the proxy do that.
2. **Encryption:** Encryption is now easier because all hosts are running proxies
that are set up to do this, and we don't need to mess with the details of TLS in various app
HTTP libraries.
3. **Complex routing:** If we want to test a new variation of service B, for instance, we can
configure the mesh to send 1% of traffic to the new instance and the rest to the older ones.
4. **Cross-fleet networking observability:** Since all communication goes through the same
layer, the mesh can expose a uniform set of metrics and logs for all inter-service links.

These benefits are particularly big when you're in an environment with a diverse set
of client and server implementations. Service A might be Ruby, B golang, and C Java. Sure,
you could add mTLS, uniform observability, etc. directly into each service, but you're going
to have to re-implement the same logic multiple times in multiple languages. Even if the
services are written in the same language, they are probably not going to be using the
same client and server implementations uniformly.

## Why they're hard

From the discussion above, it seems like service meshes are great. They make your
infrastructure more secure, uniform, controllable, and observable. Everyone should be
using them!!

Unfortunately, however, service meshes make life harder in a number of different ways.

#### It's an N^2 system

Let's say you have N services and you want to update all of them in some way, for
instance to replace a library with a newer version. Typically, this will involve
O(N) updates and O(N) things that can go wrong. When rolling out a service mesh,
however, you're making O(N^2) updates because you're changing (and potentially breaking)
how each pair of services communicates.

This means that, even with a small number of services, there are a lot of things
that can go wrong (and will). Service A might be fine talking to B, and B might be fine
talking to C, but the A to C link might occasionally timeout for some weird reason
that takes days to debug. If you're in a company with dozens of services, the N^2 effects
can be huge- be prepared for a lot of work rolling things out and debugging.

#### More hops, more problems

In the non-service-mesh world, communication issues are typically the fault of either
the client or server. If service A is getting HTTP 5XX responses from service B, you can
look at the code and logs for B to understand why that might be happening.

In the service mesh world, on the other hand, these responses might be coming from B, the
proxy on B's host, or the proxy on A's host. Now, instead of looking in one place,
you have to look in three places. This means that the debugging process is slower and
more tedious.

#### Encryption makes debugging harder

There are lots of great tools for inspecting unencrypted traffic. Personally,
I like running `tcpdump -i any -A port [my service port]` and watching requests
go back and forth when I'm trying to understand the traffic hitting a service. If
this traffic is encrypted, you can still do this but all you'll see is binary junk:

{% highlight bash %}
16:51:07.773675 IP lga15s43-in-f36.1e100.net.https > 192.168.0.10.56081: Flags [P.], seq 2713:3385, ack 537, win 261, options [nop,nop,TS val 2846442026 ecr 1037268748], length 672
..J..C..k.H...E....$..y..O...$...
......F...$o...........
..B*=.w.......7V.o.$(...wc.qk....2.ePyi\uXsTP..R..z.;S..
"iT....S...Ju.%..........%.....kZV0...EA9.W.NB.^.....f`
hV...i=8?...>8.".-..m.H.........y...	.......?.G.$U<j...s.\>....;.....a......6@
[w.>SHQ.%...F....S..e	..f,..T(CA..U....x...../...8..(.j.....k..h.{.^...5n.4f.[....].x.....}
2.....Q..*.^..?.l...e$.~.]...j......P.....]....R..ZB....7..B9}e".....f.\..
AAV$m....z..m..........x..B.P.`0....k..E..S........$.......{.W..
{% endhighlight %}

Most service meshes only use encryption on the proxy to proxy links and not
on the proxy to service ones. But, these proxy to proxy links are often where a lot of
problems happen, and not being able to easily inspect the details of each request on the
wire makes debugging harder.

#### Certificate management is hard

In order to implement mTLS rigorously, you need to generate fine-grained certificates for
all of the nodes in your mesh. Certificate management for individual hosts is hard enough,
but it gets even messier when hosts are shared by multiple services and each one needs
a distinct identity.

I spent many, many months at Stripe working on a "Service CA" to address this problem. We got
things working in the end, but it required a lot of very careful design


#### Control plane is a single point of failure

The control plane is a critical component of a service mesh. It keeps all of the proxies updated
with the latest service endpoints, routing rules, listener configs, etc. These updates
may be happening frequently due to instances coming up and down, new services being added, and
other changes in the environment. Depending on the sources of this information and the protocol
used between the control plane and proxies, keeping all of the data fresh and accurate can
be challenging.

In addition, the control plane can wreak havoc on your infrastructure if it's misconfigured
or gets confused about the state of the world.

A really scary type of incident, which I've seen a few times across multiple companies, is when
the control plane thinks that all of the service instances have disappeared (maybe because
the source that it pulls these from is broken). It blissfully pushes out empty configs to all
of the proxies,

#### Proxies are complex

Many service meshes use [Envoy](https://www.envoyproxy.io/) as the underlying proxy.
While powerful, Envoy is a beast; it has
[hundreds of knobs](https://www.envoyproxy.io/docs/envoy/latest/configuration/configuration) that
can be tuned to affect its behavior.

The code is written in C++, which is not the easiest language to make changes in, and is
prone to segfaults, leaks, and other types of memory issues if you're not super careful. At
Stripe, we occasionally got crashes and other, hard-to-debug errors that required a lot of work
to understand and fix.

These issues aren't unique to Envoy. Proxies in general are just prone to being complex,
particularly when you're trying to optimize performance and satisfy the many different use cases
that people have for them.

## Alternatives to service meshes

#### For security



#### For load balancing / routing



## The path forward

#### Don't roll your own

####