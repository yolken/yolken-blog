# Interview Prep

Having switched jobs a few times over the last few years, I've done a *a lot* of software
engineering interviews. In my most recent job search, for instance, I did around eight phone screens
followed by six on-sites.

The most stressful part of any interview for me, and for many others as well,
is the "technical coding" questions that inevitably get asked; most companies require you to solve
at least one during a phone screen, and then another two to four once you get onsite.

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

[Leetcode](https://leetcode.com/) is a site designed for practicing interview-style coding
questions. It has a large pool of questions and an online code editor that allows you to write up
and submit solutions to them.

Each submission is run against a set of question-specific test cases that verify both the
correctness and efficiency of the solution. If you get stuck, you can get help by looking through
official solution write-ups (available for the most popular questions) or reading the messages on
each question's discussion board.

There are a bunch of other sites in the general, "code interview prep" space. I've been
less satisfied with the ones that I've looked at, however, because their questions feel less
realistic to me; they're often not the right level of difficulty, or they're simply too long to do
in a 45 minute interview. These questions may be fun to work through, but if your goal is to prep
for interviews, solving them may not be the most efficient use of time.

Note that I have no official relationship with Leetcode. I just like the site and want to tell
others about it. :-)

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

I would highly recommend choosing a single, high-level language for all of your interviews. I
personally always use Python; Ruby is also a reasonable choice. C++, on the other hand, is probably
not a great choice unless you happen to be a virtuoso in the language.

There are numerous advantages to choosing a high-level language like Python:

1. Compact, less verbose code: Assuming a fixed typing or white boarding speed, this means that you
  can construct solutions faster.
2. No IDE required: Many interviews are still done on whiteboards or in bare-bones
  text editors, so you can't always depend on having an IDE to help out.
3. Rich standard libraries: Python, for instance for instance, provides binary search (in `bisect`),
  permutations (in `itertools`), and heaps (in `heapq`), among other things that are helpful in
  interviews.


### Working through the questions

When I'm ready to start, I pay for a premium Leetcode subscription. It's a bit pricey (about $35 /
month as of early 2019), but I find it worth the money because it removes various restrictions
in the free product including access to locked questions and the ability to sort questions by
frequency.

I then sort the questions in decreasing order of frequency and go through them roughly in order.
I say "roughly" because I like to initially focus on the easier questions, and then, as I get
more confidence, shift to the ones in the medium-to-hard range which, as discussed above, are
more typical in actual interviews. Also, some questions are just slight variations of ones
above them in the list, so I'll skip over these if I already feel comfortable with them.

Once I've decided to do a question, I'll work on it independently for about 20 minutes. If I
can't get a reasonable solution within that time, I'll peek at the official solution for a few
hints and then get back to work; this is similar to how it would work in an actual interview, with
the difference being that in the real thing a person (i.e., your interviewer) would be offering
these up.

I stop working on the question when either I get all the test cases to pass or I hit the 45 minute
mark. Whether I've gotten a working answer or not, I read through the solution to make sure
that I have a correct understanding of the problem and the possible approaches to it. If I didn't
get a fully working solution within 45 minutes, I'll go back and implement one of the
approaches in the solution write-up, making sure I fully understand what I'm writing down.

### How much studying is enough?

I usually feel ready to do real interviews after I've solved around 100 questions. Doing more
than this has diminishing returns for me because the questions begin to look alike and thus they
don't really improve my preparation. 

### Leetcode gaps

Leetcode has good coverage for most types of coding questions, but I have noticed some
gaps over the course of my recent job hunts. In particular, you may want to do some non-Leetcode
preparation for coding questions that relate to:

1. **Interface design:** Leetcode has to provide an interface so that it can run test
  cases against your solution. In a real interview, the interface might not be provided and,
  moreover, designing it might be a big part of the question.
2. **Concurrency:** Leetcode doesn't provide much coverage for concurrency-related problems. You may
  want to brush up on concurrency primitives in your interview language, particularly if you don't
  use these as part of your day-to-day work.
3. **Network or file system operations:** Leetcode solutions run in a sandbox, and thus aren't
  going to be making HTTP requests or reading files from the file system. These types of questions
  aren't super common, but some companies do like them so you may want to brush up on how to do
  them in your chosen interview language.

## Common question types

During my most recent rounds of interviewing, there were some types of questions that came up
again and again. If you're on the market, you may want to spend a little extra time to make
sure you're comfortable with questions of these types.

### Searching and/or exploring in a 2D grid

Interviewers love these questions because they hit on multiple 

### Evaluating arithmetic expressions

These questions are easy to explain and test, but can be challenging to implement. 

### Designing and implementing key/value stores or caches

These kinds of questions are popular because they 

## Concluding thoughts



## Acknowledgements

I'd like to thank [John Mishanski](https://www.linkedin.com/in/johnmishanski/) for providing
feedback on a draft of this post.