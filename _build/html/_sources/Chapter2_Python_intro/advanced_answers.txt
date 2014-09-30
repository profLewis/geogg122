
AE2. Advanced Exercises
=======================

-  `Exercise A2.1 <#Exercise_A2.1>`__
-  `Exercise A2.2 <#Exercise_A2.2>`__
-  `Exercise A2.3 <#Exercise_A2.3>`__

Remember that these exercises are more advanced. You are not *required*
to do these, but may like to do so if you want to stretch yourself.

Exercise A2.1
~~~~~~~~~~~~~

As an exercise for this, you could see if you can simulate the logical
combinations ``xor``, ``nor`` and ``nand``, e.g.:

.. code:: python

    # nand test:
    # see http://en.wikipedia.org/wiki/Logical_NAND
    # (A nand B) is not (A and B)
    
    ABList = [(False,False),(False,True),(True,False),(True,True)]
    for A,B in ABList:
      print '%s nand %s  ='%(str(A),str(B)),not (A and B)

.. parsed-literal::

    False nand False  = True
    False nand True  = True
    True nand False  = True
    True nand True  = False


Answer
~~~~~~

.. code:: python

    """ Exercise 2.1 Scientific Computing
        
        Thu  3 Oct 2013 10:46:58 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
        
        nand test
        
        see http://en.wikipedia.org/wiki/Logical_NAND
    
        (A nand B) is not (A and B)
        
        It is a modification of the code in Exercise A2.1
        of Scientific Computing (https://github.com/profLewis/geogg122)
        
        Edits made from original:
            - neatened output format
    """
    
    # set up a list of tuples to loop over
    ABList = [(False,False),(False,True),(True,False),(True,True)]
    
    # loop over tuples and print A xor B
    # with tabs (\t) for neater output
    for A,B in ABList:
      print '%s\tnand\t%s\t='%(str(A),str(B)),not (A and B)

.. parsed-literal::

    False	nand	False	= True
    False	nand	True	= True
    True	nand	False	= True
    True	nand	True	= False


.. code:: python

    """ Exercise 2.1 Scientific Computing
        
        Thu  3 Oct 2013 10:46:58 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
        
        nor test
        
        see http://en.wikipedia.org/wiki/Logical_NOR
    
        (A nor B) is not (A or B)
        
        It is a modification of the code in Exercise A2.1
        of Scientific Computing (https://github.com/profLewis/geogg122)
        
        Edits made from original:
            - neatened output format
            - modified from nand to nor
    """
    
    # set up a list of tuples to loop over
    ABList = [(False,False),(False,True),(True,False),(True,True)]
    
    # loop over tuples and print A xor B
    # with tabs (\t) for neater output
    for A,B in ABList:
      print '%s\tnor\t%s\t='%(str(A),str(B)),not (A or B)

.. parsed-literal::

    False	nor	False	= True
    False	nor	True	= False
    True	nor	False	= False
    True	nor	True	= False


.. code:: python

    """ Exercise 2.1 Scientific Computing
        
        Thu  3 Oct 2013 10:46:58 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
        
        xor test
        
        see http://en.wikipedia.org/wiki/Logical_XOR
    
        (A xor B) is (A or B) and not (A and B)
        
        It is a modification of the code in Exercise A2.1
        of Scientific Computing (https://github.com/profLewis/geogg122)
        
        Edits made from original:
            - neatened output format
            - modified from nand to xor
    """
    
    # set up a list of tuples to loop over
    ABList = [(False,False),(False,True),(True,False),(True,True)]
    
    # loop over tuples and print A xor B
    # with tabs (\t) for neater output
    for A,B in ABList:
      print '%s\txor\t%s\t='%(str(A),str(B)),(A or B) and not (A and B)

.. parsed-literal::

    False	xor	False	= False
    False	xor	True	= True
    True	xor	False	= True
    True	xor	True	= False


Exercise A2.2
~~~~~~~~~~~~~

a. Work out what the following decimal numbers are in binary:

   | 7
   | 493
   | 127
   | 255
   | 1024

and check your result using the approach we took to confirming ``101``:

