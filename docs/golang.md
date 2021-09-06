# Golang

## Language features and implementation details

- [Working with Errors in Go 1.13](https://blog.golang.org/go1.13-errors): How to wrap errors, and best practices for wrapping (or not wrapping) errors.
- [Inside the Map Implementation](https://www.youtube.com/watch?v=Tl7mi9QmLns) :fontawesome-brands-youtube:: By Keith Randall at GopherCon 2016.

## Best practices

- [Gophers, please tag your releases (Dave Cheney)](http://dave.cheney.net/2016/06/24/gophers-please-tag-your-releases) - Tag your releases in preparation for better dependency tools coming in the future (_2016-06-24_)
- [Idiomatic Go tricks](https://www.youtube.com/watch?v=yeetIgNeIkc) :fontawesome-brands-youtube: - _[Mat Ryer](https://medium.com/@matryer/),  2016-09-09, [companion blog post](https://medium.com/@matryer/line-of-sight-in-code-186dd7cdea88)_

## Implementation articles

- [Error handling in Upspin](https://commandcenter.blogspot.com/2017/12/error-handling-in-upspin.html): An interesting article by the legendary [Rob Pike](https://research.google.com/pubs/r.html) about how to use custom error types to provide more meaningful messages in an app with many components.

## Videos

- [Testing and Benchmarking in Go Workshop](https://www.youtube.com/watch?v=ZeAkcs5g41k)  :fontawesome-brands-youtube: - _[Gopher Guides], 2017-11-30_

[gopher guides]: https://www.gopherguides.com/

## Important third party libraries

- [GORM](http://jinzhu.me/gorm/): A popular Go <abbr title="Object-relational mapping">ORM</abbr>. Very well written usage documentation.
- CLI (Command line libraries):
    - [urfave CLI](https://github.com/urfave/cli)  :fontawesome-brands-github:: Formerly `codegangsta/cli`. Man page like extensive help formatting.
    - [Cobra](https://github.com/spf13/cobra)  :fontawesome-brands-github:: Integrates with [Viper](https://github.com/spf13/viper)  :fontawesome-brands-github:, a config management library. Also uses [pflag](https://github.com/spf13/pflag) :fontawesome-brands-github:, a more posix compliant flag library than the standard library one.
