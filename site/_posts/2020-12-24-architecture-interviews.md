---
layout: post
title:  "How to do an architecture interview"
date:   2020-12-24 12:26:00 -0700
categories: interviews
excerpt: |
    Blah blah blah
---

Most software engineering interview loops include an "architecture interview", where the
candidate is asked to develop a high-level design for a software system. Over the last few
years, I've given many, many of these interviews, so I've seen a wide range of performances
across the spectrum, from "absolutely terrible" to "we need to hire this person now!".

Based on these experiences, I'd like to share what it takes to succeed in these interviews,
and some common behaviors to avoid.

## How it works

Although the exact format can vary, most architecture interviews begin with an open-ended
prompt of the form "design *X*". The *X* can be filled in with a generic software system,
for instance:

1. A distributed [key/value store](https://en.wikipedia.org/wiki/Key%E2%80%93value_database)
2. A [web crawler](https://en.wikipedia.org/wiki/Web_crawler)
3. A system for scheduling [cron jobs](https://en.wikipedia.org/wiki/Cron) reliably across hundreds
  of machines
4. A video streaming system

Alternatively, and the approach that I think is more interesting, is to fill in the blank with
a well-known product or product feature; some examples here include:

1. Generating the Facebook news feed
2. Executing a Robinhood user's trade flow
3. Matching Uber drivers and riders

The question is left open-ended and high-level deliberately. The interviewer is not looking for
a specific answer (usually), but rather wants to observe the process by which you break down
the problem, dig into the pieces, justify your decisions, etc. As you discuss your solution,
the interviewer will ask questions, steer you towards or away from specific areas, and really try
to understand what it would be like to collaborate with you on the design of a real project.

## Structure is key

Because the questions are so open-ended, and because you're being evaluated as much on your
process as your specific solution, structuring your answer is really, really important. Here's
a structure that I think works well for most of these questions.

### Step 1: Clarification

Once you get the question, the first step is to make sure you understand what you're being asked
to design. For the "design a system to match Uber drivers and riders" example, for instance,
if you've never used Uber before it's probably good to say that and ask for more details.
Even if you're familiar with the thing being asked about, it's helpful to draw a simple picture
with stick figures to make sure that you and the interviewer are on the same page.

This is also the time to ask about rough orders of magnitude scale (e.g., how many requests
per second are expected, etc.). However, I wouldn't get too bogged down in these numbers- a
good design should have lots of room for growth and not be built to a specific set of static
dimensions.

### Step 2: High-level drawing

Next, you should draw out a high-level diagram that shows the major pieces and how they're
connected. As discussed later on, the idea here is to be high-level and not over-engineer at
this phase. However, you should mention that you're deliberately being simple and high-level,
and that you're dig into improvements later so the interview knows that you're not being sloppy.

In the Uber case, as in many others, you'll probably have clients, a layer of web servers,
and some sort of storage layer that keeps track of the states of the users and other entities
in the system.

### Step 3: Interface details

In conjunction with the high-level design, I think it's really useful to also describe the
interface for the system at this phase, i.e. what are the specific inputs and outputs, independent
of any internal implementation details. In the case of a client/server type design (most common),
these map to the requests that the clients make and the responses that they get.

Being really specific about these (the different types, what they include, etc.) ensures that
you and the interviewer are on the same page and also guides the discussion of the implementation
details in later steps.

In the Uber example, you'll have requests from the rider client (i.e., app) for a ride, requests
from the driver client to change status (i.e., available to new rides or not), to accept
a potential ride or not, etc. In this specific example, the request flows can be fairly complex
and are probably an important part of the design.

### Step 4: Implementation details

Once you've defined the high-level pieces and the interfaces, it's time to dig into the internal
implementation details. There are many different things you could focus on here, so it's really
important to lean on your interviewer for guidance. Some potential things to dig into here include:

1. Tradeoffs in choices around specific components (e.g., using a relational DB vs. a
  [NoSQL](https://en.wikipedia.org/wiki/NoSQL) solution)
2. How a specific request type is handled end-to-end (including DB changes, etc.)
3. Schemas for any data stores

### Step 5: Enhancements for scalability, performance, etc.

Once your interface and basic implementation are in place, then you can dig into the details
of how you'd make improvements to handle increased loads. This is also a good time to talk about
the reliability of your design and what you could do to improve it, if applicable.

As with the previous step, it's really important to lean on your interviewer here and try to
dig into the areas they feel are the most interesting to cover.

Although the exact solutions will vary based on the context, some general approaches that may
be helpful here include:

1. **Replication:** Stateless components can be replicated to handle more traffic. This may also
  help for stateful things like DBs if you send the reads and writes to different instances and can
  hand-wave away [consistency](https://en.wikipedia.org/wiki/Data_consistency) issues.
2. **Sharding:** Splitting up your traffic by geography, user id, etc. and allocating each bucket to
  a semi-independent copy of your system may allow you to increase scale without redesigning
  everything from scratch.
3. **Caching:** Adding caches in front of read-only data can significantly improve performance in
  many cases.
4. **Queueing:** Adding queues in your system can help shield downstream components
  from load spikes. However, it can increase latency and also is hard to implement in
  synchronous request flows, so it's most appropriate for asynchronous data pipelines.

## Common mistakes

Even with good structure, there are some pitfalls that frequently trip up candidates and
cause them to lose points

### Being too service-oriented

A common design pattern is

### Over-engineering too early

Related to SOA abuse is over-engineering your solution too early in the process. Yes,
having 3 layers of caching, or a queue between your app servers and your DB, or

### Using components you don't fully understand

### Getting specific in the wrong areas

Don't dig into the details on something

## Conclusion

