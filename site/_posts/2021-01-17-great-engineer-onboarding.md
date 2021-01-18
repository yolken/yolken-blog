---
layout: post
title:  "Great engineer onboarding"
date:   2021-01-17 10:58:00 -0700
categories: general tech
excerpt: |
    Starting a new software engineering job is hard, and making this process
    successful requires a lot of effort from both the employer and the
    employee. In this post, I want to focus on the former, and in particular
    how companies can make their onboarding processes better.
---

I've written a few posts previously about quitting a job
(see [1](/blog/leaving-a-job) and [2](/blog/quitting-a-new-job)).
Now, I want to turn my attention to a happier and more exciting topic-
what happens when you show up for the first day at your next company.

Starting a new software engineering job is hard, and making this process
successful requires a lot of effort from both the employer and the
employee. In this post, I want to focus on the former, and in particular
how companies can make their onboarding processes better. A follow-up post
will offer advice on getting up-to-speed from the employee perspective.

## Onboarding approaches

I've gone through seven onboardings in my tech career so far. Although the details
have varied a lot from company to company, I've broadly seen four different
styles of onboarding programs, each described below. Note that these aren't
mutually exclusive- some companies have adopted hybrid approaches that combine
multiple styles.

### Full bootcamp

The most intense onboarding process is what's referred to as an engineer
"bootcamp".

The analogy here is to bootcamp (also called "basic training") programs in the
military. These work by taking a bunch of people from different backgrounds,
grinding them down, and then building them back up in a uniform, structured way
that lays the foundation for being a good soldier. Those who graduate then go on
to more specialized training for their specific roles.

Tech onboarding bootcamps aren't quite as intense (no head shaving or being
yelled at by a drill sergeant, fortunately!), but the general idea is the same-
to take a diverse set of new "recruits" and give them all the same, basic skills
required to be a productive software engineer at the company.

Typically the way it works is that each cohort of new hires is seated together
in the office. For several weeks, they attend classes together and do various,
small exercises (e.g., bug fixes) either alone or in smaller groups.

Most new hires are not pre-assigned to teams. Instead, towards the latter half
of the bootcamp, a matching process takes place in which each person tries to find a
team that they're interested in, that has available headcount, and where the hiring
manager is willing to bring them on. Hiring managers might assign small technical
tasks to test out potential team members and ensure that they'll find the work
interesting.

At the end of the bootcamp, those who have met the minimum requirements "graduate"
and move onto their chosen teams. The small subset of people who don't graduate
with their cohort are typically given a bit more time to figure things out, but will
eventually be forced to leave the company if they don't complete the program.

Facebook is the best-known adopter of this approach. I haven't worked
at Facebook, so I'm not familiar with all the details of their program,
but I went through a new hire bootcamp when I started at Airbnb, who modeled
theirs after the Facebook one.

### Mini-project bootcamp

A less intense variant of the full bootcamp is one in which the new engineers
are all pre-assigned to teams, so there's no weed-out or team selection process.
Instead, the starting class is divided into smaller teams, each of which works
on a mini-project for a few weeks to get more familiar with the company's tools,
systems, and products. After the project is done, the teams are disbanded and people
begin onboarding with their real, assigned teams.

I went through a process like this when I started at Stripe- they called it
"dev/start", and it took around 5 weeks. I've heard of other companies having
programs like this, but they're typically optional and intended primarily for
more junior engineers.

### Lightweight, team-driven

An alternative to having structured, multi-week training programs is to push
most of the learning process onto individual teams. After a few days of
general orientation, new engineers go and sit with their assigned teams and
start an onboarding process that's customized by their manager for their specific
role.

The details vary, but typically the manager will write up a personalized "new hire"
doc with a specific list of tasks that the person is expected to do (e.g., meet with person X, read this design doc, etc.). The new hire is typically also assigned a
"starter project" to get their feet wet and matched with a "new hire buddy" on the
team who can help answer low-level technical questions.

The first few weeks may be interspersed with classes, social events, and other
activities that the new hires can participate in together. But, they're generally
optional to attend and fairly low key.

Many companies of lots of different sizes have adopted this approach. I went
through it at Google, and then more recently when I started at Segment.

### Bare bones

The least intense onboarding is one that's completely minimal. New hires
sign some forms, are shown to their desks, and then immediately dive in to their
work (with some manager guidance).

This is typically the approach taken by smaller startups that don't yet
have the critical mass to justify creating a formal onboarding program.
I experienced this when I joined MoPub, which at the time had only
around 45 employees.

## Lightweight is best

Based on my various job starting experiences, I personally feel that
the "lightweight, team-based" approach described above is far and away the best
choice for most companies.

Here are some reasons why.

### Onboarding isn't a one-size-fits-all activity

The members of a new hire cohort might range from new grads to industry veterans with
30+ years of experience. Even in small companies, people will most likely be assigned
to different teams working on different parts of the product and using different
technical stacks.

In this environment, it's impossible to have a multi-week, general training program
that's optimal for everybody. Even if you break it up into subspecialties (e.g.,
"frontend bootcamp" vs. "mobile bootcamp"), there's still a tendency for it to be
too fast, too slow, too general, or too specialized for some subset of the
participants.

The most efficient way to get engineers up-to-speed is to have them dive in on
project work. And, the best way to do this is to have engineers join their teams
early on in the process and lean on their managers and peers for guidance.

The other nice thing about the guided, "dive in" approach is that it can be heavily
customized on a person-by-person basis. A new grad or someone who's never worked
in the team's tech stack might be given smaller, easier starter tasks than someone
who's already an expert in the technology. New hires are able to get up-to-speed
at their own pace, without the wasted time or excess stress of a group training
program.

### Group classes have limited utility

Orientation classes can be fun at the beginning, but, after hours and hours
of sitting in a stuffy room and listening to presentations, attentions
wane and the sessions all start to blend together. In addition, these classes
by their very structure, are very much "one-size-fits-all" activities that can't
be easily customized for the requirements of each person's job.

Personally, I think a day or two of classes at the beginning is fine, provided
that these are devoted to things that are necessary and relevant for
all new hires (e.g., how to get paid, a summary of the company's products,
what the core values / operating principles are, etc.). But, beyond that,
classes should be optional and also non-continuous so that attendees can
fit them in with their team-specific onboarding tasks.

As an alternative to classes, a much better use of resources is to create
great onboarding documentation. Unlike a presentation, which tends to go in
one ear and out the other, documentation sticks around forever and can easily
be consulted after the onboarding is done. People can also work through
documentation at their own pace and skip over topics that they already know
about or aren't relevant for their work.

Google had a particularly nice balance here. There were a few technical
onboarding classes, but they were extremely high-level and designed to be more
about the social and cultural aspects of engineering than the technical ones
(as I recall, they also had cute names like "life an engineer"). Technical
training, where needed, was instead done via written "code labs" that engineers
worked on individually.

### Doing team assignments during onboarding is crazy



## Conclusion

The best approach to onboarding engineers is to quickly integrate them with
their pre-assigned teams. Doing days or weeks of