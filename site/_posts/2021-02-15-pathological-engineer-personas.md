---
layout: post
title:  "Pathological engineer personas"
date:   2021-02-15 14:15:00 -0700
categories: general tech
excerpt: |
    Blah blah blah.
---

Software engineers are an interesting bunch. Over the course of my career thus far,
I've interacted with hundreds of colleagues, and it feels like I've seen everything- people who
refuse to wear shoes, people who can't make eye contact when talking, people who voluntarily start
their day at 6PM, and many other behaviors that would be considered "weird" in normal workplaces.

Most of these quirks don't bother me, and I have a few of my own. However, there are certain
traits that I've encountered, particularly on the personality side, that are genuinely annoying and
counterproductive to my team's work. In this post, I want to explain what these are and how I try
to deal with people who exhibit them.

## Pathological personas

The sections below go into more detail on each trait. I'm framing them as "personas" to make the
discussion a little more fluid.

### The overanalyzer

The overanalyzer gets hung up on analyzing every technical decision they encounter in their
day-to-day work.

The problem with overanalysis in the context of software engineering is that there are so
many choices to make on a daily basis. At the low-level, you have mundane things like variable names
and function interfaces- should it be `myFunc(config struct)` or
`myFunc(parameter1, parameter2, etc.)`? At the higher-level, there are bigger choices about
architectures and technologies- for our new container orchestration system, should we use
[Kubernetes](https://kubernetes.io/), [ECS](https://aws.amazon.com/ecs/),
[Nomad](https://www.nomadproject.io/), [Titus](https://netflix.github.io/titus/), or something else?

The problem isn't just the number of choices, it's that for many of them there isn't a single,
"right" answer. In many cases, e.g. the container orchestration example above, there are
perfectly valid reasons for picking any one of them over the others. A big part of software
engineering, and one of the things that distinguishes it from just "coding", is evaluating these
tradeoffs and making decisions, even when the choices can't be perfect on all dimensions.

Overanalyzers get paralyzed by these choices and thus can't make decisions quickly. As a result,
their productivity is low and, if their work is in the critical path, they can block the team
from making forward progress and meeting deadlines.

### The perfectionist

The perfectionist, unlike the overanalyzer, has a clear vision for what they want. However,
they refuse to accept anything short of their final vision- it has to be perfect, or it shouldn't
be done at all.

Perfectionism is really hard to achieve in software for a few reasons. First off, *all* software
has rough edges. No matter how much work you put into something, you're going to have some bugs
or errant pixels or missing features somewhere in your product. Secondly, most software progress
is delivered incrementally- you don't achieve perfection in your first release. Instead, you
address the highest priority features and/or bugs, deliver your product, get feedback, and then
repeat the cycle. Many large, successful software products like Microsoft Office or the Python
programming language have been doing this for decades.

Perfectionist software engineers get in the way by blocking your work unless you immediately address
their long list of idealized requirements.

Sometimes, the interactions are relatively mundane, e.g. in the context of a small code review:

> Them: I need you to refactor class X and backfill tests as part of your change.
>
> Me: My change only touched one line of X. I'm already rewriting Y as part of this change, I'm not
> making X worse, and I don't have any context on the original X code so it will take me days to
> untangle this mess.
>
> Them: Sorry, I can't approve until you fix this.

The blockers can be bigger when doing design or architecture reviews:

> Them: I can't allow you to roll out your new container orchestration system because it doesn't
> have signed images and an interactive UI.
>
> Me: Our current system doesn't have those things. No one other than you is requesting them,
> and it will take months to add them. We can work on those features in v2 if needed.
>
> Them: No. Either you have signed images and an interactive UI in v1 or there's no point.

Blocking regressions or things that explicitly prevent improvement in the future is definitely
worthwhile, but perfectionists take this to the extreme of blocking non-regressive, incremental
progress too.

### The Luddite

The Luddite is unreasonably resistant to any sort of big, technological change. They believe
that the current ways of doing things, despite their faults, are superior to any new approaches that
come along.

Luddism doesn't mesh well with software engineering because software technologies, tools, and
best practices are constantly evolving. Just because things like PHP and Java were state-of-the-art
20 years ago doesn't mean that they're still the best choices for every project today. Of course,
there are tradeoffs here- older technologies can still be very good, and there are definite
downsides to switching things around just for the sake of using the latest and greatest tech.

The Luddite, however, is uniformly and stubbornly insistent that new projects, even ones that
are completely "greenfield", make only minor adjustments on top of the company's existing
standards and technologies.

Over the last few years, I've sometimes hit this persona when trying
to roll out Kubernetes and other, big infrastructure improvements at a company:

> Them: Our current orchestration system is great, we don't need Kubernetes.
>
> Me: Well, it has a lot of issues. For instance, it takes 7 days and approvals from 3 people to
> create a new service. And, the configs are spread across 6 repositories.
>
> Them: We're working on a big project to cut that down to 6 days, 2 people, and 5 repositories. It
> will be ready at the end of next year.
>
> Me: Umm, maybe there's a better way? Please hear me out.

Often times, the resistance is rooted in personal feelings. The Luddite has invested a lot of time
and energy in the current ways of doing things, and they feel that adopting something new will
diminish their previous contributions. Or, they're worried that new technology will take away
their control and thus reduce their future influence inside the organization.

### The complainer

The complainer spends an inordinate amount of time complaining about the faults in other
people's work in a way that blocks progress.

Don't get me wrong here- there's something very cathartic about complaining, and I think we all
enjoy doing it every now and then. However, it becomes a problem when the person complaining
is giving feedback that's not actionable or, if actionable, without any willingness to help make
things better.

A quick story- at the beginning of my career, I was a product manager on Google's system
for allocating compute and storage resources inside the company. Teams would get these resources
and then build the company's externally-facing products (e.g., search, Gmail, YouTube, etc.) on top
of them.

Our system, to put it mildly, was not the most popular among engineers at Google. I routinely heard
complaints that it "sucked" or "should be deleted". One very senior person even told me that he
hated our system more than his recent experience of being stuck in the Atlanta
airport with a screaming toddler for 12 hours.

None of these people really had any ideas for how to make our system better. Instead, they just
demoralized the team and blocked us from making progress since they would be fighting
against us as we tried to get more resources or push through incremental improvements.

Since moving on from my stint in Google's resource management organization, this level of
negativity has been pretty rare. However, I'm still sometimes blocked by complaints without much
willingness to help.

One example is in the context of security reviews, which many companies
require for new product launches. At a previous job, my interactions with the security engineer
went like this:

> Them: Your service isn't secure. You need to do more to ensure that only authorized users can
> make requests to your API endpoints.
>
> Me: Hmm, I'm not really an expert on security. Can you help me with this or at least point me
> to an internal example that does things the "right" way?
>
> Them: Oh no no, I'm way too busy to do that. You really need to figure it out yourself.
>
> Me: *Sigh.*

I've also seen this behavior in interactions with lawyers (technically, they're not engineers, but
they interact with us a lot, so I'm including the example):

> Them: Your product feature is not compliant with EU regulation 124-XZ. I can't let you launch it
> in its current form since this would put the company at great legal risk.
>
> Me: Ok, what specific things do I need to change to make the software compliant?
>
> Them: Well, 124-XZ is really complicated, it's hard to say. I'll have to get back to you.
> *Silence for weeks.*

Complaints are fine, but if they don't come with any offer of help (or at least specific details
of what to fix), then they can really block progress on a project.

### The nexus

The nexus wants to be at the center of all decisions, and gets upset when they're not consulted
about each one.

As described in the "overanalyzer" section above, software development involves making a lot of
decisions. Once you get beyond a small number of people, however, it's really, really hard for any
one person to be involved in each one. At a certain point, you just have to relax, trust
other people to do the right thing, and realize that if someone does make a terrible decision
without your knowledge, you can usually fix it after-the-fact.

The nexus, on the contrary, will insist that they be included in every meeting and code review
related to your project. By doing this, they necessarily slow down progress- nothing can be
done until they approve, and since they're only one person, the progress of the team is slowed
down to the rate at which they're able to process and critique each step of the project.

If you go around them, the nexus may discover and get upset. Worse than that, though, they may
overcompensate by jumping in and second-guessing all of the decisions you made without them- e.g.,
"Why did you call this setting `x` as opposed to `y`?"- which slows you down even more than if
you had consulted them at the beginning.

Unfortunately, nexus behavior is often mixed with the other traits described above. In combination,
these can be an especially big drain on engineering productivity.

## Coping

Here are some strategies for dealing with the above personas when they get in the way of your
work.

### Be direct

The most direct strategy is to call out these pathological traits when you see them.
If you're in a code review, for instance, you can explicitly push back against the reviewer's
feedback because it's not constructive or is requesting an unrealistic amount of perfectionism in a
single change.

The key here is to communicate sympathetically. You want to acknowledge the feedback and also
explain nicely why it's not 100% reasonable. In many cases, the person will understand
what you're saying and agree to back off.

### Evade

The more passive-aggressive approach is to evade the person with the unproductive trait(s) by
avoiding contact with them. If these traits come through in code or design reviews, for instance,
you can just request reviewers are who more likely to be helpful.

This isn't always doable (there may be only one person who can review your changes), but it
avoids conflict and helps move things forward. If the person you evaded discovers a serious
problem that their involvement would have detected, you can still apologize, beg for forgiveness,
and ask for their help.

### Escalate

A third option, and sometimes the only one that works, is to escalate your concerns to
management. If someone is blocking progress and being completely unreasonable, managers have the
power to push them aside and/or elevate someone more reasonable to unblock you.

It may take a while to get results and it may burn some bridges, but at a well-run company
management should be effective at removing blockers and ensuring that employees can be productive.
If they can't do this, then it might be time to switch teams or switch companies.

## Conclusion

Certain personas can really get in the way of being happy and productive as a software engineer.

Many of these are actually beneficial in small doses (e.g., perfectionism), they're just problematic
when taken to an extreme. Also, despite our best intentions, I think we all, myself included,
exhibit them sometimes in our interactions with colleagues.

The important thing is to recognize when they're reducing productivity and then make
the necessary structural or personnel changes to unblock progress.