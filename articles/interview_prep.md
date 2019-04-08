# Interview Prep

Having switched jobs a few times over the last few years, I've done a *a lot* of software
engineering interviews. In my most recent job search, for instance, I did around eight phone screens
followed by six onsites.

The most stressful part of any interview for me, and most likely for other job candidates,
is the "technical coding" questions that inevitably get asked; most companies require you to solve
at least one during a phone screen, and then another two to three once you get onsite.

Over the last few job searches, I've developed a strategy that has significantly improved my
performance on these questions, to the point that I'm now rarely phased by them. In this post, I'd
like to share what I've learned.

## Practice, practice, practice

The key to doing an excellent job in a coding-oriented software interview is very simple- you
*must* practice beforehand. The interesting thing about practice is that it's both more effective
and more necessary than one would intuitively think. Let me explain why.

### Why it's more effective than you think

Software is such a broad field and there are so many technologies and applications that could come
up in an interview! Sure, practice can help, but how can it really make that much of a difference?

The reality, however, is that only a small subset of these are appropriate for an interview. In
particular, companies generally restrict their questions to those that:

1. Can be explained in under 5 minutes
2. Can be solved by a good candidate, starting from scratch, in under 30 minutes
3. Don't require specialized, domain-specific knowledge
  (e.g., around networking, databases, cryptography, graphical user interfaces (GUIs), etc.)
4. Don't require external data, documentation, hardware, or software libraries / code
5. Touch on intro-undergraduate-level algorithms and data structures including
  sorting, searching, dynamic programming, lists, hashmaps, etc.

These restrictions significantly reduce the surface area of possible questions. Even if you
get a question that isn't exactly like one you covered in your practice, chances are that it
has some similarities to one you have seen, and you can use those to your advantage.

### Why it's more necessary than you think

Another misconception is that if you're already doing a lot of hands-on software development
as part of your day-to-day job, this replaces the need for practice. That would make sense
if companies only asked practical questions, but the reality is that most don't. In fact,
the vast, vast majority of questions I've gotten over the years have little direct overlap with the
work I've done in the past or, most likely, the work that I would do if hired by the interviewer's
company.

The reason for this gets back to the criteria listed above; day-to-day projects rarely,
if ever, satisfy all of these. Most questions are completely synthetic and, thus, you need practice
beyond your day-to-day work to really get a handle on them.

## Enter Leetcode

Leetcode is a site designed for practicing interview-style coding questions. It has a large pool
of questions and an online code editor that allows you to write up and submit solutions to these.
Each submission is run against a set of question-specific test cases that verify both the
correctness and efficiency of the solution. If you get stuck, you can get help by looking through
official solution writeups (available for the most popular questions) or reading the messages on
each question's discussion board.

There are a bunch of other sites in the general "code interview prep" space. I've been
less satisfied with the ones that I've looked at, however, because their questions feel less
realistic to me; they're either not the right level of difficulty, or they're simply too long to do
in a 45 minute interview. These questions may be fun to work through, but if your goal is to prep
for interviews, solving them may not be the most efficient use of time.

Note that I have no official relationship with Leetcode. I just like them.

### Leetcode question difficulty

Leetcode classifies questions as either "easy", "medium", or "hard". I've found that
the sweet spot for actual interviews typically begins at the middle of the "medium" tier and runs
into the bottom (i.e., easier) chunk of "hard". "Easy" questions are fine to do as stepping stones
to the "medium" tier, but you're less likely to see these types of questions in an actual interview.

The hardest "hard" questions in Leetcode are annoying because they often require obscure
algorithmic tricks to solve efficiently. I don't worry about these questions too much because,
in the unlikely event that I were to get a question in this tier, the interviewer would (hopefully)
provide hints. They also don't generalize as well as the easier questions, so studying them is not
the most effective use of time.

### Language choice

Leetcode supports the languages that are most commonly used for interviews including C++, Java,
Javascript, Python, and Ruby. You should obviously practice in the one(s) that you intend to use.

I personally only interview in Python (for reasons to be explained in a future blog post), but
if you feel more comfortable in another language, you should go with that.

### General strategy

I like doing my interview prep in a short, intensive burst starting about 3 weeks before my
first interview. This ensures that the studying stays fresh in my mind and also minimizes the number
of weeks during which interview prep interferes with the other activities in my life.

When I'm ready to start, I pay for a one month premium subscription. It's a bit pricy (about $35 as
of early 2019), but I find it worth the money because it removes a bunch of restrictions in the
free product including access to locked questions and the ability to sort questions by frequency.

I then sort the questions in decreasing order of frequency and go through them roughly in order.
I say "roughly" because I like to initially focus on the easier questions, and then, as I get
more confidence, shift to the ones in the medium-to-hard range which, as discussed above, are
more typical in actual interviews. Also, some questions further down the list are just small
variations on previous questions, which I usually skip over.

My goal is to complete around 100 questions by the time of my first interview. I then continue
practicing while interviews are ongoing until my one month subscription is over.

### Missing question types

Leetcode has good coverage for most types of coding questions, but I've definitely noticed some
gaps over the course of my recent job hunts. In addition to practicing in Leetcode, you should also
be aware of questions that involve:

1. **"Design a class that does ...":** Leetcode has to provide an interface so that it can run test
  cases against your solution. In a real interview, the interface might not be provided and,
  moreover, designing it might be a big chunk of the question.
2. **Concurrency:** Leetcode doesn't provide much coverage for concurrency-related problems. You may
  want to brush up on concurrency primitives in your interview language, particularly if you don't
  use these as part of your day-to-day work.
3. **Network or file system operations:** Leetcode solutions run in a sandbox, and thus aren't
  going to be making HTTP requests or reading files from the file system. These types of questions
  aren't super common, but some companies do like them so you may want to brush up on how to do
  them in your chosen interview language.

## The "Hit Parade"

During my most recent rounds of interviewing, there were some types of questions that came up
over-and-over again. If you're on the market, you may want to spend a little extra time to make
sure you're comfortable with questions of these types.

### Searching and/or exploring in a 2D grid

See Leetcode 

### Evaluating arithmetic expressions

Some examples here include 

### Designing and implementing key/value stores or caches

See Leetcode 