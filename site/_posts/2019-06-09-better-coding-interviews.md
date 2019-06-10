---
layout: post
title:  "The rules for better coding interviews"
date:   2019-06-09 16:49:00 -0700
categories: interviewing
---

In a [previous post](/blog/master-coding-interviews), I discussed preparing for coding
interviews as a candidate. In this post, I want to flip to the other side of the table
and talk about conducting better interviews from the interviewer perspective.

## Goals of an interview

Before digging into the details, it's worth reviewing what the purpose of an interview is-
figuring out whether a random person who you probably don't know much about (i.e., the candidate)
is a good match for a specific position at your company (i.e., the job).

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

Now that we've

### Rule 1: Coding problems should be done on a computer, not a whiteboard

Writing code on a whiteboard made sense 25 years ago, before laptops were ubiquitous and
when compiling and testing small programs could be painful due to primitive dev tooling.
Now, it's a really bad idea. Unless you happen to be at a company where software
is written without computers, having a candidate use a computer is much closer to the work in the
actual job and, therefore, is a more accurate way to predict job performance.

Beyond the high-level, philosophical reasons for doing coding problems on computers, there are
a number of practical benefits for both the candidate and the interviewing company:

1. Writing code on a computer allows the candidate to use the tooling that they feel comfortable
  with and that makes them most productive. Since engineers at most companies are allowed to pick
  their own tooling for each project (within reasonable limits), this better matches the conditions
  of the actual job.
2. On a computer, you can't hand-wave away parts of your solution (e.g., "suppose we had a helper
  function that implemented a binary search"). The candidate has to either implement it themselves
  or find some existing code or library to use.
3. Coding problems on computers usually require the candidate to write tests and then iteratively
  debug problems that are found. These testing and debugging skills are an important part of
  software engineering work, but they're much harder to evaluate on a whiteboard.

### Rule 2: Please, no algorithm or data structure trivia

Understanding algorithms and data structures is a prerequisite for writing good software. Having
them all committed to memory, however, is not, particularly for the long tail things that are
rarely encountered in day-to-day work. Quizzing a candidate on lexicographic sorting, heap
implementations, or reversing linked lists is usually just a waste of time- if you need to
understand the details of these things on the job, you can just look them up.

The same goes for trivia about programming language syntax, operating systems, hardware,
or other technical topics. If it's something that people can either pick up on the job or look up
as needed, you're not actually measuring something that's critical for success on the job; instead,
you're picking up correlated skills (e.g., studying and memorization) that may not be completely
relevant.

### Rule 3: Avoid one-shot, all or nothing problems

Most problems that engineers work on are done in stages. You usually don't deliver a new system in
a single commit. Instead, you start with the high-level data models and interfaces, sketch out
the key classes, fill in the blanks with basic implementations, then come back and optimize
as needed. At each stage, you get feedback from your peers (or, in some cases, your end users), and
make course corrections as needed before continuing the next stage.

Coding problems done in interviews should, ideally, be structured in a similar way. Instead of
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

Over the course of my career, I've seen other

### Mini-projects

Instead of asking smaller, 45-60 minute questions, some companies

### Pairing

