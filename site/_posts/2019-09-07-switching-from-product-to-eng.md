---
layout: post
title:  "Switching from product management to engineering"
date:   2019-09-07 16:23:00 -0700
categories: career
excerpt: |
    I began my career as a product manager (PM)
    but then switched tracks and became a software engineer (SWE) three and a half years later.
    In this post, I want to describe how I started as a PM, why I made the decision to switch, and
    how it worked out.
---

I began my career as a
[product manager (PM)](https://en.wikipedia.org/wiki/Product_manager#Product_management_in_software_development),
but then switched tracks and became a
[software engineer (SWE)](https://en.wikipedia.org/wiki/Software_engineer)
three and a half years later. While many people start in engineering and then later go into product
management, the direction that I took is pretty rare and something that people often ask me about
when looking at my background.

In this post, I want to describe how I started as a PM, why I made the decision to switch, and
how it worked out.

## At the start

I come from a fairly non-traditional, academic background- I did Electrical Engineering
(with some CS) in undergrad, and then spent four and a half years getting a PhD in
[Operations Research](https://en.wikipedia.org/wiki/Operations_research). The details of
why I chose to get a PhD and why I chose this field in particular are too long to cover here,
so I'll leave them for a future post.

Towards the end of my PhD program, I got a summer internship at Google through a friend
from school who had graduated and now worked there. Although the internship was technically in
software engineering, the project and day-to-day work were very research oriented- I was trying to
figure out ways to more efficiently allocate compute resources at Google, which was closely related
to my PhD research.

I enjoyed the summer a lot, and towards the end of my internship I had the opportunity to apply for
full-time positions at Google. In addition to going through the SWE conversion process, my mentor
suggested that I also consider product management. The reasoning he gave is that PMs have
higher-level control of projects and also have a lot more flexibility in their day-to-day work.

As an entry-level SWE, I'd be expected to implement small bits of functionality in Google's resource
allocation systems. As a PM, on the other hand, I'd be able to help architect those systems (which
is obviously a much higher-leverage activity), and, moreover, be able to write code, publish papers,
and do other fun activities on the side.

His advice made a lot of sense to me, and, after many rounds of interviews, I got and signed
a full-time PM offer. Six months later, and one week after defending my dissertation, I joined
the product team at Google.

## Being a PM

I started as a PM on the team that I had interned with (Cluster Management), continuing my
summer project on resource allocation and resource efficiency. The summer work had involved
implementing a proof-of-concept and showing that it would have the desired impact from a
theoretical perspective. Now, six months later, the task was to actually implement this
new resource allocation framework and roll it out across the company.

The implementation phase, as it turned out, was really, really hard. Changing how resources were
allocated involved modifying dozens of different systems across the stack and working with
stakeholders who ranged from being skeptical about the project in the best case, to outright hostile
in the worst. After a little over a year, the project team got reorganized, and I decided that
the writing was on the wall and that it was time to move on.

I had been doing some part-time PM work on the
[Google Public Data](https://www.google.com/publicdata/directory) project, and liked the team a
lot, so I managed to transition this into a full-time role.

When I started on the Public Data Team, I focused on typical PM work like writing requirements
docs and talking to customers. The team was pretty small, though, so product specs
could be generated a lot faster than the described product features could be implemented; to fill
up the extra time, I decided to take up small, engineering-related side projects that would be
useful to the team and our customers.

Our data providers, for instance, were having trouble getting their data into the XML-based format
that we required. So, I wrote some command-line tools in Python to help with the conversion process,
got this code reviewed by engineers on the team, and made it available to our users. Other projects
included prototyping a web-based dataset editor and writing Chrome extensions to speed up our
release QA process.

After a while, I realized that I liked working on these kinds of projects a lot more than my
regular product work. Although I was doing an acceptable job as a PM, I started dreading the endless
meetings and the hours spent working on product specs that had little chance of ever being
implemented. The highlight of each day was the hour or so when I could put my headphones in
and write code.

About a year into my stint on the Public Data Team, the project got merged into another,
larger effort, and the pieces that I had worked on were deemphasized. After three years as a PM, I
decided that it wasn't the ideal role for me and that now was the time to switch to engineering.

## Switching

Once I decided to switch, I had two choices- I could either make the transition at Google or
just apply to engineering jobs at other companies. I had been at Google for a while and was
itching to leave and do something new, so I went with the latter.

I was initially worried about getting interviews, but this turned out to not be a problem at all-
despite having no formal engineering experience on my resume, most companies I applied to were willing
to give me a chance because I was coming from a well-known place and had a bachelor's degree in a
relevant field. The interviews were tough, but I managed to get some solid offers and ultimately
decided to sign on as a SWE at [MoPub](https://mopub.com). I left Google, took a two week vacation,
started the new job, and have been an engineer ever since.

## Looking back

Switching to engineering was a great decision for me, and one that I've had zero regrets about.
I'm much, much happier as an engineer, and I think my career has turned out better because
of it. Although I spent a few years in a less-than-ideal role, I learned a lot from that experience,
and I think it's made me a better engineer because I'm able to incorporate product-related
thinking into my day-to-day work.

## How to decide?

Ultimately, which path to take really depends on what makes you happiest. I'm very introverted
and love sitting in front of my computer all day with my headphones in, so SWE is the best fit for
me. If you're more extroverted and would prefer to spend your time in meetings talking about
product features with engineers and other stakeholders, then PM might be a better path.

If you're thinking of switching between product and engineering, the lowest-risk approach is to try
out the other role for a few months at your current company. Large companies like Google
usually have formal rotation programs for doing this; even at companies without these kinds of
programs, it's often possible to negotiate a one-off rotation. If you're not able to do this,
you can at least try out some tasks on your team that are typically done by the "other" side-
as a PM, for instance, spend a few days fixing bugs in your team's code, or, as an engineer, talk to
some of your customers and write a requirements doc for a new product feature.