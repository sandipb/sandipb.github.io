# Golang

## Language features

- [Working with Errors in Go 1.13](https://blog.golang.org/go1.13-errors): How to wrap errors, and best practices for wrapping (or not wrapping) errors.

## Best practices

- [Gophers, please tag your releases (Dave Cheney)](http://dave.cheney.net/2016/06/24/gophers-please-tag-your-releases) - Tag your releases in preparation for better dependency tools coming in the future (_2016-06-24_)
- [Idiomatic Go tricks](https://www.youtube.com/watch?v=yeetIgNeIkc) <span class="fa fa-youtube fa-lg" aria-hidden="true"></span> - _[Mat Ryer](https://medium.com/@matryer/),  2016-09-09, [companion blog post](https://medium.com/@matryer/line-of-sight-in-code-186dd7cdea88)_

## Implementation articles

- [Error handling in Upspin](https://commandcenter.blogspot.com/2017/12/error-handling-in-upspin.html): An interesting article by the legendary [Rob Pike](https://research.google.com/pubs/r.html) about how to use custom error types to provide more meaningful messages in an app with many components.

## Videos

- [Testing and Benchmarking in Go Workshop](https://www.youtube.com/watch?v=ZeAkcs5g41k) <span class="fa fa-youtube fa-lg" aria-hidden="true"></span> - _[Gopher Guides], 2017-11-30_


[gopher guides]: https://www.gopherguides.com/

## Important third party libraries

- [GORM](http://jinzhu.me/gorm/): A popular Go <abbr title="Object-relational mapping">ORM</abbr>. Very well written usage documentation.
- CLI (Command line libraries):
    + [urfave CLI](https://github.com/urfave/cli) <span class="fa fa-github" aria-hidden="true"></span>: Formerly `codegangsta/cli`. Man page like extensive help formatting.
    + [Cobra](https://github.com/spf13/cobra) <span class="fa fa-github" aria-hidden="true"></span>: Integrates with [Viper](https://github.com/spf13/viper) <span class="fa fa-github " aria-hidden="true"></span>, a config management library. Also uses [pflag](https://github.com/spf13/pflag), a more posix compliant flag library than the standard library one.
