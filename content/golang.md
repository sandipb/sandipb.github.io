---
title: "Golang"
date: 2017-12-07T18:06:18-08:00
draft: false
---

# Best practices

- [Gophers, please tag your releases (Dave Cheney)](http://dave.cheney.net/2016/06/24/gophers-please-tag-your-releases) - Tag your releases in preparation for better dependency tools coming in the future (2016-06-24)
- [Idiomatic Go tricks](https://www.youtube.com/watch?v=yeetIgNeIkc) - By [Mat Ryer](https://medium.com/@matryer/), [companion blog post](https://medium.com/@matryer/line-of-sight-in-code-186dd7cdea88) (Youtube, 2016-09-09)

# Important third party libraries

- [GORM](http://jinzhu.me/gorm/): A popular Go <abbr title="Object-relational mapping">ORM</abbr>. Very well written usage documentation.
- CLI (Command line libraries):
    + [urfave CLI](https://github.com/urfave/cli): Formerly `codegangsta/cli`. Man page like extensive help formatting.
    + [Cobra](https://github.com/spf13/cobra): Integrates with [Viper](https://github.com/spf13/viper), a config management library

# Implementation articles

- [Error handling in Upspin](https://commandcenter.blogspot.com/2017/12/error-handling-in-upspin.html): An interesting article by the legendary [Rob Pike](https://research.google.com/pubs/r.html) about how to use custom error types to provide more meaningful messages in an app with many components.

# Videos

- [Testing and Benchmarking in Go Workshop](https://www.youtube.com/watch?v=ZeAkcs5g41k) (_[Gopher Guides]_,Youtube, 2017-11-30)


[gopher guides]: https://www.gopherguides.com/