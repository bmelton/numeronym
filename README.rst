Numeronym
=========

Numeronym is a simple Python library for creating numeronyms
like i18n, p13n, a16z, etc.  

It's like, 2 lines of code, so I don't know why you'd need it, 
but I was using it enough that I figured I'd make it a 
module that I could reuse. 

INSTALLATION
============

    >>> pip install numeronym

USAGE
=====

    >>> from numeronym import numeronym
    >>> numeronym("Andreesen Horowitz")
    >>> 'a16z'

NOTE
====

This module currently only bothers with the i18n type of
numeronym, though technically, "k9" is one as well.  I 
don't know how I'd calculate "k9" (from canine), so to hell
with that.  

LICENSE
=======

BSD.  Do whatever you want to with it. 
