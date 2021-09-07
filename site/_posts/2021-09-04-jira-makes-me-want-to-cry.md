---
layout: post
title:  "Jira makes me want to cry"
date:   2021-09-04 18:25:00 -0700
categories: general tech
excerpt: |
  Every company I've worked at in the last 9 years, from small startups
  to multi-thousand-person public companies, has used Jira for managing software
  projects internally. In this post, I want to explain what Jira is and why
  interacting with it at work makes me feel frustrated and unproductive.
---

Every company I've worked at in the last 9 years, from small startups
to multi-thousand-person public companies, has used
[Jira](https://www.atlassian.com/software/jira) for managing software
projects internally.

While the goals of this system are admirable, I've found it to be a huge
pain to use in practice. In this post, I want to explain what Jira is and why
interacting with it at work makes me feel frustrated and unproductive.

## Aside: What is Jira?

Jira is an online project management system created by
[Atlassian](https://www.atlassian.com/), an Australian company that
makes some other software productivity tools as well.

A company's Jira account is divided into "projects" which, at many companies,
roughly map with teams. Within each project/team, users create issues (sometimes
referred to as "tickets") to represent individual things that need to be done,
e.g. bugs to fix or new features to add in the company's products.

Issues can be listed, categorized, and reordered within a number of different
high-level views, depending on how the associated project is
configured. For instance, there might be a
[Kanban board](https://en.wikipedia.org/wiki/Kanban_board) that lists issues
in columns by status (example below) or a "roadmap" view that shows a
[Gantt-chart](https://en.wikipedia.org/wiki/Gantt_chart)-like summary of when issues
are projected to be done.

<img src="/assets/jira_kanban.png" alt="Jira Kanban board" width="800"/>

Each issue is assigned to a single member of the team, who's then responsible
for working on it. As they do this, they update the status of the ticket in the UI
so that others at the company can track its progress. Finally,
when the work is complete, the ticket is marked as "Done" and the assignee moves on
to the next ticket in the team's queue.

## What it's supposed to do

Managing software projects is tedious. Once you get beyond a handful of people
working on something, you need some structure so that:

1. There's a well-known place to file bugs and TODOs so that people don't forget
  about them
2. Bugs/tickets/issues (whatever you want to call them) can be prioritized by teams
  so that the more important things are worked on before the less important ones
3. Issues can be assigned to developers so that each person knows what to do next and
  work isn't duplicated
4. Managers of various types (including project, program, product, and engineering)
  can see the big picture, make promises to customers, and reallocate resources
  as needed

These requirements could be handled by post-its on a whiteboard or rows in a
spreadsheet, but these quick-and-dirty solutions don't scale too well when you have
hundreds of people around the world, simultaneously working on dozens of interdependent
projects.

Jira, in theory, provides this structure at scale. It aims to allow companies
of all sizes to manage the chaos around software development and keep teams
well-organized, productive, and responsive to customer issues as they go about their
day-to-day work.

## The reality

Although Jira is nice in theory, the reality in my experience is terrible.
There's lots of other material out there that enumerates all of the problems
(someone even made [https://whyjirasucks.com](https://whyjirasucks.com/)), so
I'm not going to rehash every one here. Instead, I want to focus on my top
three frustrations.

#### (1) It's slow

Every operation in my work team's Jira project, whether loading the details a
single issue, doing a search across all of our issues, or updating the status
on an issue, feels sluggish. It's like I'm browsing the Internet through a modem
in 1998.

But wait, you might say, that's just because your employer's account is so
big and has lots of optional add-ons installed (Jira, like many other enterprise
SaaS products, offers a lot of customization). Well, I created a vanilla personal
account through [jira.com](https://jira.com) too, and, while it's a bit better,
the performance still isn't great.

The problem with the Jira sluggishness is that users are doing many operations
per session. When I go in, for instance, I might need to review a couple dozen
issues, mark some of these as done, create a few new issues, then reorder the
updated corpus. If each operation involves multiple seconds of latency, it
adds up to a lot of wasted time.

#### (2) Creating new issues is heavyweight

Creating issues is a core activity of an issue tracking system, so ideally
the process should be fast and lightweight. Unfortunately, Jira's ticket
creation flow is about as fluid as filling out a tax form; here's a screenshot
from my personal test account:

<img src="/assets/jira_create_issue.png" alt="Creating an issue" width="500"/>

There are so many fields that I had to shrink down my browser font
to fit everything in a single screen.

Not all fields are required. However, if some of the optional fields
aren't set correctly, then the issue might not show up in the team's
Kanban board or be associated with the correct epic, which means that I'll
need to waste time in the future trying to find it and categorize it
correctly.

#### (3) There are too many ways of doing things



## The result



## Where to go from here

Jira is such a productivity drain that I think companies should seriously consider
replacing it with something else. Unfortunately, I don't have a lot of experience