::

    101 ==  (1 * 2**6) + \
            (1 * 2**5) + \
            (0 * 2**4) + \
            (0 * 2**3) + \
            (1 * 2**2) + \
            (0 * 2**1) + \
            (1 * 2**0)
        

b. How many bits are needed to represent each of these numbers?

c. What is the largest number you could represent in: (i) a 32 bit
   representation; (b) a 64 bit representation?

d. Recalling that there are 8 bits in a
   `byte <http://en.wikipedia.org/wiki/Byte>`__, what is the largest
   number you could represent in: (a) a single byte; (b) two bytes?

Answer
~~~~~~

**a. Work out what the following decimal numbers are in binary:**

| 7
| 493
| 127
| 255
| 1024

.. code:: python

    for n in (7,493,127,255,1024):
        print n,'\tin binary is',bin(n)

.. parsed-literal::

    7 	in binary is 0b111
    493 	in binary is 0b111101101
    127 	in binary is 0b1111111
    255 	in binary is 0b11111111
    1024 	in binary is 0b10000000000


**check your result using the approach we took to confirming ``101``:**

Long-hand way:

.. code:: python

    7   ==  (1 * 2**2) + \
            (1 * 2**1) + \
            (1 * 2**0)



.. parsed-literal::

    True



.. code:: python

    493 ==  (1 * 2**8) + \
            (1 * 2**7) + \
            (1 * 2**6) + \
            (1 * 2**5) + \
            (0 * 2**4) + \
            (1 * 2**3) + \
            (1 * 2**2) + \
            (0 * 2**1) + \
            (1 * 2**0)



.. parsed-literal::

    True



.. code:: python

    127 ==  (1 * 2**6) + \
            (1 * 2**5) + \
            (1 * 2**4) + \
            (1 * 2**3) + \
            (1 * 2**2) + \
            (1 * 2**1) + \
            (1 * 2**0)



.. parsed-literal::

    True



.. code:: python

    255 ==  (1 * 2**7) + \
            (1 * 2**6) + \
            (1 * 2**5) + \
            (1 * 2**4) + \
            (1 * 2**3) + \
            (1 * 2**2) + \
            (1 * 2**1) + \
            (1 * 2**0)



.. parsed-literal::

    True



.. code:: python

    1024 == (1 * 2**10)+ \
            (0 * 2**9) + \
            (0 * 2**8) + \
            (0 * 2**7) + \
            (0 * 2**6) + \
            (0 * 2**5) + \
            (0 * 2**4) + \
            (0 * 2**3) + \
            (0 * 2**2) + \
            (0 * 2**1) + \
            (0 * 2**0)



.. parsed-literal::

    True



More automatic/advanced way (but more complicated coding):

.. code:: python

    # loop over numbers
    for n in (7,493,127,255,1024):
        
        # convert decimal to binary 
        # then convert to string and ignore 0b at start
        binstr = bin(n)[2:]
        
        # initialise sum as accumulator
        sum = 0
        
        # how many bits in this case?
        nBits = len(binstr)
        print n,'\tin binary is',binstr,": %d bits"%nBits
        
        # loop over each bit
        for c in xrange(nBits):
            
            # extract the bit and exponent
            bit = int(binstr[-(c+1)])
            exp = 2**c
            sum += exp * bit
            print '\t %d x 2^%d = %d x %d \t%d'%(bit,c,bit,exp,sum)
        
        print "%d == %d?"%(n,sum),n == sum    
        print "===================================="

