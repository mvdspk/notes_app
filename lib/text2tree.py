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

"""
ALGO

fileContent <-- read the file as string
linesList <-- split lines on line ending
linesList <-- filter blank lines

textTree <-- create a tree object
textTree.root <-- linesLis[0] assign first element as root
treePathStack to ctrack the path while building a tree

for each children
of the root buildTree(), buy using the stack to mimic the path traversed
    buildTree() takes a line
        counts the starting white spaces and considers it as depth of the line
        uses stack length as the tree depth
        takes the difference treedepth and node depth
        if diff is 0 we are adding sibling
            so pop existing sibling, pop again to get parent
            add this node to parent as a child
            push parent
            push this node
        if diff is negative
            that means this node belongs to higher level
            so keep popping untl the differenrece is 0, i.e. reached same level
            again pop to get parent, 
            add this node to parent as a child
            push parent
            push this node
        if diff is positive by one unit
            we are adding a child
            pop parent
            add this node to parent as child
            push parent
            push child
by the end of iteration, e would have reached last line and built the last leaf of the tree




"""