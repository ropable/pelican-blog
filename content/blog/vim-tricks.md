Title: vim tricks
Date: 2020-04-17 13:26
Slug: vim-tricks
Author: Ashley Felton
Summary: Vim tricks

A summary of tricks that I learn about using the Vim editor, written down so
that I (possibly) remember them better.

Delete from cursor to end of line:

~~~bash
d$
~~~

Close and open a single fold:

~~~bash
zc
zo
~~~

Delete multi-line comment via Visual block mode: `ctrl v`, highlight block, `x`

Insert multi-line comment: `ctrl v`, highlight block, `shift i`, `#`, `Esc`
(wait a second).

Reference: <https://stackoverflow.com/a/1676690/14508>
