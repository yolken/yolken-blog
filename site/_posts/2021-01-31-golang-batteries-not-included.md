---
layout: post
title:  "Golang: Some batteries not included"
date:   2021-01-31 17:55:00 -0700
tags: golang
related_posts:
  - slug: "cleaner-go-code-golines"
excerpt: |
    The go standard library is fairly rich. However, there are certain pieces of functionality
    that are either missing or insufficient and that, as a result, require the use of
    third-party libraries in nearly all of my projects. In this post, I want to go through the
    main "batteries not included" in the standard library, and the alternatives that I typically
    use for each one.
---

I use [golang](https://golang.org/) (aka "go") a lot for my day-to-day work. Like other programming
languages, it consists of a [*core language spec*](https://golang.org/ref/spec), describing,
for instance, how to declare variables, construct loops, etc., plus a
[*standard library*](https://golang.org/pkg/) that implements higher-level functionality
needed for software that actually does useful things.

The go standard library is fairly rich- in addition to basic input/output, it covers
HTTP client and server implementations, time and date processing, all of the standard cryptographic
algorithms (e.g., SHA256), data compression and decompression, and lots of other goodies.
However, there are certain pieces of functionality that are either missing or insufficient and
that, as a result, require the use of third-party libraries in nearly all of my projects.

In this post, I want to go through the main "batteries not included" in the standard
library, and the alternatives that I typically use for each one. Note that I'm *not* covering
missing language features like generics since those have been discussed extensively in
[other forums](https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=golang%20generics&sort=byPopularity&type=story).

### Aside: What do batteries have to do with programming languages?

The term "batteries not included" was historically stamped on the boxes of electronic toys and other
consumer goods to indicate that the batteries needed for the item to work were not provided in the
box. When I was growing up, I remember getting gifts where the giver forgot to buy the batteries.
I would then feverishly run around the house looking for instances of the right kind (either AA,
AAA, C, D, or 9-volt) and raid my other toys or our TV remote controls as needed.

The phrase is less common today because items often include batteries in the box or they use
built-in, rechargeable ones.

In any case, at some point the [Python programming language](https://www.python.org/) adopted the
term "batteries included" to describe its standard library. This was a cheeky way of saying that
unlike those cheap toys from childhood, you didn't need to build or bring extra items (i.e.,
libraries or tools) to make the language useful- it just worked "out of the box".

Nowadays, the idea of including a rich, fully functional standard library with a programming
language is pretty common. When Python was initially released in the early 1990's, however, this
was considered quite revolutionary- the main languages at the time (e.g., C) did not have very
big standard libraries; if you wanted to do anything beyond the basics, you had to write it
yourself or import a third-party implementation.

The "batteries included" philosophy for standard libraries has become common because it has
a lot of benefits:

1. It's easier to get started in the language- no need to find, evaluate, and import third-party
  libraries for common use cases
2. It's easier to distribute your code- people can just compile and/or run it with standard tooling
3. Code is more standardized- if everyone uses the standard library for something (e.g., making
  HTTP requests), then you're unlikely to see lots of different implementations for it
4. Maintenance is less of a burden- standard libraries tend to be well-maintained and regularly
  patched for security issues. You don't have to worry about the maintainer(s) disappearing and the
  library accumulating a large bug backlog.

Unfortunately, there isn't always agreement on which batteries to include and exactly how they
should work. Also, including too many things can lead to bloat, making the core language harder to
maintain and distribute. There are complex design and performance tradeoffs here, and as result
no language is 100% "batteries included" for 100% of use cases.

## The missing batteries

Now that we've reviewed what "batteries (not) included" means, let's go into what I consider
the main missing batteries in the go standard library.

### Flags

Many of the applications that I write in go are command-line tools that use flags for
specifying options, e.g. `mytool --option1=value1 --option2=value2`.

Golang includes a [`flag` package](https://golang.org/pkg/flag/) in its standard library for
defining and parsing these flags. However, it's pretty basic as it has no built-in support
for accepting "complex" types like lists or time durations. Also, for whatever reason, it uses
single dashes instead of double dashes for long flags- like most people (I think?), I find `--help`
more canonical than `-help` when interacting with a command-line tool.

As a result, the first thing I import when I'm creating a new command-line tool in go is a better
flag library. Unfortunately, there isn't a consistent standard on what to use here instead.
I originally used [kingpin](https://github.com/alecthomas/kingpin), but then switched
to [cobra](https://github.com/spf13/cobra) a few years ago because that seemed to be more common in
the code bases I was working on.

Recently, I discovered [segmentio/cli](https://github.com/segmentio/cli), which I like a lot
because it's so simple- you just tag a `struct`, and then you get the flag functionality for free:

```golang
func main() {
    type config struct {
        Age int          `flag:"--age"     help:"your age"     default:"55"`
        Hobbies []string `flag:"--hobby"   help:"your hobbies" default:"-"`
        Name string      `flag:"-n,--name" help:"your name"    default:"Joe"`
    }

    cli.Exec(
        cli.Command(
            func(config config) {
                fmt.Printf("Hello %s!\n", config.Name)
            },
        ),
    )
}
```

This works well for simple CLIs, but becomes a little messy for more complicated ones, e.g. when
the help text blurbs are really long or when you want to have multiple layers of subcommands.
Therefore, I still find myself reverting back to cobra sometimes.

### Logging

Log output, whether to the console or to an external log collection service, is really important
for understanding what's going on in an application. As with flags,
golang includes a [`log` package](https://golang.org/pkg/log/), but it's quite
basic and insufficient for many use cases. Among other problems, it doesn't support log levels
(e.g., `INFO` vs. `DEBUG`) or structured output formats like JSON.

As with flags, there isn't really a standard alternative here. I personally like
[logrus](https://github.com/sirupsen/logrus) a lot and include it in all of the tools I build.
Using it is as simple as importing the library and then calling `log.Infof`, `log.Debugf`, etc.
in place of the standard library's `log.Printf`:

```golang
import (
    log "github.com/sirupsen/logrus"
)

func myFunc(myArg string) {
    log.Debugf("Starting myFunc with myArg %s", myArg)
    ...
    if err != nil {
        log.Warnf("Got an unexpected error: %+v", err)
    }
    ...
}
```

In addition to supporting levels better than the standard `log` library, it also exposes
a lot of controls over the output format.

There are many other choices here, and some of these may be better than `logrus` depending on
your requirements. At Segment (my current employer), we use
[segmentio/events](https://github.com/segmentio/events) in
most of our backend systems. This library makes it easier to include structured key/value
pairs alongside the primary message for each log. The former aren't super useful for command-line
tools but can be very helpful when trying to filter gigabytes of logs produced by replicated, remote
systems.

### Test assertions

Go contains decent, built-in tooling for executing tests. However, it doesn't include any of the
"assert" functions that are common in the unit testing libraries of other languages.
This means that a simple test that two slices are equal looks like:

```golang
if !reflect.DeepEqual(expected, actual) {
    t.Error(
        "Wrong value for my special slice",
        "expected", expected,
        "got", actual,
    )
}
```

Thankfully, you can avoid this messiness by using
[stretchr/testify](https://github.com/stretchr/testify). With testify's `assert` package, the
above becomes much more concise:

```golang
assert.Equal(t, expected, actual, "My special slice")
```

There's also a `require` package that has the same interface as `assert`, but will stop the test
execution if the condition isn't met.

I use `testify` without exception in any project that is doing unit tests. It seems weird to me
that some people still prefer the canonical manual check followed by a `t.Error` message,
but to each their own!

### YAML parsing

Go includes a fully functional package for handling [JSON](https://en.wikipedia.org/wiki/JSON)-formatted
data but, like Python, doesn't have any equivalent for [YAML](https://en.wikipedia.org/wiki/YAML)
in its standard library. Many of the tools that I've worked on have some sort of human-created
config file, and it's much easier on users if these are YAML instead of JSON.

The standard here is [go-yaml](https://github.com/go-yaml/yaml), which has the same interface
as the standard `json` library but uses special `yaml` struct tags instead of `json`
ones. Personally, though, I prefer [ghodss/yaml](https://github.com/ghodss/yaml), which wraps the
former, because it supports `json`-compatible tags and thus makes everything more consistent.

### Static content embedding

> **Addendum:** Golang 1.16 finally added built-in [embedding support](https://golang.org/pkg/embed/).
> Yay!!! However, I'll keep this section here for historical reasons.

One of the nice things about golang is that your entire program can be compiled into a single,
self-contained binary. Among other benefits, this makes it easier to distribute your application
or run it in bare-bones environments (e.g., scratch docker containers).

Unfortunately, though, the standard go tooling only handles go code. It won't include separate
static assets like text templates and images in your binary. I commonly use the former,
in conjunction with go's excellent [text/template](https://golang.org/pkg/text/template/) package,
to generate HTML documents or YAML configs in my tools.

To get around this, there's a great tool called
[`go-bindata`](https://github.com/go-bindata/go-bindata) that will automatically read
these external assets and embed them into a `.go` file that can be included in your binary. It
then exposes an API for fetching the contents of each asset from your code.

The original creator of the tool, `jteeuwen`, stopped maintaining it and then completely
disappeared off Github a few years ago, which caused the proliferation of multiple,
not-fully-compatible forks. Thankfully, it seems like the community has
standardized on [this one](https://github.com/go-bindata/go-bindata), which hopefully will be
actively maintained going forward.

## Conclusion

Golang is great for many use cases, but you'll probably want to bring in third-party libraries
for some things like flags, logging, and testing. It would be great if these
were improved in the standard library, but I'm not holding my breath- from what I've heard,
the go maintainers are pretty adamant about what's in the standard library and what's not.
Thankfully, the third-party solutions are pretty good at filling in the gaps.