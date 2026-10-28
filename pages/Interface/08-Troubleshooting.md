<!-- 来源: https://ck3.paradoxwikis.com/Interface oldid=35928 抓取于 2026-10-22T21:43:25+08:00 -->

# Interface — Troubleshooting


### Known crash reasons

- setting 100% size on hboxes and vboxes
- using an hbox or vbox inside a flowcontainer
- setting `resizeparent = yes` on multiple children in the same parent

even if only one of them is visible, this will still crash

- a type that references itself, this will lead to an endless loading screen until you run out of RAM
- syntax errors, like missing brackets or quotation marks

search for `{` in your file and then for `}` and compare the amounts, they should be the same

double-check that your types are set up correctly, since their syntax is different from other elements

for missing quotes, enable regex search in your editor and search for `= \[` and `\]\n`. You normally shouldn't have square brackets without quotation marks around them.