.. parsed-literal::

    7 	in binary is 111 : 3 bits
    	 1 x 2^0 = 1 x 1 	1
    	 1 x 2^1 = 1 x 2 	3
    	 1 x 2^2 = 1 x 4 	7
    7 == 7? True
    ====================================
    493 	in binary is 111101101 : 9 bits
    	 1 x 2^0 = 1 x 1 	1
    	 0 x 2^1 = 0 x 2 	1
    	 1 x 2^2 = 1 x 4 	5
    	 1 x 2^3 = 1 x 8 	13
    	 0 x 2^4 = 0 x 16 	13
    	 1 x 2^5 = 1 x 32 	45
    	 1 x 2^6 = 1 x 64 	109
    	 1 x 2^7 = 1 x 128 	237
    	 1 x 2^8 = 1 x 256 	493
    493 == 493? True
    ====================================
    127 	in binary is 1111111 : 7 bits
    	 1 x 2^0 = 1 x 1 	1
    	 1 x 2^1 = 1 x 2 	3
    	 1 x 2^2 = 1 x 4 	7
    	 1 x 2^3 = 1 x 8 	15
    	 1 x 2^4 = 1 x 16 	31
    	 1 x 2^5 = 1 x 32 	63
    	 1 x 2^6 = 1 x 64 	127
    127 == 127? True
    ====================================
    255 	in binary is 11111111 : 8 bits
    	 1 x 2^0 = 1 x 1 	1
    	 1 x 2^1 = 1 x 2 	3
    	 1 x 2^2 = 1 x 4 	7
    	 1 x 2^3 = 1 x 8 	15
    	 1 x 2^4 = 1 x 16 	31
    	 1 x 2^5 = 1 x 32 	63
    	 1 x 2^6 = 1 x 64 	127
    	 1 x 2^7 = 1 x 128 	255
    255 == 255? True
    ====================================
    1024 	in binary is 10000000000 : 11 bits
    	 0 x 2^0 = 0 x 1 	0
    	 0 x 2^1 = 0 x 2 	0
    	 0 x 2^2 = 0 x 4 	0
    	 0 x 2^3 = 0 x 8 	0
    	 0 x 2^4 = 0 x 16 	0
    	 0 x 2^5 = 0 x 32 	0
    	 0 x 2^6 = 0 x 64 	0
    	 0 x 2^7 = 0 x 128 	0
    	 0 x 2^8 = 0 x 256 	0
    	 0 x 2^9 = 0 x 512 	0
    	 1 x 2^10 = 1 x 1024 	1024
    1024 == 1024? True
    ====================================


If you enjoyed this part of the exercise ;-) , you could repeat this
part of it, but using base 8 (octal) and or base 16 (hexadecimal), which
you will often come across in computing. We might use octal e.g. in unix
file permissions, or hexadecimal more widely in memory addresses
(because it would be too long a number in binary!).

e.g.:

.. code:: python

    n = 493
    # N.B, no 0b or 0x part on the string for octal, just a 
    # leading 0
    octstr = oct(n)[1:]
    sum = 0
    # how many octets in this case? (assuming thats the right word)
    nOct = len(octstr)
    print n,'\tin octal is',octstr,": %d octets"%nOct
        
    # loop over each octets
    for c in xrange(nOct):
        # extract the octet and exponent
        octet = int(octstr[-(c+1)])
        exp = 8**c
        sum += exp * octet
        print '\t %d x 8^%d = %d x %d \t%d'%(octet,c,octet,exp,sum)
    print "%d == %d?"%(n,sum),n == sum    
    print "===================================="

.. parsed-literal::

    493 	in octal is 755 : 3 octets
    	 5 x 8^0 = 5 x 1 	5
    	 5 x 8^1 = 5 x 8 	45
    	 7 x 8^2 = 7 x 64 	493
    493 == 493? True
    ====================================


**b. How many bits are needed to represent each of these numbers?**

.. code:: python

    # bin() converts to binary, but really its a string
    # the first 2 characters of which are '0b'
    # so find the length of the string other than the first two
    # characters
    
    for n in (7,493,127,255,1024):
        binstr = bin(n)[2:]
        print binstr,len(binstr),'bits'

.. parsed-literal::

    111 3 bits
    111101101 9 bits
    1111111 7 bits
    11111111 8 bits
    10000000000 11 bits


**c. What is the largest number you could represent in: (i) a 32 bit
representation; (b) a 64 bit representation?**

In an *unsigned* integer representation, the largest number would be one
with ``1`` in all bit fields.

We *could* add this up, but it's faster to notice that this is one less
than two to the power of the number of bits, e.g. the largest number
with 8 bits is ``2^8 - 1``:

