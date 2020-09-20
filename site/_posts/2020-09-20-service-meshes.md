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



A service mesh is a dedicated infrastructure layer for handling
inter-service communication. Although the exact architecture varies,
a typical service mesh looks like this:




## Why they're hard

## Alternatives to service meshes

## The path forward

