
1. Introduction to Python
=========================

The aim of this Chapter is to introduce you to some of the fundamental
concepts in Python. Mainly, this is based around fundamental data types
in Python (``int``, ``float``, ``str``, ``bool`` etc.) and ways to group
them (``tuple``, ``list`` and ``dict``).

We then learn about how to loop over groups of things, which gives us
control to iterate some process.

We need to spend a little time on strings, as you will likely to quite a
bit of string processing in Scientific Computing (e.g. reading/writing
data to/from ASCII text files).

Although some of the examples we use are very simple to explain a
concept, the more developed ones should be directly applicable to the
sort of programming you are likely to need to do.

A set of exercises is developed throughout the chapter, with worked
answers available to you once you have had a go yourself.

In addition, a more advanced section of the chapter is available, that
goes into some more detail and complkications. This too has a set of
exercises with worked examples.

1.1 Python
----------

`Python <http://www.python.org/>`__ is a high level programming language
that is freely available, relatively easy to learn and portable across
different computing systems. In Python, you can rapidly develop
solutions for the sorts of problems you might need to solve in your MSc
courses and in the world beyond. Code written in Python is also easy to
maintain, is (or should be) self-documented, and can easily be linked to
code written in other languages.

Relevant features include:

-  it is automatically compiled and executed
-  code is portable provided you have the appropriate Python modules.
-  for compute intensive tasks, you can easily make calls to methods
   written in (faster) lower-level languages such as C or FORTRAN
-  there is an active user and development community, which means that
   new capabilities appear over time and there are many existing
   extensions and enhancements easily available to you.

For further background on Python, look over the material on `Advanced
Scientific Programming in
Python <https://python.g-node.org/wiki/schedule>`__ and/or the
`software-carpentry.org <http://software-carpentry.org/v3/py01.html>`__
and `python.org <http://www.python.org/>`__ web sites.

In this session, you will be introduced to some of the basic concepts in
Python.

1.2 Running Python Programs
---------------------------

1.2.1 Requirements
~~~~~~~~~~~~~~~~~~

For this course, we suggest you use the
`anaconda <https://store.continuum.io/cshop/anaconda/>`__ Python
distribution (this is what is installed in the unix lab computers),
though you are free to use whichever version of it you like on your own
computers.

If you are intending to use these notes on your opwn computer, you will
need a relatively comprehensive installation of Python (such as that
from `anaconda <https://store.continuum.io/cshop/anaconda/>`__), and
will also need `GDAL <http://www.gdal.org/>`__ installed for some of the
work. You may also find it of value to have
`git <http://git-scm.com/>`__ installed.

We are assuming that you are new to computing in this course, but that
you are aware of the basic unix material covered in the previous
lecture.

2.2.2 Running Python
~~~~~~~~~~~~~~~~~~~~

We will generally use the ``ipython`` interpreter for running
interactive Python programs.

You will probably want to run each session and store scripts in your
``Data`` (or ``DATA``) directory.

If you want to run the session directly in the notebook, you will need
to download the course material from
`github <https://github.com/profLewis/geogg122>`__ and run the notebook
with e.g.:

::

    berlin% cd ~/DATA
    berlin% git clone https://github.com/profLewis/geogg122.git

to obtain the notes.

You should next check that you are using the version of Python that we
intend:

::

    berlin% which ipython
    /opt/anaconda/bin/ipython

If this isn't the version of Python that you are picking up (note the
use of the unix command ``which`` here), then you can either just type
the full path name:

::

    berlin% /opt/anaconda/bin/ipython  

in place of where it says ``ipython`` in these notes, or modify your
shell initialisation file (``~/.bashrc`` if you are using ``bash`` or
``~/.cshrc`` for ``tcsh`` or ``csh``) to include ``/opt/anaconda/bin``
early on in the ``PATH``.

To go to the directory for this session:

| ``berlin% cd ~/Data/geogg122/Chapter2_Python_intro``
| ``berlin% ipython notebook python101.html --pylab=inline``

You quit an ``ipython`` notebook session with ``^C`` (``Control C``).

To exectute ('run') blocks of Python code in the notebook, use
``^<return>`` (``SHIFT`` and ``RETURN`` keys together).

Alternatively, just run ``ipython``:

::

    berlin% cd ~/DATA/geogg122/Chapter2_Python_intro
    berlin% ipython --pylab=inline

and type your own commands in at the prompt, following the class or the
material on the webpages.

2.3 Getting Started
-------------------

2.3.1 Variables, Values and Data types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The idea of **variables** is fundamental to any programming. You can
think of this as the *name* of *something*, so it is a way of allowing
us to refer to some object in the language.

What the variable *is* set to is called its **value**.

So let's start with a variable we will call (*declare to be*) ``x``.

We will give the *value* ``1`` to this variable:

.. code:: python

    x = 1
In a computing language, the *sort of thing* the variable can be set to
is called its **data type**.

In the example above, the datatype is an **integer** number (e.g.
``1, 2, 3, 4``).

In 'natural language', we might read the example above as 'x is one'.

This is different to:

.. code:: python

    x = 'one'
because here we have set value of the variable ``x`` to a **string**
(i.e. some text).

A string is enclosed in quotes, e.g. ``"one"`` or ``'one'``, or even
``"'one'"`` or ``'"one"'``.

.. code:: python

    print "one"
    print 'one'
    print "'one'"
    print '"one"'

.. parsed-literal::

    one
    one
    'one'
    "one"


This is different to:

.. code:: python

    x = 1.0
because here we have set value of the variable ``x`` to a **floating
point** number (these are treated and stored differently to integers in
computing).

This is different to:

.. code:: python

    x = True
where ``True`` is a **logical** or **boolean** datatype (something is
``True`` or ``False``).

We have so far seen three datatypes:

-  integer (``int``): 32 bits long on most machines
-  (double-precision) floating point (``float``): (64 bits long)
-  Boolean (``bool``)
-  string (``str``)

but we will come across more (and even create our own!) as we go through
the course.

type
^^^^

In each of these cases above, we have used the variable ``x`` to contain
these different data types. If you want to know what the data type of a
variable is, you can use the method ``type()``

.. code:: python

    print type(1);
    print type(1.0);
    print type('one');
    print type(True);

.. parsed-literal::

    <type 'int'>
    <type 'float'>
    <type 'str'>
    <type 'bool'>


You can explicitly convert between data types, e.g.:

.. code:: python

    print 'int(1.1) = ',int(1.1)
    print 'float(1) = ',float(1)
    print 'str(1) = ',str(1)
    print 'bool(1) = ',bool(1)

.. parsed-literal::

    int(1.1) =  1
    float(1) =  1.0
    str(1) =  1
    bool(1) =  True


but only when it makes sense:

.. code:: python

    print "converting the string '1' to an integer makes sense:",int('1')

.. parsed-literal::

    converting the string '1' to an integer makes sense: 1


.. code:: python

    print "converting the string 'one' to an integer doesn't:",int('one')

::


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-9-20c6d9c1fc49> in <module>()
    ----> 1 print "converting the string 'one' to an integer doesn't:",int('one')
    

    ValueError: invalid literal for int() with base 10: 'one'


.. parsed-literal::

    converting the string 'one' to an integer doesn't:

When you get an error (such as above), you will need to learn to *read*
the error message to work out what you did wrong.

del
^^^

You can delete a variable with ``del``:

.. code:: python

    x = 100.
    print x

.. parsed-literal::

     100.0


.. code:: python

    x = 100.
    del x
    
    # so now if we try to do anything with the variable
    # x, it should fail as x is no longer defined
    print x

::


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-11-f602427acddb> in <module>()
          4 # so now if we try to do anything with the variable
          5 # x, it should fail as x is no longer defined
    ----> 6 print x
    

    NameError: name 'x' is not defined


2.3.2 Arithmetic
~~~~~~~~~~~~~~~~

Often we will want to do some
`arithmetic <http://www.tutorialspoint.com/python/python_basic_operators.htm>`__
with numbers in a program, and we use the 'normal' (derived from C)
operators for this.

Note the way this works for integers and floating point representations.

.. code:: python

    '''
        Some examples of arithmetic operations in Python
    
        Note how, if we mix float and int, the result is raised to float
        (as the more general form)
    '''
    
    print 10 + 100     # int addition
    print 10. - 100    # float subtraction
    print 1./2.        # float division
    print 1/2          # int division
    print 10.*20.      # float multiplication
    print 2 ** 3.      # float exponent
    print 8%2          # int remainder
    
    print '========'
    # demonstration of floor (//) and remainder (%)
    number    = 9.5
    base      = 2.0
    remainder = number%base # float remainder
    floor     = number//base # 'floor' operation
    print number,'is',floor,'times',base,'plus',remainder

.. parsed-literal::

    110
    -90.0
    0.5
    0
    200.0
    8.0
    0
    ========
    9.5 is 4.0 times 2.0 plus 1.5


Exercise
~~~~~~~~

Change the numbers in the examples above to make sure you understand
these basic operations.

Try combining operations and use brackets () to check that that works as
expected.

2.3.3 Assignment Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    '''
        Assignment operators
    
        x = 3   assigns the value 3 to the variable x
        x += 2  adds 2 onto the value of x
                so is the same as x = x + 2
                similarly /=, *=, -=
        x %= 2  is the same as x = x % 2
        x **= 2 is the same as x = x ** 2
        x //= 2 is the same as x = x // 2
    
        A 'magic' trick
        ===============
    
        http://www.wikihow.com/Read-Someone\
            %27s-Mind-With-Math-%28Math-Trick%29
    
        whatever you put as myNumber, the answer is 3
    
        Try this with integers or floating point numbers ...
    '''
    
    # pick a number 
    myNumber = 34.67
    
    # assign this to the variable x
    x = myNumber
    
    # multiply it by 2
    x *= 2
    
    # multiply this by 5
    x *= 5
    
    # divide by the original number
    x /= myNumber
    
    # subtract 7
    x -= 7
    
    # The answer will always be 3
    print x

.. parsed-literal::

    3.0


2.3.4 Logical Operators
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    '''
        Logical operators
    '''
    alive = True
    dead = not alive
    print 'dead or alive is',dead or alive
    print 'dead and alive is',dead and alive

.. parsed-literal::

    dead or alive is True
    dead and alive is False