.. code:: python

    print "the largest (unsigned) integer with 8 bits (1 byte) is",2**8 -1

.. parsed-literal::

    the largest (unsigned) integer with 8 bits (1 byte) is 255


.. code:: python

    print "the largest (unsigned) integer with 32 bits is",2**32 -1
    print "the largest (unsigned) integer with 64 bits is",2**64 -1

.. parsed-literal::

    the largest (unsigned) integer with 32 bits is 4294967295
    the largest (unsigned) integer with 64 bits is 18446744073709551615


Sometimes, a *signed* integer representation is used, in which case the
leftmost bit (usually) of the bit field is used to represent the *sign*
(``0`` meaning ``+ve`` and ``1`` meaning ``-ve``), so e.g.:

| ``011`` would be +7 in decimal but
| ``111`` would be -7 in decimal

This means that there is one fewer bit to represent the magnitude of the
number, so e.g. with 8 bits (one byte) you have one bit for the sign,
and 7 bits for magnitude:

.. code:: python

    print "the largest  (signed) integer with 8 bits (1 byte) is",+2**(8-1) -1
    print "the smallest (signed) integer with 8 bits (1 byte) is",-2**(8-1) +1

.. parsed-literal::

    the largest  (signed) integer with 8 bits (1 byte) is 127
    the smallest (signed) integer with 8 bits (1 byte) is -127


Interestingly, in a signed integer representation, there are two numbers
that represent zero:

::

    000
    100

which effectively mean ``+0`` and ``-0``. In that sense, the signed
representation is a little wasteful (but you only lose one number!).

**d. Recalling that there are 8 bits in a
`byte <http://en.wikipedia.org/wiki/Byte>`__, what is the largest number
you could represent in: (a) a single byte; (b) two bytes? **

So, one byte is 8 bits.

As we saw above, for an unsigned representation this can have integers
from ``0`` to ``255``.

For a signed representation this can have integers from ``-127`` to
``+127``.

Two bytes is 16 bits, so:

.. code:: python

    print "the largest (unsigned) integer with 16 bits (2 bytes) is",2**16 -1
    print "the largest   (signed) integer with 16 bits (2 bytes) is",+2**(16-1) -1
    print "the smallest  (signed) integer with 16 bits (2 bytes) is",-2**(16-1) +1

.. parsed-literal::

    the largest (unsigned) integer with 16 bits (2 bytes) is 65535
    the largest   (signed) integer with 16 bits (2 bytes) is 32767
    the smallest  (signed) integer with 16 bits (2 bytes) is -32767


Exercise A2.3
~~~~~~~~~~~~~

.. code:: python

    qa = 0b11111111
    
    qa1 = (qa & 0b00000001) >> 0    # bit 0
    qa2 = (qa & 0b00000010) >> 1    # bit 1
    qa3 = (qa & 0b00000100) >> 2    # bit 2
    qa4 = (qa & 0b00011000) >> 3    # bit 3-4
    qa5 = (qa & 0b11100000) >> 5    # bit 5-7
    
    print 'qa1',bin(qa1)
    print 'qa2',bin(qa2)
    print 'qa3',bin(qa3)
    print 'qa4',bin(qa4)
    print 'qa5',bin(qa5)

.. parsed-literal::

    qa1 0b1
    qa2 0b1
    qa3 0b1
    qa4 0b11
    qa5 0b111


Develop some code to repeat the QA bit masking done above, but make the
code generate the bit masks itself from knowledge of the first and last
of the bit fields you require (assuming they are sequential).

If possible, do this in a function.

Demonstrate its operation with several example bit masks.

Answer
~~~~~~

One way to this elegantly is to use the left shift to generate the bit
masks.

e.g. to put a ``1`` in bit 2:

.. code:: python

    mask2 = 0b1 << 2
    print bin(mask2)

.. parsed-literal::

    0b100


or to fill fields 3-4:

.. code:: python

    mask3 = 0b11 << 3
    print bin(mask3)

.. parsed-literal::

    0b11000


An easier way though is to right shift the qa and perform a bitwise and
with the mask:

.. code:: python

    qa = 0b00011000
    mask3 = 0b11
    print bin((qa >> 3) & mask3)

