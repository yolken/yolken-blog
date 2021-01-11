---
layout: post
title:  "How I made this blog"
date:   2021-01-10 14:10:00 -0700
categories: general tech
excerpt: |
    Every now and then, I get asked how I made this blog from a technical standpoint. In this
    post, I want to share the various options for hosting a blog online and describe
    why I made the particular technical choices I did.
---

Every now and then, I get asked how I made this blog from a technical standpoint. In this
post, I want to share the various options for hosting a blog online and describe
why I made the particular technical choices I did.

## Short answer

I use [Jekyll](https://jekyllrb.com/) to generate the content and
[Github Pages](https://pages.github.com/) for the hosting. The configs are all
[here](https://github.com/yolken/yolken-blog).

## Blogging approaches

When I decided to create a blog two years ago, I did a little digging into the various
options. There were three main approaches I explored, each discussed in more detail below.

### 1: Use a hosted blogging service

The first choice I considered was to use a third-party, hosted blogging service. I had never
used any of these as an author before, but have read tons of content posted by others on these
sites over the years. Back in the day, [Blogger](https://www.blogger.com/) was all the rage.
Recently, it seems like lots of people have been posting articles on [Medium](https://medium.com).
I've also seen some blog-like content hosted on social networks like LinkedIn.

The main advantage of these services is that they're super easy to use. You just type up your
content in a nice, [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) editor and click a button
to publish. They also give you things like comments, search, and subscriptions on top of your
content without much effort.

The downside of these services is that you're handing over your content to a third-party,
who's packaging it up with other people's content, applying their own look-and-feel, and, in many
cases, trying to monetize it. Even though you're the author, and even though you maintain
legal rights to your content in most cases, there's a tendency for your work to become associated
more with the hosting service than with you.

I'm not bothered by this for short, low-value content (e.g., random pictures of my vacation), but
given that I was creating a blog to build my personal brand (among other reasons), I wanted to be in
full control and didn't want to share ownership with anyone else.

Thus, hosted blogging services were out and I moved on to the self-hosted options.

### 2: Run a content management system (CMS) myself

Being a software engineer, the natural approach to hosting your own blog is to write a service
that stores content (i.e., postings) in some sort of database and then dynamically generates
your site's pages in response to user requests. As it turns out, these things are called
content management systems (CMSes), and there are a whole bunch that have already been written.

Wordpress is the most popular; there are also things like


### 3: Generate a static site

An alterative self-hosting option is to