The result of running comparison operators will give a logical (i.e.
``bool``) output.

Most of this should be obvious, but consider carefully how this works
for string data types.

2.3.5 Comparison Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    '''
        Related, comparison operators:
        
        ==  : equvalence
        !=  : not equivalent
        >   : greater than
        >=  : greater than or equal to
        <   : less than
        <=  : less than or equal to    
    '''
    
    print "is one plus one equal to two?"
    print 1 + 1 == 2
    
    print "is one less than or equal to 0.999?"
    print 1 <= 0.999
    
    print "is one plus one not equal to two?"
    print 1 + 1 != 2
    
    # note the use of double quotes inside a single quoted string here
    print 'is "Hello" not the same as "hello"?'
    print 'Hello' != 'hello'
    
    # note the use of single quotes inside a double quoted string here
    print "is 'more' greater than 'less'?"
    print "more" > "less"
    
    print "is '100' less than '2'?"
    print '100' < '2'
    
    print "is 100 less than 2?"
    print 100 < 2
    
    # a boolean example just to see what happens
    print "is True greater than False?"
    print True > False

.. parsed-literal::

    is one plus one equal to two?
    True
    is one less than or equal to 0.999?
    False
    is one plus one not equal to two?
    False
    is "Hello" not the same as "hello"?
    True
    is 'more' greater than 'less'?
    True
    is '100' less than '2'?
    True
    is 100 less than 2?
    False
    is True greater than False?
    True


We can combine such logical statements, bracketing the terms as
required:

.. code:: python

    print (1 < 2) and (True or False)

.. parsed-literal::

    True


.. code:: python

    #!/usr/bin/env python
    
    """Exercise in logical statements
      
       P. Lewis p.lewis@ucl.ac.uk
    
       Tue  8 Oct 2013 10:11:03 BST
    """
    
    # hunger threshold in hours
    hungerThreshold = 3.0
    # sleep threshold in hours
    sleepThreshold = 8.0
    
    # time since fed, in hours
    timeSinceFed = 4.0
    # time since sleep, in hours
    timeSinceSleep = 3.0
    
    # Note use of \ as line continuation here
    # It is poor style to have code lines > 79 characters
    #
    # see http://www.python.org/dev/peps/pep-0008/#maximum-line-length
    #
    print "Tired and hungry?",(timeSinceSleep >= sleepThreshold) and \
                                (timeSinceFed >= hungerThreshold)
    print "Just tired?",(timeSinceSleep >= sleepThreshold) and \
                                (not (timeSinceFed >= hungerThreshold))
    print "Just hungry?",(not (timeSinceSleep >= sleepThreshold)) and \
                                (timeSinceFed >= hungerThreshold)

.. parsed-literal::

    Tired and hungry? False
    Just tired? False
    Just hungry? True


Exercise 2.1
~~~~~~~~~~~~

The code above works fine, but the large blocks of logical tests are not
very clear or readable, and contain repeated items.

Type the code into a file (or `download it <files/python/hungry.py>`__).

To run the code *either* type at the unix prompt:

``berlin% python hungry.py``

OR, within ipython:

``In [17]: run hungry.py``

Modify this block of code to be clearer by assigning the individual
logical tests to variables,

e.g.

``tired = timeSinceSleep >= sleepThreshold``

2.4 Groups of things
--------------------

2.4.1 tuples, lists and dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Very often, we will want to group items together.

There are several main mechanisms for doing this in Python, known as:

-  tuple, e.g. (1, 2, 3)
-  list, e.g. [1, 2, 3]
-  dict, e.g. {1:'one', 2:'two', 3:'three'}

You will notice that each of these grouping structures uses a different
form of bracket.

tuple
^^^^^

A ``tuple`` is a group of items separated by commas.

.. code:: python

    t = 1, 2, 'three', False
    print t

.. parsed-literal::

    (1, 2, 'three', False)


Note that when you declare the tuple, you don't need to put the braces
(brackets) as this is implicit.

Often though, it is a good idea to do so.

.. code:: python

    t = (1, 2, 'three', False)
    print t

.. parsed-literal::

    (1, 2, 'three', False)


If there is only one element in a tuple, you must put a comma ``,`` at
the end, otherwise it is *not* interpreted as a tuple:

.. code:: python

    t = (1)
    print t,type(t)

.. parsed-literal::

    1 <type 'int'>


.. code:: python

    t = (1,)
    print t,type(t)

.. parsed-literal::

    (1,) <type 'tuple'>


You can have an *empty* tuple though:

.. code:: python

    t = ()
    print t,type(t)

.. parsed-literal::

    () <type 'tuple'>


Notice that the tuple can contain data of different types.

It can also be nested (i.e. a tuple can contain a tuple):

.. code:: python

    t = ('one', 2), 3, ((4,5),6)
    print t

.. parsed-literal::

    (('one', 2), 3, ((4, 5), 6))


Some operations we can perform on tuples include:

-  length : ``len()``
-  selection ('slice') : []

len
^^^

.. code:: python

    # set up a simple tuple
    t = (1,2,3)
    print "The length of the tuple (1,2,3) is",len(t)
    
    # a nested example
    t = (1,('2a','2b'),3)
    print "The length of the tuple (1,2,3) is",len(t)

.. parsed-literal::

    The length of the tuple (1,2,3) is 3
    The length of the tuple (1,2,3) is 3


slice
^^^^^

.. code:: python

    # select an item with []
    # note the first item is 0, i.e. we start counting at 0
    # Python uses a 0-based indexing system
    
    t = ('it','is','a','truth','universally','acknowledged')
    
    print 'item 0',t[0]
    print 'item 4',t[4]

.. parsed-literal::

    item 0 it
    item 4 universally


.. code:: python

    # using negative to count from the end
    # so -1 is the last item, -2 the second to last etc
    
    t = ('it','is','a','truth','universally','acknowledged')
    
    print 'item -1',t[-1]
    print 'item -3',t[-3]

.. parsed-literal::

    item -1 acknowledged
    item -3 truth


.. code:: python

    # select a range (a 'slice') of items with [start:end:step]
    
    t = ('it','is','a','truth','universally','acknowledged')
    
    print 'items 0:1\t',t[0:1]        # 0 to 1, so only item 0
    print 'items 0:2\t',t[0:2]        # 0 to 2, so items 0 and 1
    print 'items :4:2\t',t[:4:2]      # :4:2 so items 0 (implicit) to 4, in steps of 2
                                      # so items 0 and 3
    print 'items ::-1\t',t[::-1]      # 0 to end in steps of -1, so reverse order
    print 'items 1:-1:2\t',t[1:-1:2]  # 1 to -1 in steps of 2 so items 1 and 3
    
    # Note the use of \t in the strings above e.g. 'items 0:1\t'
    # where \t is a tab character (for prettier formatting)

.. parsed-literal::

    items 0:1	('it',)
    items 0:2	('it', 'is')
    items :4:2	('it', 'a')
    items ::-1	('acknowledged', 'universally', 'truth', 'a', 'is', 'it')
    items 1:-1:2	('is', 'truth')


In effect, when we set up a tuple, we are *packing* some group of items
together:

.. code:: python

    t = ('the', 'past', ('is', 'a', 'foreign', 'country'))
And we can similarly *unpack*:

.. code:: python

    a, b, c = t
    
    print 'a:',a
    print 'b:',b
    print 'c:',c

.. parsed-literal::

    a: the
    b: past
    c: ('is', 'a', 'foreign', 'country')


.. code:: python

    t = ('As', 'Gregor', 'Samsa', 'awoke', 'one', 'morning')
    
    a,b = t[1:4:2]
    print 'a:',a
    print 'b:',b

.. parsed-literal::

    a: Gregor
    b: awoke


The set of operations we can perform on tuples includes:

.. raw:: html

   <table>