.. parsed-literal::

    0b11


We need to consider how to pass the information through to this
operation.

One way would be to use a ``dict`` with the ``key`` as the starting
value of the bit field and the ``value`` as the end:

.. code:: python

    fields = {0:0, 1:1, 2:2, 3:4, 5:7}
We access these as:

.. code:: python

    for start,finish in fields.items():
        print start,finish

.. parsed-literal::

    0 0
    1 1
    2 2
    3 4
    5 7


Then form an integer which is ``2^n -1``, where ``n`` is the (inclusive)
length from ``start`` to ``finish``

.. code:: python

    # a test qa with only required bits
    qa = 0b00011000
    start = 3
    finish = 4
    
    print bin(2**(finish-start+1)-1)

.. parsed-literal::

    0b11


.. code:: python

    # qa with all bits filled
    qa = 0b11111111
    
    for start,finish in fields.items():
        mask = 2**(finish-start+1)-1
        print start,finish,bin(mask)

.. parsed-literal::

    0 0 0b1
    1 1 0b1
    2 2 0b1
    3 4 0b11
    5 7 0b111


so now we right shift the ``qa`` by ``start`` and perform a bitwise and
(``&``) with the mask:

.. code:: python

    start = 3
    finish = 4
    qa = 0b00011000
    
    mask = (2**(finish-start+1)-1)
    maskedQA = (qa >> start) & mask
    print bin(maskedQA)

.. parsed-literal::

    0b11


Now we can combine all of these ideas:

.. code:: python

    fields = {0:0, 1:1, 2:2, 3:4, 5:7}
    
    # qa with all bits filled
    qa = 0b11111111
    
    for start,finish in fields.items():
        mask     = (2**(finish-start+1)-1)
        maskedQA = (qa >> start) & mask 
        print start,finish,bin(maskedQA)


.. parsed-literal::

    0 0 0b1
    1 1 0b1
    2 2 0b1
    3 4 0b11
    5 7 0b111


.. code:: python

    """Exercise 2.1 Scientific Computing
        
        Thu  3 Oct 2013 10:46:58 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
        
        bit mask test
        
        Original code
        
    """
    def maskedQA(qa, fields = {0:0, 1:1, 2:2, 3:4, 5:7}):
        """Return a dictionary of masked QA bit fields
        
        Inputs:
        qa -- QA to be masked
        
        Keyword arguments:
        fields -- bit field dictionary (default {0:0, 1:1, 2:2, 3:4, 5:7})
                  Here, the key is the start bit of a mask and the value
                  the end bit (inclusive).
        
        Returns:
        Masked QA in dictionary with same keys as fields
        """
        
        maskedQAs = {}
        
        for start,finish in fields.items():
            mask     = (2**(finish-start+1)-1)
            maskedQAs[start] = (qa >> start) & mask 
    
        return maskedQAs

.. code:: python

    help(maskedQA)

.. parsed-literal::

    Help on function maskedQA in module __main__:
    
    maskedQA(qa, fields={0: 0, 1: 1, 2: 2, 3: 4, 5: 7})
        Return a dictionary of masked QA bit fields
        
        Inputs:
        qa -- QA to be masked
        
        Keyword arguments:
        fields -- bit field dictionary (default {0:0, 1:1, 2:2, 3:4, 5:7})
                  Here, the key is the start bit of a mask and the value
                  the end bit (inclusive).
        
        Returns:
        Masked QA in dictionary with same keys as fields
    


.. code:: python

    # testing
    
    qaDict = maskedQA(0b11111111)
    for k in qaDict.keys():
        print k,qaDict[k],bin(qaDict[k])

.. parsed-literal::

    0 1 0b1
    1 1 0b1
    2 1 0b1
    3 3 0b11
    5 7 0b111


.. code:: python

    qaDict = maskedQA(0b01010101)
    for k in qaDict.keys():
        print k,qaDict[k],bin(qaDict[k])

.. parsed-literal::

    0 1 0b1
    1 0 0b0
    2 1 0b1
    3 2 0b10
    5 2 0b10

