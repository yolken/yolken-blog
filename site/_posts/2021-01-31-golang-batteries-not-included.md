---
layout: post
title:  "Golang batteries not included"
date:   2021-01-31 17:55:00 -0700
categories: general tech
excerpt: |
    The golang standard library is fairly rich. However, there are certain pieces of functionality
    that are either missing or insufficient and that, as a result, require me to provide with
    third-party libraries in nearly all of my projects. In this post, I want to go through the
    main "batteries not included" in the standard library, and the alternatives that I typically
    use for each one.
---

I use [golang](https://golang.org/) a lot for my day-to-day work. Like many other programming
languages, it consists of a [*core language spec*](https://golang.org/ref/spec) (describing,
for instance, how to declare variables, construct a loop, etc.) plus a
[*standard library*](https://golang.org/pkg/) that extends the core by implementing
higher-level functionality that is often needed when writing software that actually does
useful things.

The golang standard library is fairly rich- in addition to basic input/output, it covers
HTTP client and server implementations, time and date processing, all of the standard cryptographic
algorithms (e.g., SHA256), data compression and decompression, and lots of other goodies.
However, there are certain pieces of functionality that are either missing or insufficient and
that, as a result, require the use of third-party libraries in nearly all of my projects.

In this post, I want to go through the main "batteries not included" in the standard library,
and the alternatives that I typically use for each one.

## Aside: What do batteries have to do with programming languages?



## The missing batteries

### Flags



### Logging



### Test assertions

Go contains decent, built-in tooling for executing tests. However,

### YAML



### Static content embedding



## Conclusion

Golang is great for many use cases, but