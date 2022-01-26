Cheat Sheet
===============

.. _skumar_site: https://skphy.github.io/aug20/

This sheet created by me for placing things at a single place. Also, this is the link to my home 
page at git site skumar_site_.

Sheet for Git and rst documentation
-----------------------------------

rst commands
------------

Heading
^^^^^^^

 `===========` , `------------`, `~~~~~~~`, '********', `^^^^^^^^^`

Inline markup
^^^^^^^^^^^^^
 **text**, *text*, ``text``

Bulleted list
^^^^^^^^^^^^^
    -- this is a bullet 1.
    * this is a bullet 2, too.

Numbered list
^^^^^^^^^^^^^
    #. number list 1
    1. number list 1, too.

Nested list
^^^^^^^^^^^
It  is also possible: just combine bullet list and indent the number list.

Hyperlink
^^^^^^^^^
 this is the hyperlink to my site: `skphy site <https://skphy.github.io/aug20/>`_.

Note
^^^^
 this is a example of adding a note is the rst file
.. note::
   how to use these notes for understanding.


Similary instead of Note use also Tip, Exercise, Important, Warning, Danger, and so on.


Git commands
------------

These command are taken from `fogelman git-site <https://gist.github.com/fogleman/>`_.


**Clone a repository (GitHub)**

```
git clone git@github.com:username/repository.git
```

**Checkout a branch into your working tree**

```
git checkout branchname
```

Dealing with the Working Tree
-----------------------------
**Delete untracked files in your working tree**

```
git clean -f      # Remove untracked files

git clean -f -d   # Also directories

git clean -f -x   # Also ignored files

git clean -f -X   # Just ignored files

```

**Restore to the HEAD of your current branch**

This is a good way to abort a merge in progress

```
git reset --hard HEAD
```

**Restore a file from an old revision**

```
git checkout [commit_id] -- path/to/oldfile
```

Branches
--------

**Delete a local branch**

```
git branch -d branchname
```

**Push a new branch for the first time**

```
git push -u origin branchname
```

Tags
----
**Create an annotated tag**

Annotated tags are more rich than regular tags, and include date/author information.

```
git tag -a [tagname] -m "Tag Message..."
```

**Checkout a tag**

```
git checkout [tagname]
```

The History, and Logs
---------------------
**View the commit history, showing the status of files that changed**

```
git log --stat
```
