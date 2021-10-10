---
layout: post
title:  "How I made this blog"
date:   2021-01-10 14:10:00 -0700
tags: general-tech
excerpt: |
    Every now and then, I get asked how I made this blog from a technical standpoint. In this
    post, I want to share how my content is generated and hosted, and then describe some
    commonly-used, alternative approaches that I decided not to take.
---

Every now and then, I get asked how I made this blog from a technical standpoint. In this
post, I want to share how my content is generated and hosted, and then describe some commonly-used,
alternative approaches that I decided not to take.

## How it works

I write each post in a separate [Markdown](https://en.wikipedia.org/wiki/Markdown) file.
Markdown is nice because it's super lightweight, supports most of the formatting I need
(headers, bolding, bullets, etc.), and I've used it a lot for writing documentation at work, so
I feel very comfortable with the syntax.

For example, here's a sample of the Markdown for my recent post on
[quitting a new job](/blog/quitting-a-new-job):

{% highlight markdown %}
---
layout: post
title:  "Quitting a new job"
date:   2021-01-01 18:40:00 -0700
tags: career
excerpt: |
    Two years ago, I did something ...
---

Two years ago, I did something that I'd never done in my career before-
I left a job (at [Nuro](https://nuro.ai)) only a few months after starting
it. In this post, I want to explain what happened and what I learned from
the experience.

## What happened

#### The job switch

Back in the spring of 2019, I decided to leave [Stripe](https://www.stripe.com),
where I'd been a software engineer for about a year and a half. The full
details are best left to a separate post, but at a high level I just wasn’t very
happy...
{% endhighlight %}

I then use [Jekyll](https://jekyllrb.com/) to convert these Markdown files into a collection
of static HTML pages that can be rendered by web browsers. Jekyll is what's known as a
"static site generator"; in addition to supporting higher-level formats like Markdown that are
easier to work with than HTML, these frameworks also automate setting the look-and-feel of each
page and inserting common content like headers and footers that would be tedious to add manually.

Here's what the [quitting a new job](/blog/quitting-a-new-job) Markdown looks like after
conversion to HTML:

{% highlight html %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Quitting a new job | Benjamin Yolken</title>
    ...
  </head>
  <body>
    <header class="site-header">
      <div class="trigger">
        <a class="page-link" href="/blog">Blog</a>
        <a class="page-link" href="/pubs">Publications</a>
        <a class="page-link" href="/about">About</a>
      </div>
    </header>
    ...
    <div class="post-content e-content" itemprop="articleBody">
    <p>Two years ago, I did something that I’d never done in my career before-
      I left a job (at <a href="https://nuro.ai">Nuro</a>) only a few months
      after starting it. In this post, I want to explain what happened and
      what I learned from the experience.
    </p>
    <h2 id="what-happened">What happened</h2>
    <h4 id="the-job-switch">The job switch</h4>
    <p>Back in the spring of 2019, I decided to leave
      <a href="https://www.stripe.com">Stripe</a>, where I’d been a software
      engineer for about a year and a half. The full details are best left to
      a separate post, but at a high level I just wasn’t very happy...
{% endhighlight %}

Finally, I push the generated HTML files, along with a stylesheet for the site, into the
`gh-pages` branch of my [GitHub repo](https://github.com/yolken/yolken-blog). GitHub has a nice
feature called [GitHub Pages](https://pages.github.com/) that will take the contents of an arbitrary
branch (`gh-pages` by default) and serve them as static content behind a web server. It also
supports custom domains, which allows for my pages to be available though `yolken.net` as opposed to
a shared domain like `github.com`.

GitHub has solid documentation on the entire process, including the content generation
steps, that you can read
[here](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll). Everything is free if your repo is open-source
and you abide by the [GitHub Pages guidelines](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/about-github-pages#guidelines-for-using-github-pages), all of which
are pretty reasonable for most personal blogs.

## Rejected alternatives

There are several other approaches to publishing a blog online that I decided not to go with.
These weren't ideal for me, but, depending on your specific requirements, may be reasonable
choices for your content.

### Use a third-party blogging service

The easiest way to get a blog online is to use a third-party, hosted blogging service.
Back in the day, [Blogger](https://www.blogger.com/) was all the rage.
Now, it seems like [Medium](https://medium.com) is the hot platform to use. There are tons of other
choices here, including social networks like Facebook and LinkedIn, which have started supporting
blog-like user content.

The main advantage of these services is that they're super easy-to-use. You just type up your
content in a pretty, web-based editor and click a button to publish. They also provide features like
comments, searching, and subscriptions on top of your content without much effort.

The downside of these services is that you're handing over your content to a third-party,
who's packaging it up with other people's content, applying their own look-and-feel, and, in many
cases, trying to monetize it. Even though you're the author, and even though you maintain
legal rights to your content in most cases, there's a tendency for your work to become associated
more with the hosting service than with you.

Personally, I'm fine with this when I'm sharing low-quality, short-form content like
my vacation photos. However, for something as important and personal as my blog, I wanted
to be in complete control and not share any ownership with a third-party.

If you're just writing occasionally, though, or really, really don't want to deal with any
technical details, putting your content in a third-party service might be an acceptable
choice.

### Host in a cloud provider

GitHub Pages is very reliable and low-hassle but only handles static content and imposes
[some limitations](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/about-github-pages#guidelines-for-using-github-pages) on this content including its size and
update frequency. It also abstracts away the lower-level serving details, which are
sometimes useful to observe and adjust.

An alternative is to host your blog using a cloud provider like AWS. The details
here vary a lot based on which provider you're using and what you're trying to do, but if
you have static content only, you can use a storage service like
[S3](https://aws.amazon.com/s3/) plus a content delivery network (CDN) like
[CloudFront](https://aws.amazon.com/cloudfront/) to handle caching and HTTPS termination closer
to end users.

I decided to not take this approach because my blog comfortably fits within the limits of
GitHub Pages, and I also like that it's totally free. This may change in the future, though, if I
outgrow GitHub Pages or get bored and want to handle more of the lower-level serving details
myself.

### Run your own content management system (CMS)

Static sites like the one for this blog are fairly limited; among other examples, you can't
customize pages on a per-user basis, it's hard to provide dynamic features like search,
and, since all posts are static files, it can become tedious to manage a large amount of content.

An alternative is to run a service called a
[content management system (CMS)](https://en.wikipedia.org/wiki/Content_management_system), which
stores the content in a database and dynamically generates pages in response to user requests.
Because the content is stored in a structured format and because the server can customize the
contents of each page, it's much easier to incorporate Blogger or Medium-like features such as user
logins, search, and online post editing.

There are a large number of fully-featured, open-source CMSes to choose from, including
[WordPress](https://en.wikipedia.org/wiki/WordPress) and
[Drupal](https://en.wikipedia.org/wiki/Drupal). You can also write your own on top of a web
application framework like [Django](https://www.djangoproject.com/).

Running these systems is a lot more complicated than throwing static HTML into
GitHub Pages or S3. In addition to choosing a hosting provider and configuring all of the
associated software, you also need to worry about things like monitoring (what if the site goes
down?) and capacity planning (what if a post goes viral and gets tens of thousands of views?).

For me, the extra features of a CMS just weren't worth the hassle. However, this may be a good
choice if you want to create a site with more than just a static list of posts. The more popular
CMSes like WordPress also have rich ecosystems of themes and plugins that you can use
to create prettier, more complex online destinations.

## Conclusion

This blog consists of static HTML served by GitHub Pages. Although it's not the fanciest
approach, I've found that it provides a high degree of personal control while having
minimal maintenance overhead.