::

    <tr><td><b>Name</b></td><td><b>Example</b></td><td><b>Result</b></td><td><b>Meaning</b></td></tr>
    <tr><td><pre>len()</pre></td><td><pre>len((1,2,(3,4))</pre></td><td><pre>3</pre></td><td>Length</td></tr>
    <tr><td><pre>+</pre></td><td><pre>(1,2) + (3,4,5)</pre></td><td><pre>(1,2,3,4,5)</pre></td><td>Concatenate (join)</td></tr>
    <tr><td><pre>\*</pre></td><td><pre>(1,2) * 3</pre></td><td><pre>(1, 2, 1, 2, 1, 2, 1, 2)</pre></td><td>Repetition</td></tr>
    <tr><td><pre>in</pre></td><td><pre>2 in (1,2,3,4)</pre></td><td><pre>True</pre></td><td>Membership</td></tr>
    <tr><td><pre>index</pre></td><td><pre>('a','b','c','d').index('c')</pre></td><td><pre>2</pre></td><td><p>Index</p><p>T.index(value, [start, [stop]]) -> integer -- return first index of value.</p><p>Raises ValueError if the value is not present</p></td></tr>    
    <tr><td><pre>count</pre></td><td><pre>('a','b','c','c','d','c').count('c')</pre></td><td><pre>3</pre></td><td><p>Count</p><p>T.count(value) -> integer -- return number of occurrences of value</p></td></tr>    
    <tr><td><pre>min(), max()</pre></td><td><p><pre>min(('a','b','c'))</pre></p><p><pre>max((3,4,1))</pre></p></td><td><p><pre>'a'</pre></p><p><pre>4</pre></p></td><td>Minimum, maximum</td></tr>
    <tr><td><pre>tuple()</pre></td><td><p><pre>tuple([1,2,3])</pre></p><p><pre>tuple('hello')</pre></p><p><pre>tuple({1:'one',2:'two'})</pre></p></td><td><p><pre>(1,2,3)</pre></p><p><pre>('h', 'e', 'l', 'l', 'o')</pre></p><p><pre>(1,2)</pre></p></td><td>Convert to tuple</td></tr>

.. raw:: html

   </table>

You will find that these basic operators work with any of the group
types, so you should make sure you are aware of them.

.. code:: python

    # some examples
    
    print "\ntuple('hello world'):\n\t",tuple('hello world')
    print "\ntuple('hello world').count('o'):\n\t",tuple('hello world').count('o')
    print "\n('1',)*5 + (1,)*5:\n\t",('1',)*5 + (1,)*5
    
    # Note use of \t in string for tab and \n for newline

.. parsed-literal::

    
    tuple('hello world'):
    	('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
    
    tuple('hello world').count('o'):
    	2
    
    ('1',)*5 + (1,)*5:
    	('1', '1', '1', '1', '1', 1, 1, 1, 1, 1)


You **cannot** directly replace an element in a tuple:

.. code:: python

    t = (1,2,3,4)
    t[2] = 'three'

::


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-32-0dc2fa4129fe> in <module>()
          1 t = (1,2,3,4)
    ----> 2 t[2] = 'three'
    

    TypeError: 'tuple' object does not support item assignment


so you would need to find another way to do this, e.g.

.. code:: python

    t = (1,2,3,4)
    
    t = t[:2] + ('three',) + t[3:]
    print t

.. parsed-literal::

    (1, 2, 'three', 4)


Neither can you delete an item in a tuple:

.. code:: python

    t = (1,2,3,4)
    
    del t[2]
    print t

::


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-34-b33678abdb80> in <module>()
          1 t = (1,2,3,4)
          2 
    ----> 3 del t[2]
          4 print t


    TypeError: 'tuple' object doesn't support item deletion


.. code:: python

    # again, find another way around
    
    t = (1,2,3,4)
    
    t = t[:2] + t[3:]
    print t

.. parsed-literal::

    (1, 2, 4)


string as a group
^^^^^^^^^^^^^^^^^

You might have noticed that a string data type ``str`` acts as a
collection of individual characters, e.g.:

.. code:: python

    word = 'hello world'
    
    print "word =\t",word,"\n"
    
    print "tuple(word) =\t",tuple(word)
    # slice
    print "word[2:5] =\t",word[2:5]
    # len
    print "len(word) =\t",len(word)
    # max (similarly min)
    print "max(word) =\t",max(word)
    # in (membership)
    print "'w' in word =\t",'w' in word
    # count
    print "word.count('l')=\t",word.count('l')
    # index
    print "word.index('l')=\t",word.index('l')
    # + (concatenation)
    print "word + ' again'=\t",word + ' again'
    # * (repetition)
    print "word * 2=\t",word*2

.. parsed-literal::

    word =	hello world 
    
    tuple(word) =	('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
    word[2:5] =	llo
    len(word) =	11
    max(word) =	w
    'w' in word =	True
    word.count('l')=	3
    word.index('l')=	2
    word + ' again'=	hello world again
    word * 2=	hello worldhello world


This sort of consistency or operation is one of the things that makes
Python a good language to program in.

list
^^^^

*lists* or *sequences* are contained within square brackets ``[]``:

The operators available for tuple work in much the same way as for lists
(more formally, sequences):

.. code:: python

    t = ['It', 'was', 'the', 'best', 'of', 'times']
    print t
    
    """slicing is the same as for tuples"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----slice----"
    print 't[:4:2]:\n\t',t[:4:2]       # 0th item to 4th in steps of 2, so 0,2
    print 't[::-1]:\n\t',t[::-1]       # reversal
    
    
    """index"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----index----"
    print 't.index("best"):\n\t',t.index('best')
    
    
    """plus"""
    t = ['It', 'was'] + ['the', 'best', 'of', 'times']
    
    print "\n----plus----"
    print "t = ['It', 'was'] + ['the', 'best', 'of', 'times']\n\t",t
    
    
    """multiply"""
    t = ['It', 'was', 'the'] + ['best'] * 3 + ['of', 'times']
    
    print "\n----multiply----"
    print "t = ['It', 'was', 'the'] + ['best'] * 3 + ['of', 'times']\n\t",t
    


.. parsed-literal::

    ['It', 'was', 'the', 'best', 'of', 'times']
    
    ----slice----
    t[:4:2]:
    	['It', 'the']
    t[::-1]:
    	['times', 'of', 'best', 'the', 'was', 'It']
    
    ----index----
    t.index("best"):
    	3
    
    ----plus----
    t = ['It', 'was'] + ['the', 'best', 'of', 'times']
    	['It', 'was', 'the', 'best', 'of', 'times']
    
    ----multiply----
    t = ['It', 'was', 'the'] + ['best'] * 3 + ['of', 'times']
    	['It', 'was', 'the', 'best', 'best', 'best', 'of', 'times']


But there are many other things one can do with a list, e.g.:

.. code:: python

    """replace"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----replace----"
    t[3:5] = ['New','York']
    print "t[3:5] = 'New York':\n\t",t
    
    
    """index and replace"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----index and replace----"
    t[t.index('best')] = 'worst'
    print 't[t.index("best")] = "worst":\n\t',t
    
    
    """can delete one or more items"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----del item----"
    del t[2:4]                         # delete items 2 to 4, i.e. 2, 3 
                                       # i.e. 'the', 'best'
    print 'del t[2:4]:\n\t',t
    
    
    """can sort"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----sort----"
    t.sort()                           # sort inplace
    
    print 't.sort():\n\t',t
    
    
    """can insert"""
    t = ['It', 'was', 'the', 'best', 'of', 'times']
    
    print "\n----insert----"
    t.insert(1,'really')               # insert inplace 
    
    print "t.insert(1,'really'):\n\t",t


.. parsed-literal::

    
    ----replace----
    t[3:5] = 'New York':
    	['It', 'was', 'the', 'New', 'York', 'times']
    
    ----index and replace----
    t[t.index("best")] = "worst":
    	['It', 'was', 'the', 'worst', 'of', 'times']
    
    ----del item----
    del t[2:4]:
    	['It', 'was', 'of', 'times']
    
    ----sort----
    t.sort():
    	['It', 'best', 'of', 'the', 'times', 'was']
    
    ----insert----
    t.insert(1,'really'):
    	['It', 'really', 'was', 'the', 'best', 'of', 'times']


range
^^^^^

Many functions that return multiple items will make use of a list to do
so.

An example of this that we will use below is
```range(start,stop,step)`` <http://docs.python.org/2/library/functions.html#range>`__
that returns a list of integers from ``start`` to (but not including)
``stop`` in steps of ``step``.

.. code:: python

    print range(10)

.. parsed-literal::

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


.. code:: python

    print range(1,3)

.. parsed-literal::

    [1, 2]


.. code:: python

    print range(-10,10,2)

.. parsed-literal::

    [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]


.. code:: python

    # set a value 3 to the variable x
    x = 3
    
    # range(10) produces the lis
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x in range(10)



.. parsed-literal::

    True



2.5 Loops and Conditional Statements: if, for, while
----------------------------------------------------

if
^^

So far, we have come across the ideas of variables, data types, and two
ways of grouping objects together (tuples and lists).

Another fundamental aspect of any programming language is conditional
statements. The simplest form of this is an ``if ... else ...``
statement:

.. code:: python

    pockets = ['phone','keys','wallet','frog'] 
    
    this_item = 'nothing'
    
    # test if something is in the list 
    if this_item in pockets:
        print "You do have",this_item,'in your pocket'
    else:
        print "You don't have",this_item,'in your pocket'

.. parsed-literal::

    You don't have nothing in your pocket


Here,

::

    this_item in pockets

is a membership test as we have seen above (it returns ``True`` or
``False``).

If it's ``True``, the code block

::

    print "You do have",this_item,'in your pocket'

is executed. If ``False``, then the next condition is checked.

Note the use of indentation here (using ``tab`` or spaces) to represent
the structure of the conditional statements.

Note also the use of a colon (``:``) to mark the end of the conditional
test.

.. code:: python

    '''An if example
    
       Threshold the value of x at zero
    '''
    
    x = 3
    
    # threshold at zero
    # and print some information about what we did
    
    if x < 0:
        print 'x less than 0'
        x = 0
    elif x == 0:
        print 'x is zero'
    else:
        print 'x is more than zero'
        
    print 'thresholded x = ',x

.. parsed-literal::

    x is more than zero
    thresholded x =  3


The syntax of this is:

.. code:: python

        if condition1 is True:
            ...
        elif condition2 is True:
            ...
        else:
            ...

where ``condition1`` and ``condition2`` are logical tests (e.g.
``this_item in pockets``, ``today == "Wednesday"``, ``x > 10`` etc.) and
the ``is True`` part of the syntax is implicit (i.e. you don't need to
type ``is True``).

The word ``elif`` means ``else if``. The tests are considered in the
order they are givem so that if ``condition1`` is ``not True``, we
examine ``condition2``. If that is ``not True``, we fall through to the
final ``else`` block.

.. code:: python

    # nested conditional statements: If
    
    what_you_keep = 'your head'
    when_you_do_it = 'all about you are losing theirs'
    whom_you_trust_when_all_men_doubt_you = 'yourself'
    
    # first tests
    if ( what_you_keep == 'your head' ) and \
        (when_you_do_it == 'all about you are losing theirs'):
    
        # second level tests
        if whom_you_trust_when_all_men_doubt_you == 'yourself':
            print "Yours is the Earth and everything that’s in it ..."
        else:
            print "Nearly there ..."
    
    else:
        print "Have a look at http://www.poetryfoundation.org/poem/175772"

.. parsed-literal::

    Yours is the Earth and everything that’s in it ...


Exercise 2.2
~~~~~~~~~~~~

A.
^^

A small piece of Python code that will set the variable ``today`` to be
a string with the day of the week today is:

.. code:: python

    # This imports a module that we can use to access dates
    from datetime import datetime
    
    # set up a list of days of the week, starting Monday
    # Note the line continuation here with \
    week = ['Monday','Tuesday','Wednesday','Thursday',\
            'Friday','Saturday','Sunday']
    
    # This part gives the day of the week
    # as an integer, 0 -> Monday, 1 -> Tuesday etc.
    day_number = datetime.now().weekday()
    
    today = week[day_number]
    
    # print item day_number in the list week
    print "today is",today

.. parsed-literal::

    today is Tuesday


Based on the example below, **set up a diary for youself for the week to
print out what you should be doing today, using the conditional
structure ``if .. elif ... else``.**

.. code:: python

    if day_number == 2:
        print "Remember to wake up early to get to the Python class at UCL"
    elif day_number == 4:
        print "Remember to wake up early to go to classes at Imperial College"
    else:
        print "get some sleep"

.. parsed-literal::

    get some sleep


B.
^^

You could set up the basic calendar for the week in a list, with the
first entry representing Monday, the second Tuesday etc.

.. code:: python

    my_diary = ['Spend the day practicing Python',\
                'Do some reading in the library at UCL', \
                'Remember to wake up early to get to the Python class at UCL',\
                'Spend the day practicing Python',\
                'Remember to wake up early to go to classes at Imperial College',\
                'Work at Python exercises from home',\
                'Work at Python exercises from home']
Using a list of this sort, **print the diary entry for today *without*
using conditional statements.**

Criticise the code you develop and make suggestions for improvement.

for
^^^

Very commonly, we need to iterate or 'loop' over some set of items.

The basic stucture for doing this (in Python, and many other languages)
is ``for ... in ...``:

.. code:: python

    count_list = range(1,4)
    
    # for loop
    for count in count_list:
        '''print counter in loop'''
        print count
        
    print 'blast off'

.. parsed-literal::

    1
    2
    3
    blast off


which has the syntax:

::

    for var in list:
        ...

where the variable ``var`` is set to each of the items in ``list``, in
the order in which they appear in ``list``.

xrange
^^^^^^

When we have a loop, there nust be something that defines what it is we
loop over. In the example above, this was a list, ``count_list``, which
here is ``[1, 2, 3]``.

In Python, we can use either use some explicit list, tuple etc. to
define what we loop over, or, we can use a `generator
expression <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#generator-expressions-1>`__,
which is something that returns one of its members at a time.

Normally then, instead or using ``range`` above, which involves an
*explicit* calculation and storage of all elements of the list, we use a
generator function,
```xrange`` <http://docs.python.org/2/library/functions.html#xrange>`__,
which, in essence, returns the elements 'on demand' as needed in the
loop (and so uses less memory, though there is little real difference
except for very large loops).

.. code:: python

    # for loop
    for count in xrange(1,4):
        '''print counter in loop'''
        print count
        
    print 'blast off'

.. parsed-literal::

    1
    2
    3
    blast off


If you need to force an
```iterable`` <http://docs.python.org/2/glossary.html#term-iterable>`__
to e.g. return a list, you can convert the data type to ``list``:

.. code:: python

    print xrange(1,4)

.. parsed-literal::

    xrange(1, 4)


.. code:: python

    print list(xrange(1,4))

.. parsed-literal::

    [1, 2, 3]


enumerate
^^^^^^^^^

Commonly, when iterating over a set of items, we also need access to a
counter, telling us which item in the list we are currently on.

This is done using the function
```enumerate()`` <http://docs.python.org/2/library/functions.html#enumerate>`__.
This returns the ``tuple`` ``(count,item)`` where ``count`` is the index
of ``item`` in ``list``.

.. code:: python

    word_list = ['Call', 'me', 'Ishmael']
    
    for i,w in enumerate(word_list):
        print 'The',i,'th','word is',w

.. parsed-literal::

    The 0 th word is Call
    The 1 th word is me
    The 2 th word is Ishmael


Here the syntax:

::

    for count,var in enumerate(list):
        ...

2.6 Strings and things
----------------------

We have seen the data type ``str`` above and noted some of the
operations we can use of strings.

You can look over some more `detailed
notes <http://docs.python.org/2/library/string.html_>`__ on strings at
some point, but here we will now go through some other typical
operations you will use in scientific computing:

2.6.1 Some basic string operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a recap, with some slightly more complicated examples:

.. code:: python

    word = 'hello world'
    
    print "word \n\t=",word,"\n"
    
    print "list(word) \n\t=",list(word)
    
    # slice
    print "word[::-1] \n\t=",word[::-1]
    # len
    print "len(word) \n\t=",len(word)
    # min (similarly max)
    print "min(word) \n\t=",min(word),'\n\t... what was printed there?'
    # in (membership)
    print "'n' in word \n\t=",'n' in word
    # count
    print "word.count('p')\n\t=",word.count('p')
    # + (concatenation)
    print "'hey!' + word[len('hello')::2]\n\t=",'hey!' + word[len('hello')::2]
    # * (repetition)
    print "word[:6]* 3\n\t=",word[:6]*3

.. parsed-literal::

    word 
    	= hello world 
    
    list(word) 
    	= ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    word[::-1] 
    	= dlrow olleh
    len(word) 
    	= 11
    min(word) 
    	=   
    	... what was printed there?
    'n' in word 
    	= False
    word.count('p')
    	= 0
    'hey!' + word[len('hello')::2]
    	= hey! ol
    word[:6]* 3
    	= hello hello hello 


.. code:: python

    # look what happens if we call index
    # for something that doesn't exist in the string
    print "word.index('x')=\t",word.index('x')


::


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-55-515f07310ca9> in <module>()
          1 # look what happens if we call index
          2 # for something that doesn't exist in the string
    ----> 3 print "word.index('x')=\t",word.index('x')
    

    ValueError: substring not found


.. parsed-literal::

    word.index('x')=	

.. code:: python

    # Sometimes, we might wish to use 
    # the string operator find instead
    print "word.find('x')=\t",word.find('x')


.. parsed-literal::

    word.find('x')=	-1


2.6.2 split
~~~~~~~~~~~

Suppose we have some data that are presented to us as a string with
white space separating each data element, e.g.:

.. code:: python

    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
These data are total fossil fuel emissions for Zimbabwe (thousand metric
tons of C) for selected years (dataset `doi
10.3334/CDIAC/00001\_V2011 <ftp://cdiac.ornl.gov/pub/trends/emissions/zim.dat>`__).

The even elements are the year (``1964``, ``1974`` etc.) and the odd
elements (``1220``, ``2470``) the data for that year.

We can use the string operator ``split()`` to separate this into a list
of strings:

.. code:: python

    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
    sdata = data.split()
    print sdata

.. parsed-literal::

    ['1964', '1220', '1974', '2470', '1984', '2706', '1994', '4812', '2004', '2707']


We could the convert these to integer:

.. code:: python

    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
    sdata = data.split()
    
    # how many items are there?
    # use len(), and divide by 2 in this case
    n_items = len(sdata)
    
    # create an empty list: years
    years = []
    
    # create an empty list: emissions
    emissions = []
    
    # loop over sdata in steps of 2
    # and append years and emissions
    # data as int
    
    # xrange(0,n_items,2) because
    # we want to step every 2 in this case
    for i in xrange(0,n_items,2):
        years.append(int(sdata[i]))
        emissions.append(int(sdata[i+1]))
    print years
    print emissions

.. parsed-literal::

    [1964, 1974, 1984, 1994, 2004]
    [1220, 2470, 2706, 4812, 2707]


2.6.3 join
~~~~~~~~~~

The 'opposite' of ``split`` is ``join``.

This returns an iterable of the form ``S.join(list)``, where ``S`` is
the separator and ``list`` is a **list of strings** e.g.:

.. code:: python

    str1 = 'hello'
    str2 = 'world'
    
    # joint with space
    print ' '.join([str1,str2])
    # joint with no space
    print ''.join([str1,str2])
    # join with tab
    print '\t'.join([str1,str1,str2])
    # join with colon :
    # note what happens we pass a 
    # string, rather than a list
    print ':'.join(str1)

.. parsed-literal::

    hello world
    helloworld
    hello	hello	world
    h:e:l:l:o


.. code:: python

    # remember that it has to be a list
    # of strings: years here is a list
    # of integers
    print ' '.join(years)

::


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-61-795783cbd46a> in <module>()
          2 # of strings: years here is a list
          3 # of integers
    ----> 4 print ' '.join(years)
    

    TypeError: sequence item 0: expected string, int found


.. code:: python

    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
    sdata = data.split()
    
    for i in xrange(0,len(sdata),2):
        print ' '.join(sdata[i:i+2])

.. parsed-literal::

    1964 1220
    1974 2470
    1984 2706
    1994 4812
    2004 2707


2.6.4 listcomp
~~~~~~~~~~~~~~

That is a perfectly fine way to pull these data out of a string, but
it's not very
`'Pythonic' <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`__
(it does'nt make best use of some of the elegant features of this
language).

Better in this sense is what are known as
`listcomps <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#list-comprehensions>`__
(list comprehensions).

With a listcomp, you define a list (enclosed in ``[``, ``]``), with two
or three terms. The first term is some function ``fn(item)``. The second
is a for statement. The third, if present, is a conditional (``if``)
statement.

For example:

.. code:: python

    fdata = [int(s) for s in data.split()]
    
    print fdata

.. parsed-literal::

    [1964, 1220, 1974, 2470, 1984, 2706, 1994, 4812, 2004, 2707]


This generates a list. Within this list, we iterate over the loop
``for s in data.split()``, and enter the result of the function
``int(s)``.

So this example is directly equivalent to:

.. code:: python

    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
    
    fdata = []
    for s in data.split():
        fdata.append(int(s))
            
    print fdata

.. parsed-literal::

    [1964, 1220, 1974, 2470, 1984, 2706, 1994, 4812, 2004, 2707]


You will very commonly use listcomps of this nature when performing some
function over elements in a list where you have to perform the function
on each element at a time.

.. code:: python

    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
    fdata = [int(s) for s in data.split()]
    
    # use slicing to separate the odd
    # and even data
    years     = fdata[0::2]
    emissions = fdata[1::2]
    
    print years
    print emissions

.. parsed-literal::

    [1964, 1974, 1984, 1994, 2004]
    [1220, 2470, 2706, 4812, 2707]


Listcomps can be very convenient, as they are a compact way of
specifying a loop (with a conditonal statement oif required).

Don't use listcomps if they obscure the meaning of what you are doing
though.

2.6.5 generator expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A listcomp generates everything in the list, then returns the list.

Sometimes, you only need one element at a time (e.g. within a loop). In
such cases, it is better to use generator expressions.

These look much like listcomps but use ``()`` rather than ``[]``

.. code:: python

    fdata = (int(s) for s in data.split())
    print fdata
    
    for i in fdata:
        print i

.. parsed-literal::

    <generator object <genexpr> at 0x106102e10>
    1964
    1220
    1974
    2470
    1984
    2706
    1994
    4812
    2004
    2707


but only return one item at a time, on demand in the loop.

2.6.6 replace
~~~~~~~~~~~~~

Another useful string operator is ``replace``, e.g.:

.. code:: python

    # change white space separation to comma separation
    data = "1964 1220 1974 2470 1984 2706 1994 4812 2004 2707"
    print data.replace(' ',',')

.. parsed-literal::

    1964,1220,1974,2470,1984,2706,1994,4812,2004,2707


2.6.7 format
~~~~~~~~~~~~

The most common way you are likely to be formatting strings is using
expressions such as:

.. code:: python

    how_many = 10
    how_much = "hours"
    
    print "There are only %d things to learn.\
            \nBut\tit will take you %s to do so."%(how_many,how_much)

.. parsed-literal::

    There are only 10 things to learn.        
    But	it will take you hours to do so.


Using this style of string formatting, you put control characters into
the string, e.g.:

::

    "%d: hello %s"

and put a tuple of variables after the string, separated by ``%`` which
are inserted into the string in the order in which they appear:

::

    "%d: hello %s"%(10,'ten')

Note that you must get the data types correct, or you will generate an
error.

The most common formatting codes are:

-  ``%d`` represents an integer
-  ``%s`` represents a string
-  ``%f`` represents a float
-  ``%e`` represents a float in exponential form

e.g.:

.. code:: python

    print "\
            integer     %d\n\
            float       %f\n\
            string      %s\n\
            exponential %e"%(3,3.1415926536,"pies are squared",3.1415926536)

.. parsed-literal::

            integer     3
            float       3.141593
            string      pies are squared
            exponential 3.141593e+00


2.6.8 strip
~~~~~~~~~~~

A useful method is ``strip()`` that strips off any unnecessary white
space and newlines e.g.:

.. code:: python

    string = '   hello world      \t'
    print '|%s|'%string
    print '|%s|'%string.strip()

.. parsed-literal::

    |   hello world      	|
    |hello world|


2.6.9 Getting and splitting filenames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

glob
^^^^

.. code:: python

    # example, with directory names
    
    # glob unix style pattern matching for files and directories
    import glob
    
    # returns a list (or [] if empty)
    # to match the pattern given
    file_list = glob.glob("files/data/*.txt")
    print "file_list:\n\t",file_list
    
    # e.g. the first string in the list
    this_file = file_list[0]

.. parsed-literal::

    file_list:
    	['files/data/HadSEEP_monthly_qc.txt', 'files/data/heathrowdata.txt', 'files/data/modis_files.txt', 'files/data/modis_files2a.txt', 'files/data/modis_files2b.txt', 'files/data/some_modis_files.txt']


.. code:: python

    this_file = 'files/data/HadSEEP_monthly_qc.txt'
    
    # split the filename on the field '/'
    print "\nthis_file.split('/'):\n\t",this_file.split('/')
    
    # so the filename is just the last element in this list
    print "\nthis_file.split('/')[-1]:\n\t",this_file.split('/')[-1]

.. parsed-literal::

    
    this_file.split('/'):
    	['files', 'data', 'HadSEEP_monthly_qc.txt']
    
    this_file.split('/')[-1]:
    	HadSEEP_monthly_qc.txt


.. code:: python

    # another example, with directory names
    
    # glob unix style pattern matching for files and directories
    import glob
    
    # returns a list
    file_list = glob.glob("files/data/*.txt")
    print "file_list:\n\t",file_list
    
    print "\nfile names:"
    # loop over the list of file namnes
    for this_file in file_list:
        # for each of these
        # split the filename on the field '/'
        print "\t",this_file.split('/')[-1]
        

.. parsed-literal::

    file_list:
    	['files/data/HadSEEP_monthly_qc.txt', 'files/data/heathrowdata.txt', 'files/data/modis_files.txt', 'files/data/modis_files2a.txt', 'files/data/modis_files2b.txt', 'files/data/some_modis_files.txt']
    
    file names:
    	HadSEEP_monthly_qc.txt
    	heathrowdata.txt
    	modis_files.txt
    	modis_files2a.txt
    	modis_files2b.txt
    	some_modis_files.txt


Exercise 2.3
------------

The data below are fields of:

| 0 year
| 1 month
| 2 tmax (degC)
| 3 tmin (degC)
| 4 air frost (days)
| 5 rain (mm)
| 6 sun (hours)

for Lowestoft in the UK for the year 2012, taken from `Met Office
data <http://www.metoffice.gov.uk/climate/uk/stationdata/lowestoftdata.txt>`__.

.. code:: python

    data = """   2012   1    8.7    3.1      5   33.1   53.9
       2012   2    7.1    1.6     13   13.8   86.6
       2012   3   11.3    3.7      2   64.2  141.3
       2012   4   10.9    4.3      3  108.9  151.1
       2012   5   15.1    8.6      0   46.6  171.3
       2012   6   17.9   10.9      0   74.4  189.0
       2012   7   20.3   12.8      0   93.6  206.9
       2012   8   22.0   14.0      0   59.6  217.3
       2012   9   18.9    9.5      0   38.8  200.8
       2012  10   13.6    7.9      0   92.7   94.7
       2012  11   10.5    4.4      2   62.1   79.6  
       2012  12    7.9    2.4      8   95.6   41.9  """
    
    print data

.. parsed-literal::

       2012   1    8.7    3.1      5   33.1   53.9
       2012   2    7.1    1.6     13   13.8   86.6
       2012   3   11.3    3.7      2   64.2  141.3
       2012   4   10.9    4.3      3  108.9  151.1
       2012   5   15.1    8.6      0   46.6  171.3
       2012   6   17.9   10.9      0   74.4  189.0
       2012   7   20.3   12.8      0   93.6  206.9
       2012   8   22.0   14.0      0   59.6  217.3
       2012   9   18.9    9.5      0   38.8  200.8
       2012  10   13.6    7.9      0   92.7   94.7
       2012  11   10.5    4.4      2   62.1   79.6  
       2012  12    7.9    2.4      8   95.6   41.9  


You can use the Python package ``pylab`` to simply plot data on a graph:

.. code:: python

    # import the pylab module
    import pylab as plt
    
    # some e.g. x and y data
    x = range(100)
    y = [i**0.5 for i in x]
    
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of sqrt(x)') 



.. parsed-literal::

    <matplotlib.text.Text at 0x1061717d0>




.. image:: python101_files/python101_185_1.png


**Produce a plot of the number of sunshine hours for Lowestoft for the
year 2012** using the data given above.

Hint: the data have newline chcracters ``\n`` at the end of each line of
data, and are separated by white space within each line.

2.7 Files
---------

To open a file that already exists for *reading*, we use:

.. code:: python

        fp = open(filename,'r')

where ``filename`` here is the name of a file and the ``'r'`` argument
tells us that we want to open in 'read' mode.

This returns a file object, ``fp`` here that we can use to read data
from the file etc.

When we have finished doing what we want to do, we should close the
file:

.. code:: python

        fp.close()

To read ASCII data from a file as a list of strings for each line, use:

.. code:: python

        fp.readlines()

To write ASCII text to the file, use:

.. code:: python

        fp.write("some text")

or to write a list of strings all at once:

.. code:: python

        fp.writelines(["some text\n","some more\n"])

As a first example, let's open a file for *reading* from a file
```files/data/elevation.dat`` <files/data/elevation.dat>`__ that
contains a list of dates, times and solar elevation angles (degrees).

.. code:: python

    !head -10 < files/data/elevation.dat 

.. parsed-literal::

    2013/10/8 00:00:00 -44.2719952943
    2013/10/8 00:30:00 -43.5276412785
    2013/10/8 00:59:59 -41.9842746582
    2013/10/8 01:30:00 -39.7226999863
    2013/10/8 02:00:00 -36.8452198361
    2013/10/8 02:30:00 -33.459799008
    2013/10/8 03:00:00 -29.6691191507
    2013/10/8 03:30:00 -25.5652187709
    2013/10/8 03:59:59 -21.2281801291
    2013/10/8 04:30:00 -16.7272357302


What we are going to want to do is to create a new file which has the
time, specified in decimal hours, and the solar zenith angle (i.e. 90
degrees minus the elevation) into a new file ``files/data/zenith.dat``,
but only when the Sun is above the horizon.

Let's first concentrate on reading the data in:

.. code:: python

    filename = 'files/data/elevation.dat'
    fp = open(filename,"r")
Now we will use ``readlines`` to return a list of strings:

.. code:: python

    sdata = fp.readlines() 
    print sdata

.. parsed-literal::

    ['2013/10/8 00:00:00 -44.2719952943\n', '2013/10/8 00:30:00 -43.5276412785\n', '2013/10/8 00:59:59 -41.9842746582\n', '2013/10/8 01:30:00 -39.7226999863\n', '2013/10/8 02:00:00 -36.8452198361\n', '2013/10/8 02:30:00 -33.459799008\n', '2013/10/8 03:00:00 -29.6691191507\n', '2013/10/8 03:30:00 -25.5652187709\n', '2013/10/8 03:59:59 -21.2281801291\n', '2013/10/8 04:30:00 -16.7272357302\n', '2013/10/8 05:00:00 -12.1229087343\n', '2013/10/8 05:30:00 -7.44278286026\n', '2013/10/8 06:00:00 -1.67990284889\n', '2013/10/8 06:30:00 2.07557325291\n', '2013/10/8 06:59:59 6.41682356012\n', '2013/10/8 07:30:00 10.718795157\n', '2013/10/8 08:00:00 14.8409321418\n', '2013/10/8 08:30:00 18.7041059194\n', '2013/10/8 09:00:00 22.2360923619\n', '2013/10/8 09:30:00 25.3625807186\n', '2013/10/8 09:59:59 28.0062976444\n', '2013/10/8 10:30:00 30.0911497093\n', '2013/10/8 11:00:00 31.54841838\n', '2013/10/8 11:30:00 32.3246113226\n', '2013/10/8 12:00:00 32.389146365\n', '2013/10/8 12:30:00 31.7393119221\n', '2013/10/8 12:59:59 30.4007451089\n', '2013/10/8 13:30:00 28.4231526272\n', '2013/10/8 14:00:00 25.8729768496\n', '2013/10/8 14:30:00 22.8253857155\n', '2013/10/8 15:00:00 19.3576781834\n', '2013/10/8 15:30:00 15.5452510038\n', '2013/10/8 15:59:59 11.4587795592\n', '2013/10/8 16:30:00 7.17635425621\n', '2013/10/8 17:00:00 2.81567654312\n', '2013/10/8 17:30:00 -1.12901415483\n', '2013/10/8 18:00:00 -6.60204292249\n', '2013/10/8 18:30:00 -11.3521065185\n', '2013/10/8 18:59:59 -15.9844936391\n', '2013/10/8 19:30:00 -20.5264294183\n', '2013/10/8 20:00:00 -24.9191119037\n', '2013/10/8 20:30:00 -29.0954447321\n', '2013/10/8 21:00:00 -32.9777242563\n', '2013/10/8 21:30:00 -36.4761369039\n', '2013/10/8 21:59:59 -39.4893158374\n', '2013/10/8 22:30:00 -41.9086473886\n', '2013/10/8 23:00:00 -43.6280450593\n', '2013/10/8 23:30:00 -44.5592559753\n']


We can see that each line of the file contains three fields e.g.:

.. code:: python

    print sdata[0]

.. parsed-literal::

    2013/10/8 00:00:00 -44.2719952943
    


The first field is the date (year, day, month), the second is the time
(hour, minute, second), and the third is the solar elevation at UCL at
that time/date.

To decode each line then we can use ``split()`` e.g.

.. code:: python

    print sdata[0].split()

.. parsed-literal::

    ['2013/10/8', '00:00:00', '-44.2719952943']


what we want is the time and elevation fields, so we will make a loop to
get this, but ``break`` from the loop after the first entry at the
moment:

.. code:: python

    filename = 'files/data/elevation.dat'
    fp = open(filename,"r")
    
    for i in fp.readlines():
        data = i.split()
        time = data[1]
        elevation = float(data[2])
        print time,elevation
        break
    fp.close()

.. parsed-literal::

    00:00:00 -44.2719952943


We need to convert the time field to minutes. We can start this by
splitting the string on ``:``:

.. code:: python

    time = data[1].split(':')
    print time

.. parsed-literal::

    ['00', '00', '00']


then convert these to ``float`` and add up the minutes:

.. code:: python

    time = [float(i) for i in data[1].split(':')]
    hours = time[0] + time[1]/60. + time[2]/(60.*60)
    print hours

.. parsed-literal::

    0.0


we can easily convert elevation to zenith angle.

.. code:: python

    zenith = 90. - elevation
    print zenith

.. parsed-literal::

    134.271995294


Putting this together, only printing when the zenith is less than or
equal to 90.:

.. code:: python

    filename = 'files/data/elevation.dat'
    fp = open(filename,"r")
    
    for i in fp.readlines():
        data = i.split()
        time = [float(i) for i in data[1].split(':')]
        hours = time[0] + time[1]/60. + time[2]/(60.*60)
        zenith = 90. - float(data[2])
        if zenith <= 90.:
            print hours,zenith
    fp.close()

.. parsed-literal::

    6.5 87.9244267471
    6.99972222222 83.5831764399
    7.5 79.281204843
    8.0 75.1590678582
    8.5 71.2958940806
    9.0 67.7639076381
    9.5 64.6374192814
    9.99972222222 61.9937023556
    10.5 59.9088502907
    11.0 58.45158162
    11.5 57.6753886774
    12.0 57.610853635
    12.5 58.2606880779
    12.9997222222 59.5992548911
    13.5 61.5768473728
    14.0 64.1270231504
    14.5 67.1746142845
    15.0 70.6423218166
    15.5 74.4547489962
    15.9997222222 78.5412204408
    16.5 82.8236457438
    17.0 87.1843234569


Now, writing to an output file ``files/data/zenith.dat``:

.. code:: python

    ifilename = 'files/data/elevation.dat'
    ofilename = 'files/data/zenith.dat'
    
    ifp = open(ifilename,"r")
    ofp = open(ofilename,"w")
    
    for i in ifp.readlines():
        data = i.split()
        time = [float(i) for i in data[1].split(':')]
        hours = time[0] + time[1]/60. + time[2]/(60.*60)
        zenith = 90. - float(data[2])
        if zenith <= 90.:
            ofp.write("%.1f %.3f\n"%(hours,zenith))
    ifp.close()
    ofp.close()
We could check the output file from unix:

.. code:: python

    !head -10 < files/data/zenith.dat

.. parsed-literal::

    6.5 87.924
    7.0 83.583
    7.5 79.281
    8.0 75.159
    8.5 71.296
    9.0 67.764
    9.5 64.637
    10.0 61.994
    10.5 59.909
    11.0 58.452


.. code:: python

    !ls -l files/data/zenith.dat

.. parsed-literal::

    -rw-r--r--  1 plewis  staff  257  8 Oct 22:23 files/data/zenith.dat


Exercise 2.4
------------

The text file
`files/data/modis\_files.txt <files/data/modis_files.txt>`__ contains a
listing of hdf format files that are in the directory
``/data/geospatial_19/ucfajlg/fire/Angola/MOD09`` on the UCL Geography
system. The contents of the file looks like (first 10 lines):

.. code:: python

    !head -10 < files/data/modis_files.txt

.. parsed-literal::

    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004001.h19v10.005.2008109063923.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004002.h19v10.005.2008108084250.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004003.h19v10.005.2008108054126.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004004.h19v10.005.2008108112322.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004005.h19v10.005.2008108173219.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004006.h19v10.005.2008108214033.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004007.h19v10.005.2008109081257.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004008.h19v10.005.2008109111447.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004009.h19v10.005.2008109211421.hdf
    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004010.h19v10.005.2008110031925.hdf


Your task is to create a new file
```files/data/some_modis_files.txt`` <files/data/some_modis_files.txt>`__
that contains *only* the file names for the month of August.

You will notice that the file names have a field in them such as
``A2004006``. This is the one you will need to concentrate on, as it
specifies the year (``2004`` here) and the day of year (``doy``),
(``006`` in this example).

There are various ways to find the day of year for a particular month /
year, e,g, look on a
`website <http://www.soils.wisc.edu/cgi-bin/asig/doyCal.rb>`__.

2.8 Doing Some Science
----------------------

Maximum Precipitation
~~~~~~~~~~~~~~~~~~~~~

The Problem
^^^^^^^^^^^

We want to calculate the **maximum** monthly precipitation for regions
of the UK for all years in the 20th Century.

The Data
^^^^^^^^

We have access to monthly average precipitation data as regional totals
from the `UK Met
Office <http://www.metoffice.gov.uk/hadobs/hadukp/data/download.html>`__.

These data are in ASCII format, available over the internet.

e.g.
http://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP\_monthly\_qc.txt

or locally as
```files/data/HadSEEP_monthly_qc.txt`` <files/data/HadSEEP_monthly_qc.txt>`__.

for South East England.

Solving the Problem
^^^^^^^^^^^^^^^^^^^

With just the Python skills you have learned so far, you should be able
to solve a problem of this nature.

Before diving into this though, you need to think through **what steps**
you need to go through to achieve your aim?

At a 'high' level, this could be:

1. Examine the data
2. Read the data into the computer program
3. Select which years you want
4. Find the maximum value for each year over all months
5. Print the results

So now we need to think about how to implement these steps.

Examine the data
^^^^^^^^^^^^^^^^

For the first step, there are many ways you could do this.

You will probably want to look at the data set `in a
browser <files/data/HadSEEP_monthly_qc.txt>`__.

You should see that the data are 'white space' separated.

The first 4 lines are 'header' text, giving contextual information on
the data.

Subsequent lines have the **year** in the first column, then 12 columns
of monthly precipitation, then an annual total.

Read the data into the computer program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a. You could simply save the file using 'Save As ...' from the browser.

b. You could, if you really wanted, just copy and paste the data into a
   file on the local system.

c. You could use the unix command ``wget``:

| ``berlin% mkdir -p ~/Data/python/Chapter2_Python_intro/files/data``
| ``berlin% cd ~/Data/python/Chapter2_Python_intro``
| ``berlin% wget -O files/data/HadSEEP_monthly_qc.txt \         http://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt``

d. You could download and read the file directly from a URL within
   Python

Let us suppose that you had downloaded the file and saved it as
``files/data/HadSEEP_monthly_qc.txt``.

In this case, we would use:

.. code:: python

    filename = 'files/data/HadSEEP_monthly_qc.txt'
    
    fp = open(filename,'r')
    raw_data = fp.readlines()
    fp.close()
    
    print raw_data[:10]

.. parsed-literal::

    ['Monthly Southeast England precipitation (mm). Daily automated values used after 1996.\n', 'Wigley & Jones (J.Climatol.,1987), Gregory et al. (Int.J.Clim.,1991)\n', 'Jones & Conway (Int.J.Climatol.,1997), Alexander & Jones (ASL,2001). Values may change after QC.\n', 'YEAR   JAN   FEB   MAR   APR   MAY   JUN   JUL   AUG   SEP   OCT   NOV   DEC   ANN\n', ' 1873  87.1  50.4  52.9  19.9  41.1  63.6  53.2  56.4  62.0  86.0  59.4  15.7  647.7\n', ' 1874  46.8  44.9  15.8  48.4  24.1  49.9  28.3  43.6  79.4  96.1  63.9  52.3  593.5\n', ' 1875  96.9  39.7  22.9  37.0  39.1  76.1 125.1  40.8  54.7 137.7 106.4  27.1  803.5\n', ' 1876  31.8  71.9  79.5  63.6  16.5  37.2  22.3  66.3 118.2  34.1  89.0 162.9  793.3\n', ' 1877 146.0  47.7  56.2  66.4  62.3  24.9  78.5  82.4  38.4  58.1 144.5  54.2  859.6\n', ' 1878  39.9  44.7  34.2  76.6  96.0  46.8  42.3 133.1  35.7  72.9  94.1  40.7  757.0\n']


So we have read the data in well enough, but it's not really in a
convenient format.

| First, it has 4 lines at the top that we don't want.
| Second, although the data are in a list for each line, each line is
stored as a string.

Since we know about lists, we might suppose that it would be better to
have each line as a list, with each 'white space' separated item being
an element of the list.

If we have a string such as:

``' 1873  87.1  50.4  52.9  19.9  41.1  63.6  53.2  56.4  62.0  86.0  59.4  15.7  647.7\n'``

one way to achieve this would be to use ``split()``:

.. code:: python

    line_data = ' 1873 87.1 50.4 52.9 19.9 41.1 63.6 53.2 56.4 62.0 86.0 59.4 15.7 647.7\n'
    year_data = line_data.split()
    print year_data

.. parsed-literal::

    ['1873', '87.1', '50.4', '52.9', '19.9', '41.1', '63.6', '53.2', '56.4', '62.0', '86.0', '59.4', '15.7', '647.7']


Thats useful, and we could loop over each line and perform this to get
line lists with the first element as the year, second as precipitation
in January, etc.

But each element is still a string, and really, we want these as
``float``.

We can convert ``str`` to ``float`` using ``float()``, but we have to do
this for each string individually.

We can do this in a loop:

.. code:: python

    line_data = ' 1873 87.1 50.4 52.9 19.9 41.1 63.6 53.2 56.4 62.0 86.0 59.4 15.7 647.7\n'
    year_data = line_data.split()
    
    for column,this_element in enumerate(year_data):
        year_data[column] = float(this_element)
    
    print 'format now',type(year_data[0])
    print year_data

.. parsed-literal::

    format now <type 'float'>
    [1873.0, 87.1, 50.4, 52.9, 19.9, 41.1, 63.6, 53.2, 56.4, 62.0, 86.0, 59.4, 15.7, 647.7]


Now we know how to convert each line of data into a list of floating
point numbers.

In practice, we will see later in the course that there are simpler ways
of achieving (using ```numpy`` <http://www.numpy.org/>`__).

We should first chop off the first 4 lines of data:

.. code:: python

    required_data = raw_data[4:]
    
    # lets check what the first line is now
    print required_data[0]

.. parsed-literal::

     1873  87.1  50.4  52.9  19.9  41.1  63.6  53.2  56.4  62.0  86.0  59.4  15.7  647.7
    


Putting all of this together:

.. code:: python

    # specify filename
    filename = 'files/data/HadSEEP_monthly_qc.txt'
    
    # read the data, chop off first 4 lines 
    # and store in required_data
    fp = open(filename,'r')
    raw_data = fp.readlines()
    fp.close()
    required_data = raw_data[4:]
    
    # set up list to store data in
    data = []
    
    
    # loop over each line
    for line_data in required_data:
        # split on white space
        year_data = line_data.split()
        
        # convert data to float
        for column,this_element in enumerate(year_data):
            year_data[column] = float(this_element)
        data.append(year_data)
Now we have the data read in, as floating point values, in the 2-D list
called ``data``:

.. code:: python

    print data[0]
    print data[1]

.. parsed-literal::

    [1873.0, 87.1, 50.4, 52.9, 19.9, 41.1, 63.6, 53.2, 56.4, 62.0, 86.0, 59.4, 15.7, 647.7]
    [1874.0, 46.8, 44.9, 15.8, 48.4, 24.1, 49.9, 28.3, 43.6, 79.4, 96.1, 63.9, 52.3, 593.5]


and we can compare this with the `original data we saw on the
web <http://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt>`__
or the `file we downloaded <files/data/HadSEEP_monthly_qc.txt>`__ to
check it's been read in correctly.

Select which years you want
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want years 1900 to 1999.

The year is stored in the first column, e.g. ``data[10][0]``, and we
want columns ``1`` to ``-1`` (i.e. skip the first and last column):

.. code:: python

    print data[10][0]
    print data[10][1:-1]

.. parsed-literal::

    1883.0
    [60.2, 97.4, 23.6, 36.5, 48.1, 53.3, 69.7, 21.7, 100.6, 58.1, 97.8, 22.5]


.. code:: python

    c20_data = []
    for line in data:
        if (line[0] >= 1900) and (line[0] < 2000):
            c20_data.append(line[1:-1])
Find the maximum value for each year over all months
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to find the maximum value in each row of ``c20_data`` now.

If we consider row 0, we can use e.g.:

.. code:: python

    print c20_data[0]
    print max(c20_data[0])

.. parsed-literal::

    [92.8, 125.9, 23.3, 30.7, 30.0, 74.6, 31.0, 73.3, 22.3, 56.1, 72.1, 88.2]
    125.9


i.e. in the year 1900 (row 0), for S.E. England, the maximum rainfall
was in February.

.. code:: python

    # Aside: show which month that was
    month_names = [ "Jan", "Feb", "Mar", "Apr", \
        "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
    
    print "In South East England"
    for row in xrange(0,100,10):
        year = 1900 + row
        max_precip = max(c20_data[row])
        month = c20_data[row].index(max_precip)
    
        print "In the year",year,"the rainiest month was",month_names[month],"with",max_precip,"mm"

.. parsed-literal::

    In South East England
    In the year 1900 the rainiest month was Feb with 125.9 mm
    In the year 1910 the rainiest month was Dec with 119.4 mm
    In the year 1920 the rainiest month was Jul with 116.9 mm
    In the year 1930 the rainiest month was Nov with 121.0 mm
    In the year 1940 the rainiest month was Nov with 203.0 mm
    In the year 1950 the rainiest month was Nov with 137.9 mm
    In the year 1960 the rainiest month was Oct with 167.0 mm
    In the year 1970 the rainiest month was Nov with 186.4 mm
    In the year 1980 the rainiest month was Oct with 110.1 mm
    In the year 1990 the rainiest month was Feb with 122.3 mm


.. code:: python

    # max precip for all years
    
    result = []
    for row in xrange(100):
        result.append(max(c20_data[row]))
Print the results
^^^^^^^^^^^^^^^^^

.. code:: python

    print "In South East England, the maximum value for the years 1900 to 1999 is"
    print result
    print "The highest rainfall in a month was",max(result),"mm"
    print "It occurred in",result.index(max(result))+1900

.. parsed-literal::

    In South East England, the maximum value for the years 1900 to 1999 is
    [125.9, 98.7, 97.2, 188.4, 96.0, 104.5, 127.3, 129.5, 83.8, 143.9, 119.4, 153.6, 151.6, 106.5, 190.2, 163.9, 110.7, 135.1, 151.1, 121.4, 116.9, 70.8, 92.2, 142.5, 110.2, 98.1, 143.8, 138.5, 137.0, 175.6, 121.0, 101.3, 146.4, 74.1, 176.3, 148.2, 112.8, 124.9, 93.6, 154.0, 203.0, 117.3, 94.3, 130.2, 117.0, 103.8, 126.7, 150.7, 125.3, 189.3, 137.9, 161.9, 99.9, 87.5, 131.0, 110.5, 113.7, 97.7, 107.4, 143.4, 167.0, 102.0, 94.0, 141.0, 97.7, 126.9, 129.1, 126.6, 135.5, 108.4, 186.4, 134.4, 94.0, 76.6, 164.7, 122.8, 141.5, 132.8, 144.9, 122.6, 110.1, 131.2, 143.0, 98.5, 112.4, 103.7, 110.1, 198.7, 143.8, 143.8, 122.3, 102.0, 132.8, 133.9, 115.6, 143.1, 122.6, 100.6, 128.1, 109.5]
    The highest rainfall in a month was 203.0 mm
    It occurred in 1940


Exercise 2.5
------------

That is quite an achievement, given the limited amount of programming
you know so far.

If you go through this though, you will (should) see that it is really
not very efficient.

For example:

-  we read all the data in and then filter out the years we want (what
   if the dataset were **huge**?)
-  we loop over the 100 years multiple times
-  we store intermediate results

For this exercise, you should look through the code we developed and try
to make it more efficient.

Efficiency should not override clarity and understanding though, so make
sure you can understand what is going on at each stage.

Exercise 2.6
------------

Average Temperature
~~~~~~~~~~~~~~~~~~~

We want to calculate the long-term average temperature (tmax degC) using
observational data at one or more meteorological stations. Such data are
`relevant to understanding climate and its
dynamics <http://www.carbonbrief.org/profiles/global-temperatures/>`__.

We choose the period 1960 to 1990 (30 years average to even out natural
variability).

We can obtain monthly average data for a number of UK stations from the
`UK Met. Office <http://www.metoffice.gov.uk/climate/uk/stationdata>`__.

Not all station records are complete enough for this calculation, so we
select, for example
`Heathrow <http://www.metoffice.gov.uk/climate/uk/stationdata/heathrowdata.txt>`__.

Just with the Python skills you have learned so far, you should be able
to solve a problem of this nature.

Before diving into this though, you need to think through **what steps**
you need to go through to achieve your aim?

At a 'high' level, this could be:

1. Get hold of the data
2. Read the data into the computer program
3. Select which years you want
4. Average the data for each month over all selected years
5. Print the results

So now we need to think about how to implement these steps.

For the first step, there are many ways you could do this.

2.9 Dictionaries
----------------

Dictionaries (type ``dict``) are another way of grouping objects.

These are defined within curley brackets ``{}`` and are distinguished by
having a ``'key`` and ``value`` for each item.

e.g.:

.. code:: python

    a = {'one': 1, 'two': 2, 'three': 3}
    
    # we then refer to the keys and values in the dict as:
    
    print 'a:\n\t',a
    print 'a.keys():\n\t',a.keys()     # the keys
    print 'a.values():\n\t',a.values() # returns the values
    print 'a.items():\n\t',a.items()   # returns a list of tuples

.. parsed-literal::

    a:
    	{'three': 3, 'two': 2, 'one': 1}
    a.keys():
    	['three', 'two', 'one']
    a.values():
    	[3, 2, 1]
    a.items():
    	[('three', 3), ('two', 2), ('one', 1)]


Notice that the order they appear in is not necessarily the same as when
we generated the dictionary.

We refer to specific items as e.g.:

.. code:: python

    print a['one']

.. parsed-literal::

    1


We can loop over dictionaries in various interesting ways:

.. code:: python

    for k in a.keys():
        print a[k]

.. parsed-literal::

    3
    2
    1


.. code:: python

    for k,v in a.items():
        print k,v

.. parsed-literal::

    three 3
    two 2
    one 1


If you really need to process in some order, you need to sort the keys
in some way:

.. code:: python

    for k in sort(a.keys()):
        print a[k]

.. parsed-literal::

    1
    3
    2


though in this case this still might not be what you want, so be
careful.

You can add to a list with ``update``:

.. code:: python

    a.update({'four':4,'five':5})
    print a

.. parsed-literal::

    {'four': 4, 'three': 3, 'five': 5, 'two': 2, 'one': 1}


or for a single item:

.. code:: python

    a['six'] = 6
    print a

.. parsed-literal::

    {'six': 6, 'three': 3, 'two': 2, 'four': 4, 'five': 5, 'one': 1}


or delete items:

.. code:: python

    del a['three']
    print a

.. parsed-literal::

    {'six': 6, 'two': 2, 'four': 4, 'five': 5, 'one': 1}


These trivial examples are useful for understanding some basic
operations on dictionaries, but don't show their real power.

configuration file
^^^^^^^^^^^^^^^^^^

A good example is to consider a configuration file.

When we have to run complicated processing jobs (e.g. on stacks of
satellite data), we will often control the processing of these jobs with
some text that we may put in a file.

This would describe the particular conditions that one subset of the
jobs would process, for example.

Following from exercise 2.4 above, we might create a configuration file
with:

.. code:: bash

    [TERRA]  
    dir  = /data/geospatial_19/ucfajlg/fire/Angola/MOD09  
    name = MODIS TERRA data
    year = 2004
    doy_start = 214
    doy_end = 245
    file_list = files/data/modis_files2a.txt

    [AQUA]  
    dir  = /data/geospatial_19/ucfajlg/fire/Angola/MYD09  
    name = MODIS AQUA data
    year = 2004
    doy_start = 214
    doy_end = 245
    file_list = files/data/modis_files2b.txt

This information is in the file
```files/data/modis.cfg`` <files/data/modis.cfg>`__.

We could read and parse this file ourselves:

.. code:: python

    fp = open('files/data/modis.cfg')
    
    # empty dict
    modis = {}
    this_section = modis
    
    # loop over each line
    for line in fp.readlines():
        # strip any extra white space
        line = line.strip()
        # check that there is some text
        # and it starts with [ and ends with ]
        if len(line) and line[0] == '[' and line[-1] == ']':
            section = line[1:-1]
            modis[section] = this_section = {}
        elif len(line) and line.find("=") != -1:
            key,value = line.split("=")
            this_section[key.strip()] = value.strip()
    
    fp.close()
    print modis

.. parsed-literal::

    {'AQUA': {'doy_end': '245', 'doy_start': '214', 'name': 'MODIS AQUA data', 'year': '2004', 'file_list': 'files/data/modis_files2b.txt', 'dir': '/data/geospatial_19/ucfajlg/fire/Angola/MYD09'}, 'TERRA': {'doy_end': '245', 'doy_start': '214', 'name': 'MODIS TERRA data', 'year': '2004', 'file_list': 'files/data/modis_files2a.txt', 'dir': '/data/geospatial_19/ucfajlg/fire/Angola/MOD09'}}


though in practice, we might choose to use the
```ConfigParser`` <http://docs.python.org/2/library/configparser.html>`__
module:

.. code:: python

    import ConfigParser
    
    config = ConfigParser.ConfigParser()
    config.read('files/data/modis.cfg')
    
    # we can convert this to a normal dictionary
    modis = {}
    for k in config.sections():
        modis[k] = dict(config.items(k))
    print modis

.. parsed-literal::

    {'AQUA': {'doy_end': '245', 'doy_start': '214', 'name': 'MODIS AQUA data', 'year': '2004', 'file_list': 'files/data/modis_files2b.txt', 'dir': '/data/geospatial_19/ucfajlg/fire/Angola/MYD09'}, 'TERRA': {'doy_end': '245', 'doy_start': '214', 'name': 'MODIS TERRA data', 'year': '2004', 'file_list': 'files/data/modis_files2a.txt', 'dir': '/data/geospatial_19/ucfajlg/fire/Angola/MOD09'}}


The text file
`files/data/modis\_files2a.txt <files/data/modis_files2a.txt>`__
contains a listing of hdf format files that are in the directory
``/data/geospatial_19/ucfajlg/fire/Angola/MOD09`` and
`files/data/modis\_files2b.txt <files/data/modis_files2b.txt>`__ those
in ``/data/geospatial_19/ucfajlg/fire/Angola/MYD09`` on the UCL
Geography system. The contents of the files looks like (first 10 lines):

.. code:: python

    !head -10 <  files/data/modis_files2b.txt 

.. parsed-literal::

    MYD09GA.A2004001.h19v10.005.2008035021539.hdf
    MYD09GA.A2004002.h19v10.005.2008035115941.hdf
    MYD09GA.A2004003.h19v10.005.2008035223215.hdf
    MYD09GA.A2004004.h19v10.005.2008036154947.hdf
    MYD09GA.A2004005.h19v10.005.2008036025835.hdf
    MYD09GA.A2004006.h19v10.005.2008037030304.hdf
    MYD09GA.A2004007.h19v10.005.2008037072048.hdf
    MYD09GA.A2004008.h19v10.005.2008037155636.hdf
    MYD09GA.A2004009.h19v10.005.2008037162301.hdf
    MYD09GA.A2004010.h19v10.005.2008038034819.hdf


Let's try to use the information in the configuration dictionary
``modis`` to generate a list of the files we want to process:

.. code:: python

    # first, work out how to loop over config sections
    # and get the sub-dictionary
    
    for k,v in modis.items():
        print "\nexamining section",k
        sub_dict = v
        print v

.. parsed-literal::

    
    examining section AQUA
    {'doy_end': '245', 'doy_start': '214', 'name': 'MODIS AQUA data', 'year': '2004', 'file_list': 'files/data/modis_files2b.txt', 'dir': '/data/geospatial_19/ucfajlg/fire/Angola/MYD09'}
    
    examining section TERRA
    {'doy_end': '245', 'doy_start': '214', 'name': 'MODIS TERRA data', 'year': '2004', 'file_list': 'files/data/modis_files2a.txt', 'dir': '/data/geospatial_19/ucfajlg/fire/Angola/MOD09'}


Next, make sure we can read the ``file_list``:

.. code:: python

    print 'reading',sub_dict['file_list']
    fp = open(sub_dict['file_list'],'r')
    file_data = fp.readlines()
    fp.close()
    
    # print the first one, just to see what it looks like
    count = 0
    print file_data[count]

.. parsed-literal::

    reading files/data/modis_files2a.txt
    MOD09GA.A2004001.h19v10.005.2008109063923.hdf
    


Make sure we can get the day of year from this:

.. code:: python

    print file_data[count].split('.')

.. parsed-literal::

    ['MOD09GA', 'A2004001', 'h19v10', '005', '2008109063923', 'hdf\n']


.. code:: python

    print file_data[count].split('.')[1]

.. parsed-literal::

    A2004001


.. code:: python

    doy = int(file_data[count].split('.')[1][-3:])
    print doy

.. parsed-literal::

    1


whats the range of days we want?

.. code:: python

    doy_range = range(int(sub_dict['doy_start']),int(sub_dict['doy_end']))
    print doy_range

.. parsed-literal::

    [214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244]


Is ``doy`` in the range?

.. code:: python

    print doy in doy_range

.. parsed-literal::

    False


So now we have all of the parts we need to create this code:

.. code:: python

    # 1. Read the configuration file
    # into the dict modis
    import ConfigParser
    
    config = ConfigParser.ConfigParser()
    config.read('files/data/modis.cfg')
    
    # we can convert this to a normal dictionary
    modis = {}
    for k in config.sections():
        modis[k] = dict(config.items(k))
    
    # 2. Now, loop over config sections
    # and get the sub-dictionary which we call sub_dict
    
    # 3. set up anb empty list to contain the
    # files we want to process
    wanted_files = []
    
    for k,v in modis.items():
        
        sub_dict = v
        
        # 3a. Read the file list
        fp = open(sub_dict['file_list'],'r')
        file_data = fp.readlines()
        fp.close()
        
        # 3b. find the doy range
        doy_range = range(int(sub_dict['doy_start']),\
                              int(sub_dict['doy_end']))
        
        # 3c. loop over each file read from
        #     sub_dict['file_list']
        for count in xrange(len(file_data)):
            # 3d. extract doy from the file name
            this_file = file_data[count]
            
            doy = int(this_file.split('.')[1][-3:])
            
            # 3e. see if doy is in the range we want?
            if doy in doy_range:
                
                # 3f. put the directory on the fornt
                full_name = sub_dict['dir'] + \
                            '/' + this_file
                wanted_files.append(full_name)
                
    print "I found %d files to process"%len(wanted_files)
    
    # I won't print the whole list as its too long
    # just the first 10
    for f in wanted_files[:10]:
        print f
    


.. parsed-literal::

    I found 62 files to process
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004214.h19v10.005.2007299212915.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004215.h19v10.005.2007300042347.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004216.h19v10.005.2007300091257.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004217.h19v10.005.2007300153436.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004218.h19v10.005.2007300215826.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004219.h19v10.005.2007302194509.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004220.h19v10.005.2007302093547.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004221.h19v10.005.2007302222054.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004222.h19v10.005.2007303011606.hdf
    
    /data/geospatial_19/ucfajlg/fire/Angola/MYD09/MYD09GA.A2004223.h19v10.005.2007303073538.hdf
    


Exercise 2.7
------------

You should modify the example above to make it simpler, if you can spot
any places for that (don't make it more complicated!).

You should then modify it so that the list of files that we want to
process is printed to a file.

2.10 Where we have reached
--------------------------

That is plenty of Python for one day. We would not expect you to be able
to remember all of this the first time you go through it: you will have
to work at it and go through it multiple times. Make sure that the time
you spend going through codes and examples is profitable though: it is
all too easy to sit and stare at a section of code for hours without
*learning* anything ... you need to be engaged with the learning for
this to happen, so take frequent breaks, write your own summary notes
and do whatever you need to get to grips with the basics here.

Although we have rather crammed a lot into this session, that is for
timetabling reasons more than for effectiveness. When you go through it
in your own time, break it into sections and try to get to grips with
each part.

We would not expect you to be able to develop codes of the sort we have
developed above from scratch to start with, but as you go through these
notes and do the exercises, you should start to understand something of
how we build a piece of code.

Our experience is that you should be able to get to grips with these
examples (or at least most of them). Don't start by looking at some
finished piece of code ... start by going through the simple examples to
learn the commands and syntax, then try to put the pieces together.

Once you have learned the basic tools, you will be in a much better
position to think about *algorithms*, i.e. how to break a problem down
into smaller parts that you can solve with the Python that you know.
