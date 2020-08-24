---
layout: post
title:  "Stop hiding levels"
date:   2020-03-29 13:27:00 -0700
categories: career
excerpt: |
    Most tech companies, even those without formal job titles,
    assign "levels" to engineers. Despite the importance of levels for determining compensation
    and job expectations, many companies prevent non-management employees
    from seeing anyone's levels besides their own. In this post,
    I explain why this is a harmful practice that should be
    discontinued.
---

Most tech companies, even those without formal job titles,
assign "levels" to engineers. These levels are used to set initial
pay when an offer is made and then, after joining, for evaluating
performance and determining subsequent pay adjustments and promotions.

Despite the importance of levels for determining compensation
and job expectations, many companies prevent non-management employees
from seeing anyone's levels besides their own. In this post,
I want to explain why this is a harmful practice that should be
discontinued.

## Aside: Intro to eng levels

### What they are

Although different companies use different labels and titles for their levels,
most of them assign engineers to the following buckets:

| Bucket  | Typical IC Titles  | Typical Manager Titles |
|---|---|
| 1  | SWE 1, new grad | - |
| 2  | SWE 2  | - |
| 3  | Senior engineer  | Engineering manager |
| 4  | Staff engineer | Engineering manager, senior engineering manager |
| 5+ | Senior staff, principal, etc. | Senior manager, director, VP, etc. |

The first two buckets/levels are typically IC (individual contributor) only. Starting at the
third level, people can choose to stay in the IC track or switch over to management. The
ranks thin out considerably above the fourth level, so I've compressed these
in the table above.

As mentioned previously, the labels for the levels vary considerably between
companies. Google, for instance, starts its leveling scheme at "3" instead of "1", and as
a result a bunch of other companies who love copying Google (or copying companies that
have already copied Google, like Facebook) do the same thing. The boundaries between
the levels can also vary a bit, particularly in the higher ones; some companies make it
relatively straightforward to get to the fourth and fifth levels, for instance, whereas
others require many, many years of continuous high performance to be promoted above the
"senior" one.

If you're curious about the levels at a specific company, [levels.fyi](https://levels.fyi)
seems fairly accurate and also attempts to show apples-to-apples comparisons between
different companies.

### What they mean

Levels play a huge role in compensation. When a company extends a job offer, it's calculated
from the level they have determined for you based on your interview performance and
prior work experience. When you negotiate with them on the offer details, they're just
moving the numbers around within the pre-determined (and usually secret) pay and equity bands
for your level.

Once you're on the job, your level determines the expectations for your role and, as
a consequence, how your performance is evaluated. This, in turn, determines the magnitudes
of any pay increases or bonuses you earn as well as your eligibility for promotion.

Surprisingly, levels don't play a big role in day-to-day work, at least for IC engineers.
People at higher levels are expected to work on bigger, more technically complex
projects, but nothing stops a new-grad from working on a challenging, multi-month project or
a principal engineer from fixing small bugs and responding to alerts in the middle
of the night.

## Why levels are kept secret

Companies that make levels secret usually justify this by a desire to prevent
higher-level people from "pulling rank". The idea is that if levels
are open and an L2 and an L5 (using the numbers from the table above) are having a
heated technical discussion, the L2 might be intimidated and feel that they can't
challenge the L5's judgement. In the alternative world where levels are secret,
the thinking goes, the two sides will treat each others as equals and be forced
to resolve disputes objectively, based solely on the merits of each alternative.

The reality, however, is that people can, and do, still pull rank when levels are
secret. The L5 can't say "listen to me because I'm a senior staff engineer", but
they can say "listen to me because I've been at this company longer than you have".
With levels taken away, people revert, either implicitly or explicitly, to seniority, age,
project responsibilities, and other things that loosely correlate with level. These
criteria, however, are no more "fair" and objective than what they're replacing, and, in
some situations, are strictly worse.

Another argument for secret levels is that it prevents "resentment", particularly
when people feel that a peer's level is not justified given their job performance.
If the company's leveling and promotion policies are unfair, however,
people will figure this out eventually, whether or not the levels are open. Instead of
attempting to hide the problem, companies that are afraid of blowback from their
levels should address these issues head-on, by fixing the underlying process and/or
giving more detailed justifications for their decisions.

Finally, a more cynical reason for keeping levels secret is that it gives ICs
less negotiating power in discussions with management. If I'm an L3 and I know
that I'm performing better than higher-level people on the team, I can argue for
a promotion and a raise. If I don't know this, I'm less likely to complain,
and, even if I do, my arguments will be easier to dismiss. This "information
asymmetry" gives the company an edge that can help it save money.

## The downside of secret levels

The worst aspect of secret levels is that they make career progression harder
for IC engineers, particularly as they become more senior. Explaining why this
is true requires a bit more background on how performance evaluation works
behind-the-scenes.

Engineer performance at most companies is evaluated through a combination of peer,
self, and manager reviews at each cycle (typically every 6 months). To make sure that
evaluations are fair and to assign the official ratings, there's usually a "calibration"
process done by managers, followed, at some companies, by a "promotions committee" that
decides who gets leveled up.

The evaluations at these meetings are nominally done based on a set of
non-secret, objective criteria for each level, e.g. "an L3 engineer should be
a technical expert in at least one area" or "an L5 engineer should lead a major,
1-2 year effort". In practice, however, the easiest way to evaluate someone's
performance is to compare them to their peers-- e.g., "Alice is an L3 and she's
operating at the same level as the L4s on the team, therefore she should be promoted"--
and this is, in fact, how these judgments are often made.

The problem is that if you don't know the levels of your peers, it's hard for you
to understand where you stand and what you should be aiming for to get to the next
level. It also makes it hard to write accurate peer reviews (a feature of most
tech companies' processes) because you don't know exactly what the expectations
are for the person you're reviewing. Ultimately, because peer reviews can't address
specific leveling criteria and comparisons to other team members at the same level, each
person's evaluation is based more on managers' personal judgments. This makes the
outcomes more arbitrary and less fair.

Companies with secret levels realize that this is a problem and typically
address it by publishing a set of "personas" alongside their official leveling
criteria. At one of my former employers, they were structured like this:

> Sally is a senior engineer on the search infrastructure team. Last quarter,
> she led a project to migrate the search backend from a giraffe-based architecture
> to a cheetah-based one, which involved close collaboration with the search
> frontend and product teams. She also did 30 interviews and represented the company
> by giving a presentation at State University's job fair.

That's great if you're on the search infrastructure team and are working
on a project just like the one described, but otherwise this story is both
fake and worthless. It doesn't help me to accurately evaluate myself or
my peers and keeps the true evaluation criteria in a secret, black box.

## Conclusion

Hiding levels isn't a great policy for software engineers. The supposed benefits to
employees and company culture aren't really benefits at all, and the downsides for IC career
advancement can be significant.