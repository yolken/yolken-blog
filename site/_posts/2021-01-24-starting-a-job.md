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

First off, it's important for me to state that I find starting a new
job as a software engineer really, really hard.

Even after many years of experience and even if the new company is using a tech
stack that I'm already familiar with, there is
just so much to learn about before one can become productive, including:

1. Where the code lives and how it's organized
2. The key software systems, their interfaces, and how they all fit together
3. Standards and tools for testing, logging, metrics, code reviews, deploys, etc.
4. What infrastructure the code is running on and how to interact with it
5. Who knows what and how to get questions answered
6. How planning is done, what the team's current priorities are, what I should
  be working on to make the biggest impact, etc.

On top of this giant pile of things to learn about, the start of a new job
is often when I'm feeling the most "buyer's remorse" around my decision to
switch employers. This can include thoughts like "maybe I should have stayed at my
old job". Or, I'll be thinking that it was right to leave my old job, but that
maybe I should have picked one of the other offers I had.

The end result is that the onboarding process is really stressful for me- I
often feel kind of crappy, and then I may have trouble sleeping, which makes
me feel even worse. Even if you're not as uptight as I am, it's generally not
the time in your career when you're going to be at your peak happiness.

## Coping strategies

Over the course of starting many new jobs, I've developed a collection of strategies
for making the onboarding process less stressful and more productive. Here are the most
helpful ones.

### Give it time

The most important coping strategy for me is to realize that it takes time to get
up-to-speed, and, at the same time, to realize that my colleagues know this
and will cut me some slack in the interim.

The exact amount of time required varies from company to company, and it's
something that I ask my manager about in our first 1:1 meeting. However,
at most of my previous jobs, the general guidance has been that it takes around
3 months to start making non-trivial contributions, and around 6-9 months before
new hires are expected to be fully productive.

During those first couple of months, I tell myself that I can relax- it's ok to make
mistakes, and it's also perfectly fine to spend time doing background reading,
getting to know colleagues, and attending internal tech talks as opposed to focusing
completely on my team's regular tasks.

### Get work environment right

I find that my work environment plays a big role in my productivity and happiness.
This is particularly true when I'm starting at a new job and dealing with the
firehose of technical things that I need to get up-to-speed on.

The first thing I try to optimize is the company-provided hardware that I'm touching
or looking at for my day-to-day work, i.e. my laptop, mouse, keyboard, and monitor.
If any of these is not ideal, I press very hard to get replacements ordered during
my first few days on the job (within reasonable bounds, of course).

Beyond that, I then work to improve the other aspects of my environment, including
my desk and chair, and the light, noise, and temperature of my immediate work area.
Now that I'm working from home these are all under my direct personal control, but
back when I was in an office I sometimes asked for help in dealing with noisy
officemates, weird vibrations in my desk, or a less-than-comfortable chair.

Many of these things will take a while to resolve, so it's important to raise
concerns early on to get the process started.

### Do coffee chats

Getting to know your manager and the peers on your team is a critical part
of the onboarding process that everyone does. Beyond this, though, I've found that
it's really informative to meet with colleagues beyond my direct team, even if I'm
not going to be working with them at all. I usually just message these people
in the company's chatting system and ask for permission to put 30 minutes into their
calendar (they almost always say yes!)

Staff in the extended organization can provide "big picture" perspective
that's useful to know about as I'm getting up-to-speed. Also, because they won't
be working with me day-to-day, I've found that they tend to be more honest and less
inhibited when it comes to providing advice about how to be successful in the job.

When possible, I like to structure these as "coffee chats" as opposed to formal
1:1's. This makes them more fun and fosters an environment in which we can
talk honestly.

### Create personal reference document

Starting on my first day, I create a document in whatever system the company
prefers for technical docs (e.g., Dropbox Paper, Quip, Google Docs, etc.) and
start jotting down anything that I think will be helpful to refer to later;
here are some made-up examples:

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

I treat this document as append-only- as I interact with more tools and systems, I
just keep adding more sections. Later, if I need to refer to anything, I can do a
quick search in the doc and then use the links or commands that I previously
jotted down to complete the task I'm doing.

I keep adding to the document and referring back to it even after I'm fully onboarded. Over
time, it can get so big that it becomes painful to load and search in whatever tool I'm using to
host it. When this happens, I'll just freeze the first document and start adding notes into
a new one. In my current job, I'm at the beginning of my second reference doc. In previous
jobs, I've gone through three or four of these over the course of a few years.

### Personal code sandbox

In conjunction with my reference doc, I find it's also helpful to have a personal
"sandbox" for code-related notes and experiments.

At companies that use GitHub (including all of my recent employers), I just
set up a repo that's under my work account but separate from the
company's main GitHub organization. If I were at a company that didn't have this
functionality in its code systems, I would just throw my changes into an
"experimental" branch that is never submitted for review.

Wherever it lives, I use this sandbox as a place to put longer scripts, to become more
comfortable with the frameworks and technologies that the company uses, and to try out
new approaches to my team's work. Doing these things in a personal space allows for me
to experiment and explore without judgement from colleagues.

As with the reference doc, I keep adding to my personal code sandbox even after the
onboarding process is complete. However, I generally find that it becomes less useful over
time as I become more comfortable with the company's tech stack and more confident in
my abilities to make changes out in the open directly.

## Conclusion

Starting a new job is hard, but I've adopted a few strategies that have consistently helped.
The optimal onboarding path can vary a lot from person-to-person and from job-to-job, so these
may or may not be ideal for you. However, you may find some subset of them helpful the next time
you're struggling to get up-to-speed at a new job.

Good luck and, most importantly, don't get too stressed!