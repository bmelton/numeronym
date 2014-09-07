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

    >>> from numeronym import Numeronym
    >>> output = Numeronym()
    >>> result = output.encode("Andreesen Horowitz")
    >>> 'a16z'

The Numeronym class has two Boolean options.  'short' and 
'lower'.

Pass in short=True to allow short inputs (like "hi").  Default
is False, as creating a numeronym for something like "hi" is 
kind of silly, but if you want it to do that, or don't want to 
have to deal with catching the exception for short values, then
feel free to enable it. 

Example

    >>> from numeronym import Numeronym

    >>> output = Numeronym(short=True)
    >>> result = output.encode("Hi")
    
    >>> Traceback (most recent call last):
    >>>  File "<stdin>", line 1, in <module>
    >>>  File "numeronym/main.py", line 29, in encode
    >>>    raise Exception("Input string must be at least four characters in length")
    >>> Exception: Input string must be at least four characters in length

    >>> output = Numeronym(short=True)
    >>> result = output.encode("Hi")
    >>> 'h1' 

The other option is lower, which will return output in lower 
case by default.  If you wish to preserve the case of the input, 
simply pass lower=False. 

Example

    >>> from numeronym import Numeronym
    >>> output = Numeronym(lower=False)
    >>> result = output.encode("Andreesen Horowitz")
    >>> 'A16z' # Note the upper case 'A' 

NOTE
====

This module currently only bothers with the i18n type of
numeronym, though technically, "k9" is one as well.  I 
don't know how I'd calculate "k9" (from canine), so to hell
with that.  

LICENSE
=======

BSD.  Do whatever you want to with it. 
