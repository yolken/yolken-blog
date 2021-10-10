---
layout: post
title:  "The rules for better coding interviews"
date:   2019-06-09 16:49:00 -0700
tags: interviewing
related_posts:
  - title: "Using Leetcode to master coding interviews"
    slug: "master-coding-interviews"
  - title: "How to do an architecture interview"
    slug: "architecture-interviews"
excerpt: |
  In a previous post, I discussed preparing for coding
  interviews as a candidate. In this post, I want to flip to the other side of the table
  and talk about conducting better interviews from the interviewer perspective.
---

In a [previous post](/blog/master-coding-interviews), I discussed preparing for coding
interviews as a candidate. In this post, I want to flip to the other side of the table
and talk about conducting better interviews from the interviewer perspective.

## Goals of an interview

Before digging into the details, it's worth reviewing what the purpose of an interview is-
figuring out whether a random person who you probably don't know much about (i.e., "the candidate")
is a good match for a specific position at your company (i.e., "the job").

The most reliable way to figure out whether the candidate is a match for the job is to
observe them doing the job or, at least, doing activities that are as close as possible to the
work involved in the job. If you were interviewing a chef for a restaurant, you would ask
them to cook a meal for you. Likewise, in the case of a software engineer, your interview should
focus on things that software engineers actually do day-to-day- writing, testing, and running code
on a computer, debugging issues in systems, and explaining technical ideas to colleagues, among
other things.

Questions that are not directly related to day-to-day work on the job may have some correlation
with eventual job performance, but it's not going to be as strong. Given the amount of time required
for the interview on both sides as well as the risk of bad hiring decisions, it's best for all
questions to be as practical and job-relevant as possible.

## The rules

Now that we've covered the purpose of interviewing, I'd like to share some "rules" for coding
interviews to ensure that they're productive and provide good signal.

### Rule 1: Coding problems should be done on a computer, not a whiteboard

Writing code on a whiteboard made sense 25 years ago, before laptops were ubiquitous and
when compiling and testing small programs could be painful due to primitive tooling.
Now, there's really no good reason to do it. Unless you happen to be at a company where software
is written without computers, having a candidate use a computer is much closer to the work in the
actual job and, therefore, is a more accurate way to predict job performance.

Beyond the high-level, philosophical reasons for doing coding problems on computers, there are
a number of practical benefits for both the candidate and the interviewing company:

1. Writing code on a computer, ideally their own computer, allows the candidate to use the tooling
  that they feel comfortable with and that makes them productive. Since engineers at most
  companies are allowed to pick their own tooling (within reasonable limits), this better matches
  the conditions of the actual job.
2. On a computer, you can't hand-wave away parts of your solution (e.g., "suppose we had a helper
  function that implemented a binary search"). The candidate has to either implement it themselves
  or find some existing code or library to use.
3. Coding problems on a computer requires the candidate to write tests and then iteratively
  debug problems that are found. These testing and debugging skills are an important part of
  software engineering work, but they're much harder to evaluate on a whiteboard.

### Rule 2: Please, no algorithm trivia

Understanding algorithms and data structures is a prerequisite for writing good software. Having
them all committed to memory, however, is not. This is particularly true for the long tail things
that are rarely encountered in day-to-day work. Quizzing a candidate on lexicographic sorting, heap
implementations, or reversing linked lists is usually just a waste of time- if you need to
understand the details of these things on the job, you can just look them up.

The same goes for trivia about programming language syntax, operating systems, hardware,
or other technical topics. If it's something that people can either pick up on the job or look up
as needed, you're not actually measuring something that's critical for job success; instead,
you're picking up correlated skills (e.g., studying and memorization) that may not be relevant.

### Rule 3: Avoid one-shot, all or nothing problems

Most problems that engineers work on are done in stages. You usually don't deliver a new system in
a single commit. Instead, you start with the high-level data models and interfaces, sketch out
the key classes, fill in the blanks with basic implementations, then come back and optimize
as needed. At each stage, you get feedback from your peers (or, in some cases, your end users), and
make course corrections as needed before continuing to the next stage.

Coding problems done in interviews should ideally be structured in a similar way. Instead of
just throwing a problem out and asking the candidate to solve it end-to-end in one burst, it's
better to divide it into chunks and work through it in stages- first, have the candidate write
a skeleton class, then ask them to add in a method to do X, then a method to do Y that uses X, etc.
Ideally, there should be a long list of these extensions so that even the best candidates never
make it through all of them.

In addition to being more like real projects, this approach has a number of other,
interview-specific benefits:

1. Candidates are eased into the problem gradually. If they're prone to interview anxiety
  (as I often am), this makes them feel more comfortable.
2. Having seen the problem before is less of an advantage. The candidate may be able to get
  an answer to the core parts very quickly, but then you can just ask harder and harder extensions
  which they're less likely to have prepared solutions for.
3. Performance is less likely to be binary. Even weak candidates should make some progress,
  whereas stronger candidates will get to different parts of the problem depending on their
  skills and background. This allows for more granular feedback than simply "they got the problem
  so they passed" or "they didn't get it so they failed".

## Other approaches to more practical interviews

Over the course of my career, I've seen companies take other approaches to make their
interviews better match real work. These are less common and a bit more controversial than
the rules above, so I'm putting them in their own section.

### Mini-projects

Instead of asking a bunch of smaller, 45-60 minute technical questions, some companies have their
candidates do a single "mini-project". The work is either done at home, before the interview,
or for a couple of hours on site. Ideally, the candidate doesn't just submit their code but also
gets a chance to present their work and discuss why they took the approaches that they did with
their interviewers.

I think these projects can be a good way to make interviews more realistic and give candidates
a chance to show off their skills. On the other hand, when the project is done at home (as is
usually the case), there's pressure to spend a lot of time on it, way more than the suggested
amount, to make a good impression. This can be unfair for candidates who have full-time jobs
and/or significant personal obligations outside of work.

### Pairing

The idea here is to have the candidate pair with a member of the team instead of solving interview
problems by themselves. The pair can work together on either made-up interview questions or,
in some cases, actual project work for the company. Ideally, the company has hardware set up
that's designed for pairing, i.e. two monitors, mice, and keyboards connected to a single computer.

The advantages over standard, non-paired interviews are that:

1. The interview better tests collaboration, a big part of practical software work, by forcing the
  candidate to work directly with someone else.
2. The interviewer can step in and help the candidate make progress when they get stuck.
3. If the pairing is on actual project work, the interview can be a more realistic test of how
  well the candidate will perform on the job.

I think there are good intentions here. In practice, though, there are a number of issues I've
seen with pairing interviews that make me have mixed feeling about them:

1. If the company provides its own hardware, then the candidate might be forced to use a setup
  that's not ideal for them.
2. Often, there really isn't much pairing going on- the interviewer just watches the candidate solve
  the question like in a normal, non-paired interview.
3. If the pairing is on actual project work, then the candidate is basically being forced to do
  unpaid work. Aside from the potential legal issues involved here, this can feel
  exploitative.

## Concluding thoughts

Interviews should measure how well candidates do on realistic problems under job-like constraints.
Despite the common sense behind this, I still see companies routinely asking abstract, one-shot,
whiteboard coding questions. Just don't do this- it's not the way to hire the best people.