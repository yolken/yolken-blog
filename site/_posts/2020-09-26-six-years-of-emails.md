---
layout: post
title:  "Six years of recruiting emails"
date:   2020-09-26 16:59:00 -0700
tags: recruiting
excerpt: |
    As a software engineer working in the San Francisco Bay Area, I get a lot of
    unsolicited recruiting emails. I recently decided to dig through my email archives
    and do some analysis of the long-term trends. Here are the results.
---

As a software engineer working in the San Francisco Bay Area, I get *a lot* of
unsolicited recruiting emails. I recently decided to dig through my email archives
and do some analysis of the long-term trends. Here are the results.

## Methodology

I get career-related messages sent to both my LinkedIn and Gmail accounts. Here's a typical
example (with the sender's name blacked out for privacy):

<div style="text-align:center">
<img width="600" src="/assets/typical_email.png" alt="typical email">
</div>

<br/>

The first step was to get all these messages out of my accounts and into a format
that I could use for the analysis.

For LinkedIn, this was easy- there's a "Get a copy of your data" section in the account
privacy settings. I selected "Messages", clicked the "Request Archive" button and then,
a few minutes later, downloaded a CSV that contained one row per message, with columns
for all of the important metadata: sender, recipient, subject, date, etc.

For Gmail, the process was a bit more involved. I had to go through Google's general
export product, [Takeout](https://takeout.google.com/), scroll down the Gmail section,
then select the labels to export. Thankfully, I've done a good job labelling
all of my career related emails, so I could just export those and not everything in my account.

A few minutes later, I got the option to download a bundle of all my emails in an
[mbox](https://en.wikipedia.org/wiki/Mbox) file. This is a legacy
format originally developed for text-based email clients in Unix; unfortunately, Google
doesn't give you the option to download your emails in an easier-to-use format like CSV.

The file had several million lines that looked like this:

```
From 1669160939957813740@xxx Thu Jun 11 00:38:38 +0000 2020
X-GM-THRID: 1669160939957813740
X-Gmail-Labels: Archived,Important,Opened,Category Updates,jobs
Delivered-To: XXXXX@gmail.com
Received: by 2002:a8a:40a:0:0:0:0:0 with SMTP id n10csp877323ocb;
        Wed, 10 Jun 2020 17:38:38 -0700 (PDT)
X-Received: by 2002:a17:902:ab87:: with SMTP id f7mr5405841plr.166.1591835918733;
        Wed, 10 Jun 2020 17:38:38 -0700 (PDT)
```

I then wrote a Python script to read this file, pull out the inbound messages, and convert
each one to a `<from,subject,date,body>` tuple. Thankfully, the Python standard library contains a
[mailbox](https://docs.python.org/3/library/mailbox.html) module that parses mbox files
and makes it easy to pull out the sender, recipient, subject, and date for each message.
Getting the bodies was a little trickier since mbox bodies can have multiple parts, each with
a different encoding (text, html, etc.), but I managed to find some
[examples on Stack Overflow](https://stackoverflow.com/questions/26567843/reading-the-mail-content-of-an-mbox-file-using-python-mailbox)
to copy.

I then merged the Gmail data with the LinkedIn data, exported everything to a CSV, and opened
this in Google Sheets. Finally, I spent an hour going through all the messages and deleting
the ones that weren't unsolicited. The result was a clean spreadsheet with one row per recruiting
email that I could use for my analysis.

## The results

The following shows the number of unsolicited recruiter emails I've received by month since the
beginning of 2014:

<iframe width="850" height="526" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4ZHxTwbmETB3mUTcILEkU77r_R8TVF3UcgW3Ems11ULMfJWuG8wwioWwx-myDnrEUhcbk1myxaAAr/pubchart?oid=1061438793&amp;format=interactive"></iframe>

A few interesting trends:

#### *Volume has increased a lot over the years*

Back in 2014, I was only getting a handful of messages per month. Now, I routinely get more
than one a day. The fact that I have more experience now than I did earlier in my career is
certainly a factor. But, I think the key driver here is simply that tech keeps getting bigger
and bigger, and the need for skilled engineers has increased significantly over time.

#### *There are clear seasonal patterns*

Email volume goes down significantly around the winter holidays. There's also a smaller drop
in the middle of the summer. Spring and fall are the busiest times, which also matches when
companies do the most interviewing.

#### *I get more emails when I'm actively engaged in a job search*

The peaks in 2015, 2017, and 2019 correspond to periods when I was actively on the job
market. During these times, I was much more active about updating my LinkedIn profile, which
is probably a strong signal that a candidate is looking for something new. It's also possible
that word spread through recruiters or friends, and that led to more job solicitations.

#### *There was no significant drop due to COVID*

Despite many companies laying people off or implementing hiring freezes earlier this year, I
still got a lot of recruiter emails. Now that startup valuations are back up and companies are
hiring again, I'm getting more emails than ever.

## Other trends

#### *Big companies can send lots of emails*

Facebook has by far been the peskiest of all the companies over the years, sending me more than
25 unsolicited recruiting emails since 2014. They've also sent a few text messages to my phone,
which is super-annoying. I should note, though, that I did interview there back in 2012, so I'm
probably in their system as a past prospect, which makes me a more likely sourcing target.

Amazon has also sent a lot of emails, particularly over the last two years.

Interestingly, I've only gotten one email from Apple, and nothing from other tech giants like
Microsoft, Netflix, IBM, SAP, and Cisco.

#### *Follow-ups*

A very common pattern is to send a message, then send a few follow-ups over the next
few days with slightly different bodies and subject lines. See the Opendoor example
at the beginning of this post for an example.

I guess that's one way to make sure that an email isn't missed, although it can get a little
tiresome if you're not interested in the company at all.

#### *Cute (and not-so-cute) subject lines*

Recruiters and sourcers try to be clever with subject lines and message introductions to
catch your attention and make the messages seem more personal.

Binary is one way to get attention, but I have no idea what it says since I'm not a
computer :-):

<div style="text-align:center">
<img width="400" src="/assets/message2.png" alt="typical email2">
</div>

<br/>

Another trick is to put your current and past employers in the subject so that
it looks more personalized, and then reference them in the body.
Not sure how effective it is, though:

<div style="text-align:center">
<img width="400" src="/assets/message3.png" alt="typical email3">
</div>

<br/>

Emoji are cute. Here's a message that had one in the subject
and then used them liberally in the body:

<div style="text-align:center">
<img width="400" src="/assets/message4.png" alt="typical email4">
</div>

<br/>

## Final thoughts

I've gotten a lot of recruiting emails over the years, and, assuming that current trends
continue, will get a lot more in the future. Despite these messages being unsolicited, I don't
consider them "spam" and actually like reading them. The vast majority are polite, informative,
and well-written. Even if I'm not actively looking for a new job, it's nice to learn about what's
out there so I know where to apply the next time I'm on the market.
