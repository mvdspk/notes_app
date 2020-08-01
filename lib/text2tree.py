"""
PROBLEM STATEMENT:

if a text is given, convert to tree

example:
------
title
    sub title  1
        multi line description
        .that extends 
        .more than one line
        .and all lines start with a dot but considered a single line

        another single line

        sdkjsandkjsandsad
            dkfbdkkjd
                sknfkjdsnfkjsndf
                    snsndfsdfsd
                    sdjfnsdfn
                    sdfjndksfnkdsjf
                jkjjk
    kjjkjjsdfds323232

in the above text 
the first line that appears with 0 indent is the root
subsequnet lines are considered the children
their indent is their depth
"""