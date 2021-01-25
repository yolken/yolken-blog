---
layout: post
title:  "Starting a job"
date:   2021-01-24 15:20:00 -0700
categories: general tech
excerpt: |
    In my last post, I discussed how companies can make their onboarding processes
    better for employees. In this post, I want to turn the tables and talk about the
    strategies I use personally to get up-to-speed when I'm starting at a new job.
---

In my [last post](/blog/great-engineer-onboarding), I discussed how companies can
make their onboarding processes better for employees. In this post, I want to turn
the tables and talk about the strategies I use personally to get up-to-speed when
I'm starting at a new job.

## Starting is hard

First, it's important to state at the outset that I find starting a new job as a
software engineer really, really hard. Even after many years of experience and even
if the new company is using a tech stack that I'm already familiar with, there is
just so much to learn about before one can become productive, including:

1. Where the code lives and how it's organized
2. The key software systems, their interfaces, and how they all fit together
3. Standards and tools for testing, logging, metrics, code reviews, deploys, etc.
4. What infrastructure the code is running on and how to interact with it
5. Who knows what and how to get questions answered
6. How planning is done, what are the team's current priorities, what should I
  be working on to make the biggest impact, etc.

On top of this giant pile of things to learn about, the start of a new job
is often when I'm feeling the most "buyer's remorse" around my decision to
switch employers- maybe I should have stayed at my old job. Or,
maybe it was right to leave my old job, but maybe I should have picked
one of the other offers I had.

The end result is that the onboarding process is really stressful for me- I
often feel kind of crappy, and then I may have trouble sleeping, which makes
me feel even worse. Even if you're not as uptight as I am, it's generally not
the time in your career when you're going to be at your peak happiness.

## Coping strategies

### Give it time

The most important coping strategy is to realize that it takes time to get
up-to-speed, and, at the same time, to realize that your colleagues know this
and will cut you some slack in the interim.

The exact amount of time required varies from company to company, and it's
something that you should ask your manager about in your first 1:1 meeting. However,
at most of my previous jobs, the general guidance has been that it takes around
3 months to start making non-trivial contributions, and around 6-9 months before
new hires are expected to be fully productive.

During those first couple of months, you can relax- it's ok to make mistakes, and it's
also perfectly fine to spend time doing background reading, getting to know colleagues,
attending internal tech talks, etc. as opposed to focusing completely on your
team's regular work.

### Get work environment right

I find that my work environment plays a big role in my productivity and happiness.
I'm particularly sensitive to my mouse, keyboard, and monitor. If any of these
is not ideal, I press very hard to get replacements ordered ASAP.

Fixing a desk


### Do coffee chats



### Create personal reference document

Starting on my first day, I create a document in whatever system the company
prefers for technical docs (e.g., Dropbox Paper, Quip, Google Docs, etc.) and
start jotting down anything that I think will be helpful to refer to later;
here are some examples:

```markdown
Key documents:
1. Design doc for system X
2. Intro to technology Y
3. External tutorial on doing Z
...

How to deploy system X
1. `cd ~/workspace/x`
2. `deploy -x -b 123abc --production`

Running tests for system Y
1. `cd ~/workspace/y`
2. `docker-compose up -d`
3. `make tests`
...
```

I treat this document as append-only- as I interact with more systems, I just
add more and more. After a few months, this document becomes a personal reference
for me- I can copy and paste


### Personal GitHub repo

In conjunction with my notes doc, I find it's also helpful to have a "sandbox"
where I can put longer scripts, play around with whatever libraries or frameworks
the company uses, and, have a private place where I can test out
things relevant to my team's work without being judged by colleagues.

At companies that use GitHub (including all of my recent employers), I just
put this stuff into a repo that's under my work account but separate from the
company's main GitHub organization. If your employer is using some other system for
storing code, you can just throw your changes into an "experimental" branch that
isn't submitted for review.
