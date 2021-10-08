# Git

## Common procedures

### Remove git submodules

- [Remove a Submodule within git](https://davidwalsh.name/git-remove-submodule): Adding a submodule is easy, removing is such a pain

[hugo]: https://gohugo.io/

### Revert a commit in the past

tldr;

- `git revert COMMIT`
- or, for a range of changes: `git revert COMMIT_R0..COMMIT_Rn`.

External resources:

- Tutorial: [How to reset, revert, and return to previous states in Git](https://opensource.com/article/18/6/git-reset-revert-rebase-commands)
- Ref: [`git-revert`](https://git-scm.com/docs/git-revert)

## References

- [Using Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules): No matter how less I want to use Git modules, I seem to need them all the time. Most of the time, whenever I use a program like [Hugo] which has external extensions, I end up needing submodules.
