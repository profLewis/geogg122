
E2. Exercises
=============

This notebook contains answers and notes for the following exercises:

-  `Exercise 2.1 <#Exercise_2.1>`__

   -  `Answer 2.1 <#Answer-2.1>`__

-  `Exercise 2.2 <#Exercise_2.2>`__

   -  `Answer 2.2 <#Answer-2.2>`__

-  `Exercise 2.3 <#Exercise_2.3>`__

   -  `Answer 2.3 <#Answer-2.3>`__

-  `Exercise 2.4 <#Exercise_2.4>`__

   -  `Answer 2.4 <#Answer-2.4>`__

-  `Exercise 2.5 <#Exercise_2.5>`__

   -  `Answer 2.5 <#Answer-2.5>`__

-  `Exercise 2.6 <#Exercise_2.6>`__

   -  `Answer 2.6 <#Answer-2.6>`__

-  `Exercise 2.7 <#Exercise_2.7>`__

   -  `Answer 2.7 <#Answer-2.7>`__

Exercise 2.1
------------

You were given some code:

.. code:: python

    #!/usr/bin/env python
    
    
    
    # hunger threshold in hours
    hungerThreshold = 3.0
    # sleep threshold in hours
    sleepThreshold = 8.0
    
    # time since fed, in hours
    timeSinceFed = 4.0
    # time since sleep, in hours
    timeSinceSleep = 3.0
    
    # Note use of \ as line continuation here
    # It is poor style to have code lines > 79 characters
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


The code above works fine, but the large blocks of logical tests are not
very clear or readable, and contain repeated items.

Modify this block of code to be clearer by assigning the individual
logical tests to variables,

e.g.

``tired = timeSinceSleep >= sleepThreshold``

Answer 2.1
----------

This is quite easily made clearer, and is also improved by making sure
you comment what you are doing.

It is normally a good idea to put some information on what the purpose
of the code is etc.

It is also a good idea if you get into the practice of describing what
changes you have made to the code from the original version that this is
based on, to give full attribution. We will see that this is important
with regard to plagiarism in coursework submission.

Hasve a look at the `Python
styleguide <http://www.python.org/dev/peps/pep-0008/#code-lay-out>`__
for ideas on what makes good clear code.

You wouldn't have been expected to do *all* of these things (the code
below is mainly to give you some ideas for what to do next time!), but
hopefully you will have at least set the variables:

| ``tired  = (timeSinceSleep >= sleepThreshold)``
| ``hungry = (timeSinceFed >= hungerThreshold)``

and used them in the code for greater clarity.

.. code:: python

    """ Exercise 2.1 Scientific Computing
        
        Thu  3 Oct 2013 10:46:58 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
      
        This code prints information on whether
        I am tired and/or hungry.
        
        It is controlled by the variables:
            timeSinceFed
            timeSinceSleep
            
        which are checked against hunger and
        sleep thresholds:
            hungerThreshold
            sleepThreshold
            
        All times given as float, in hours
            
            
        It is a modification of the code in Exercise 2.1
        of Scientific Computing (https://github.com/profLewis/geogg122)
        
        Edits made from original:
            - added detailed comment strings
            - neatened up the comments
            - made code easier to read by setting variables
              tired and hungry.
            - added a new result for 'tired or hungry'
            - added tabs (\t) to the print statements to get
              neater output formatting.
              
    """
    
    # Thresholds
    hungerThreshold = 3.0    # hunger threshold in hours
    sleepThreshold  = 8.0    # sleep threshold in hours
    
    # Control variables
    timeSinceFed   = 4.0     # time since fed, in hour
    timeSinceSleep = 3.0     # time since sleep, in hours
    
    # logical tests for tired and hungry
    tired  = (timeSinceSleep >= sleepThreshold)
    hungry = (timeSinceFed >= hungerThreshold)
    
    # print results
    print "Tired and hungry?\t",  tired and hungry    
    print "Tired or hungry?\t\t", tired or hungry    
    print "Just tired?\t\t",      tired and not hungry
    print "Just hungry?\t\t",     hungry and not tired

.. parsed-literal::

    Tired and hungry?	False
    Tired or hungry?		True
    Just tired?		False
    Just hungry?		True


Exercise 2.2
------------

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
    
    # print item day_number in the list week
    print "today is",week[day_number]

.. parsed-literal::

    today is Tuesday


Based on the example below, **set up a diary for youself for the week to
print out what you should be doing today, using the conditional
structure ``if .. elif ... else``.**

Answer 2.2
----------

.. code:: python

    '''
        Exercise 2.2A Scientific Computing
        
        Mon  7 Oct 2013 10:43:38 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
      
        This code prints a diary for today.
        
    '''
    
    '''The following code block is taken verbatim from 
       The Scientific Computing notes
    '''
    # This imports a module that we can use to access dates
    from datetime import datetime
    
    # set up a list of days of the week, starting Monday
    # Note the line continuation here with \
    week = ['Monday','Tuesday','Wednesday','Thursday',\
            'Friday','Saturday','Sunday']
    
    # This part gives the day of the week
    # as an integer, 0 -> Monday, 1 -> Tuesday etc.
    day_number = datetime.now().weekday()
    
    # print item day_number in the list week
    print "Today is",week[day_number]
    
    '''New code: my own work
       Following the example in the question for E2.2A
    '''
    
    if day_number == 0:   # Monday
        print 'Spend the day learning Python'
    elif day_number == 1: # Tuesday
        print 'Spend the day learning Python'
    elif day_number == 2: # Wednesday
        print 'Go to Python class'
    elif day_number == 3: # Thursday
        print 'Spend the day learning Python'
    elif day_number == 4: # Friday
        print 'Spend the day learning Python'
    elif day_number == 5: # Saturday
        print 'Spend the day learning Python'
    elif day_number == 6: # Sunday
        print 'Spend the day learning Python'
    else:
        print "get some sleep"


.. parsed-literal::

    Today is Tuesday
    Spend the day learning Python


You should see from this that this is a rather awkward way to set up
something of this nature, and it is prone to error in typing (you could
easily miss a day out or type something else wrong).

B.
^^

You could set up the basic calendar for the week in a list, with the
first entry representing Monday, the second Tuesday etc.

.. code:: python

    my_diary = ['Spend the day practicing Python',\
                'Spend the day practicing Python',\
                'Do some reading in the library at UCL', \
                'Remember to wake up early to get to the Python class at UCL',\
                'Spend the day practicing Python',\
                'Remember to wake up early to go to classes at Imperial College',\
                'Work at Python exercises from home',\
                'Work at Python exercises from home']
Using a list of this sort, **print the diary entry for today *without*
using conditional statements.**

Criticise the code you develop and make suggestions for improvement.

Answer
~~~~~~

.. code:: python

    '''
        Exercise 2.2B Scientific Computing
        
        Mon  7 Oct 2013 10:43:38 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
      
        This code prints a diary for today.
        
    '''
    
    '''The following code block is taken verbatim from 
       The Scientific Computing notes
    '''
    # This imports a module that we can use to access dates
    from datetime import datetime
    
    # set up a list of days of the week, starting Monday
    # Note the line continuation here with \
    week = ['Monday','Tuesday','Wednesday','Thursday',\
            'Friday','Saturday','Sunday']
    
    # This part gives the day of the week
    # as an integer, 0 -> Monday, 1 -> Tuesday etc.
    day_number = datetime.now().weekday()
    
    '''New code: my own work
       Following the example in the question for E2.2B
    '''
    
    my_diary = ['spend the day doing Python',\
                'do some reading in the library at UCL', \
                'remember to wake up early to get to the Python class at UCL',\
                'spend the day doing Python',\
                'remember to wake up early to go to classes at Imperial College',\
                'work at Python exercises from home',\
                'work at Python exercises from home']
    
    
    print "Today is",week[day_number],'so',my_diary[day_number]


.. parsed-literal::

    Today is Tuesday so do some reading in the library at UCL


This is a bit better, but it's still too easy to get the entries in the
list wrong, or get confused that Monday is day 0, so we would typically
use a dictionary (``dict``) for something of this nature.

.. code:: python

    '''
        Exercise 2.2B Scientific Computing
        
        Mon  7 Oct 2013 10:43:38 BST
        
        P. Lewis : p.lewis@ucl.ac.uk
      
        This code prints a diary for today.
        
    '''
    
    '''The following code block is taken verbatim from 
       The Scientific Computing notes
    '''
    # This imports a module that we can use to access dates
    from datetime import datetime
    
    # This part gives the day of the week
    # as an integer, 0 -> Monday, 1 -> Tuesday etc.
    day_number = datetime.now().weekday()
    
    '''New code: my own work
       Following the example in the question for E2.2B
    '''
    
    week = {0: 'Monday',\
            1: 'Tuesday',\
            2: 'Wednesday',\
            3: 'Thursday',\
            4: 'Friday',\
            5: 'Saturday',\
            6: 'Sunday'}
    
    
    my_diary = {'Monday':    'spend the day doing Python',\
                'Tuesday':   'do some reading in the library at UCL',\
                'Wednesday': 'remember to wake up early to get to the Python class at UCL',\
                'Thursday':  'spend the day doing Python',\
                'Friday':    'remember to wake up early to go to classes at Imperial College',\
                'Saturday':  'work at Python exercises from home',\
                'Sunday':    'work at Python exercises from home'}
    
    today = week[day_number]
    print "Today is",today,'so',my_diary[today]


.. parsed-literal::

    Today is Tuesday so do some reading in the library at UCL


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

    <matplotlib.text.Text at 0x106501890>




.. image:: main_answers_files/main_answers_29_1.png


**Produce a plot of the number of sunshine hours for Lowestoft for the
year 2012** using the data given above.

Hint: the data have newline chcracters ``\n`` at the end of each line of
data, and are separated by white space withion each line.

Answer 2.3
----------

First, we need to split the string ``data`` by newline (``\n``) to give
a list of lines:

.. code:: python

    ldata = data.split('\n')
    
    print ldata

.. parsed-literal::

    ['   2012   1    8.7    3.1      5   33.1   53.9', '   2012   2    7.1    1.6     13   13.8   86.6', '   2012   3   11.3    3.7      2   64.2  141.3', '   2012   4   10.9    4.3      3  108.9  151.1', '   2012   5   15.1    8.6      0   46.6  171.3', '   2012   6   17.9   10.9      0   74.4  189.0', '   2012   7   20.3   12.8      0   93.6  206.9', '   2012   8   22.0   14.0      0   59.6  217.3', '   2012   9   18.9    9.5      0   38.8  200.8', '   2012  10   13.6    7.9      0   92.7   94.7', '   2012  11   10.5    4.4      2   62.1   79.6  ', '   2012  12    7.9    2.4      8   95.6   41.9  ']


Next, we need to loop over each line and split by whitespace.

This will involve something like:

.. code:: python

    # example using first line
    this_line = ldata[0]
    items = this_line.split()
    print items

.. parsed-literal::

    ['2012', '1', '8.7', '3.1', '5', '33.1', '53.9']


.. code:: python

    ldata = data.split('\n')
    
    # set empty lists to put the data in
    x = []
    y = []
    
    for this_line in ldata:
        items = this_line.split()
        # convert from string to float
        x.append(float(items[1])) # the month
        y.append(float(items[6])) # sunshine hrs
    
    print x
    print y

.. parsed-literal::

    [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    [53.9, 86.6, 141.3, 151.1, 171.3, 189.0, 206.9, 217.3, 200.8, 94.7, 79.6, 41.9]


Now we just need to plot it:

.. code:: python

    # import the pylab module
    import pylab as plt
    
    plt.plot(x,y)
    plt.xlabel('month of 2012')
    plt.ylabel('Sunshine hours')
    plt.title('Sunshine hours for Lowestoft, UK, 2012') 



.. parsed-literal::

    <matplotlib.text.Text at 0x106499550>




.. image:: main_answers_files/main_answers_38_1.png


We could make it a bit more compact and general, but if you do, make
sure it is still easily readable.

.. code:: python

    import pylab as plt
    
    items = [[float(i) \
                for i in j.split()] \
                    for j in data.split('\n')]
    
    # get specific columns from items 
    x = [i[1] for i in items]
    y = [i[6] for i in items]
    
    # bigger graph if we want
    plt.figure(figsize=(14, 6))
    plt.plot(x,y)
    plt.xlabel('month of 2012')
    plt.ylabel('Sunshine hours')
    plt.title('Sunshine hours for Lowestoft, UK, 2012') 



.. parsed-literal::

    <matplotlib.text.Text at 0x106787510>




.. image:: main_answers_files/main_answers_40_1.png


You *might think* that labelling with the month name would be nicer.

Thats quite a bit more complicated, but we'll put it in here anyway for
future reference:

.. code:: python

    import pylab as plt
    
    items = [[float(i) \
                for i in j.split()] \
                    for j in data.split('\n')]
    
    # get specific columns from items 
    x = [int(i[1]) for i in items]
    y = [i[6] for i in items]
    
    months = ["Jan", "Feb", "Mar", "Apr", \
        "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
    
    # need access to ax to mess with xticks
    fig, ax = plt.subplots(figsize=(14, 6))
    plt.plot(x,y)
    
    # lots of hassle to do this sort of thing ...
    # but it is possible
    #
    # first set the limits to be the
    # same as x
    plt.xlim(x[0],x[-1])
    # then set the xticks to the values of x
    # to make sure there are 12 of them
    ax.set_xticks(x)
    # then replace these by the months
    ax.set_xticklabels(months)
    
    plt.xlabel('month of 2012')
    plt.ylabel('Sunshine hours')
    plt.title('Sunshine hours for Lowestoft, UK, 2012') 



.. parsed-literal::

    <matplotlib.text.Text at 0x106855110>




.. image:: main_answers_files/main_answers_42_1.png


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


Your task is to create a new file ``files/data/some_modis_files.txt``
that contains *only* the file names for the month of August.

You will notice that the file names have a field in them such as
``A2004006``. This is the one you will need to concentrate on, as it
specifies the year (``2004`` here) and the day of year (``doy``),
(``006`` in this example).

There are various ways to find the day of year for a particular month /
year, e,g, look on a
`website <http://www.soils.wisc.edu/cgi-bin/asig/doyCal.rb>`__.

Answer 2.4
----------

First then, find out which day of year range you want.

August 2004 was doy 214 to 244 inclusive, so in python:

.. code:: python

        range(214,245)

We should know how to read data from files from the material above.

.. code:: python

    # ls /data/geospatial_19/ucfajlg/fire/Angola/MOD09/*.hdf > /tmp/modis_files.txt
    fp = open('files/data/modis_files.txt','r')
    for line in fp.readlines():
        print line
        break   # break in here just so it doesnt print too much 
                # dont put that in your code !!!
    fp.close()

.. parsed-literal::

    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004001.h19v10.005.2008109063923.hdf
    


we have the filename e.g.

``/data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004001.h19v10.005.2008109063923.hdf``

in the variable ``line``.

Now we want to split this to find the filename, which will be the last
element (-1):

.. code:: python

    # split the string on '/', the file separator
    aline = line.split('/')
    print aline

.. parsed-literal::

    ['', 'data', 'geospatial_19', 'ucfajlg', 'fire', 'Angola', 'MOD09', 'MOD09GA.A2004001.h19v10.005.2008109063923.hdf\n']


.. code:: python

    # and all we want is the last item:
    
    fname = line.split('/')[-1]
    print fname

.. parsed-literal::

    MOD09GA.A2004001.h19v10.005.2008109063923.hdf
    


Now we need to split this up, with ``.`` (dot) as the separator, and get
the second item:

.. code:: python

    fname = line.split('/')[-1]
    fbits = fname.split('.')
    print fbits
    
    datebit = fbits[1]
    print datebit

.. parsed-literal::

    ['MOD09GA', 'A2004001', 'h19v10', '005', '2008109063923', 'hdf\n']
    A2004001


The day of year is the last 3 elements of this string:

.. code:: python

    doy = int(datebit[-3:])
    
    print doy

.. parsed-literal::

    1


And check to see if doy is in the required range:

Putting this together:

.. code:: python

    date_range = range(214,245)
    
    # ls /data/geospatial_19/ucfajlg/fire/Angola/MOD09/*.hdf > /tmp/modis_files.txt
    fp = open('files/data/modis_files.txt','r')
    for line in fp.readlines():
        fname = line.split('/')[-1]
        fbits = fname.split('.')
        datebit = fbits[1]
        doy = int(datebit[-3:])
        if doy in date_range:
            print line
            break
    fp.close()

.. parsed-literal::

    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004214.h19v10.005.2010052095834.hdf
    


Now put in the part that writes it to a file:

.. code:: python

    ifile = 'files/data/modis_files.txt'
    ofile = 'files/data/some_modis_files.txt'
    
    ifp = open(ifile,'r')
    ofp = open(ofile,'w')
    for line in ifp.readlines():
        fname = line.split('/')[-1]
        fbits = fname.split('.')
        datebit = fbits[1]
        doy = int(datebit[-3:])
        if doy in date_range:
            ofp.write(line)
    ifp.close()
    ofp.close()
.. code:: python

    # or in a more compressed form
    
    ifile = 'files/data/modis_files.txt'
    ofile = 'files/data/some_modis_files.txt'
    
    ifp = open(ifile,'r')
    ofp = open(ofile,'w')
    for line in ifp.readlines():
        doy = int(line.split('/')[-1].split('.')[1][-3:])
        if doy in date_range:
            ofp.write(line)
    ifp.close()
    ofp.close()
check from unix:

.. code:: python

    !head -1 < files/data/some_modis_files.txt

.. parsed-literal::

    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004214.h19v10.005.2010052095834.hdf


.. code:: python

    !tail -1 < files/data/some_modis_files.txt

.. parsed-literal::

    /data/geospatial_19/ucfajlg/fire/Angola/MOD09/MOD09GA.A2004244.h19v10.005.2008256095130.hdf


Exercise 2.5
------------

We want to calculate the **maximum** monthly precipitation for regions
of the UK for all years in the 20th Century.

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
    
    
    # select years    
    c20_data = []
    for line in data:
        if (line[0] >= 1900) and (line[0] < 2000):
            c20_data.append(line[1:-1])
            
    # Aside: show which month that was
    month_names = [ "Jan", "Feb", "Mar", "Apr", \
        "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
    
    print "In South East England"
    for row in xrange(0,100,1):
        year = 1900 + row
        max_precip = max(c20_data[row])
        month = c20_data[row].index(max_precip)
    
        print "In the year",year,"the rainiest month was",month_names[month],"with",max_precip,"mm"

.. parsed-literal::

    In South East England
    In the year 1900 the rainiest month was Feb with 125.9 mm
    In the year 1901 the rainiest month was Dec with 98.7 mm
    In the year 1902 the rainiest month was Aug with 97.2 mm
    In the year 1903 the rainiest month was Oct with 188.4 mm
    In the year 1904 the rainiest month was Jan with 96.0 mm
    In the year 1905 the rainiest month was Jun with 104.5 mm
    In the year 1906 the rainiest month was Jan with 127.3 mm
    In the year 1907 the rainiest month was Oct with 129.5 mm
    In the year 1908 the rainiest month was Aug with 83.8 mm
    In the year 1909 the rainiest month was Oct with 143.9 mm
    In the year 1910 the rainiest month was Dec with 119.4 mm
    In the year 1911 the rainiest month was Dec with 153.6 mm
    In the year 1912 the rainiest month was Aug with 151.6 mm
    In the year 1913 the rainiest month was Oct with 106.5 mm
    In the year 1914 the rainiest month was Dec with 190.2 mm
    In the year 1915 the rainiest month was Dec with 163.9 mm
    In the year 1916 the rainiest month was Mar with 110.7 mm
    In the year 1917 the rainiest month was Aug with 135.1 mm
    In the year 1918 the rainiest month was Sep with 151.1 mm
    In the year 1919 the rainiest month was Dec with 121.4 mm
    In the year 1920 the rainiest month was Jul with 116.9 mm
    In the year 1921 the rainiest month was Jan with 70.8 mm
    In the year 1922 the rainiest month was Jul with 92.2 mm
    In the year 1923 the rainiest month was Oct with 142.5 mm
    In the year 1924 the rainiest month was Oct with 110.2 mm
    In the year 1925 the rainiest month was Jul with 98.1 mm
    In the year 1926 the rainiest month was Nov with 143.8 mm
    In the year 1927 the rainiest month was Sep with 138.5 mm
    In the year 1928 the rainiest month was Oct with 137.0 mm
    In the year 1929 the rainiest month was Nov with 175.6 mm
    In the year 1930 the rainiest month was Nov with 121.0 mm
    In the year 1931 the rainiest month was Aug with 101.3 mm
    In the year 1932 the rainiest month was Oct with 146.4 mm
    In the year 1933 the rainiest month was Mar with 74.1 mm
    In the year 1934 the rainiest month was Dec with 176.3 mm
    In the year 1935 the rainiest month was Nov with 148.2 mm
    In the year 1936 the rainiest month was Jan with 112.8 mm
    In the year 1937 the rainiest month was Jan with 124.9 mm
    In the year 1938 the rainiest month was Nov with 93.6 mm
    In the year 1939 the rainiest month was Oct with 154.0 mm
    In the year 1940 the rainiest month was Nov with 203.0 mm
    In the year 1941 the rainiest month was Aug with 117.3 mm
    In the year 1942 the rainiest month was Oct with 94.3 mm
    In the year 1943 the rainiest month was Jan with 130.2 mm
    In the year 1944 the rainiest month was Nov with 117.0 mm
    In the year 1945 the rainiest month was Jul with 103.8 mm
    In the year 1946 the rainiest month was Nov with 126.7 mm
    In the year 1947 the rainiest month was Mar with 150.7 mm
    In the year 1948 the rainiest month was Jan with 125.3 mm
    In the year 1949 the rainiest month was Oct with 189.3 mm
    In the year 1950 the rainiest month was Nov with 137.9 mm
    In the year 1951 the rainiest month was Nov with 161.9 mm
    In the year 1952 the rainiest month was Nov with 99.9 mm
    In the year 1953 the rainiest month was Jul with 87.5 mm
    In the year 1954 the rainiest month was Nov with 131.0 mm
    In the year 1955 the rainiest month was May with 110.5 mm
    In the year 1956 the rainiest month was Jan with 113.7 mm
    In the year 1957 the rainiest month was Feb with 97.7 mm
    In the year 1958 the rainiest month was Sep with 107.4 mm
    In the year 1959 the rainiest month was Dec with 143.4 mm
    In the year 1960 the rainiest month was Oct with 167.0 mm
    In the year 1961 the rainiest month was Dec with 102.0 mm
    In the year 1962 the rainiest month was Sep with 94.0 mm
    In the year 1963 the rainiest month was Nov with 141.0 mm
    In the year 1964 the rainiest month was Mar with 97.7 mm
    In the year 1965 the rainiest month was Dec with 126.9 mm
    In the year 1966 the rainiest month was Oct with 129.1 mm
    In the year 1967 the rainiest month was Oct with 126.6 mm
    In the year 1968 the rainiest month was Sep with 135.5 mm
    In the year 1969 the rainiest month was Nov with 108.4 mm
    In the year 1970 the rainiest month was Nov with 186.4 mm
    In the year 1971 the rainiest month was Jun with 134.4 mm
    In the year 1972 the rainiest month was Dec with 94.0 mm
    In the year 1973 the rainiest month was May with 76.6 mm
    In the year 1974 the rainiest month was Sep with 164.7 mm
    In the year 1975 the rainiest month was Sep with 122.8 mm
    In the year 1976 the rainiest month was Oct with 141.5 mm
    In the year 1977 the rainiest month was Aug with 132.8 mm
    In the year 1978 the rainiest month was Dec with 144.9 mm
    In the year 1979 the rainiest month was Dec with 122.6 mm
    In the year 1980 the rainiest month was Oct with 110.1 mm
    In the year 1981 the rainiest month was Mar with 131.2 mm
    In the year 1982 the rainiest month was Oct with 143.0 mm
    In the year 1983 the rainiest month was May with 98.5 mm
    In the year 1984 the rainiest month was Jan with 112.4 mm
    In the year 1985 the rainiest month was Dec with 103.7 mm
    In the year 1986 the rainiest month was Jan with 110.1 mm
    In the year 1987 the rainiest month was Oct with 198.7 mm
    In the year 1988 the rainiest month was Jan with 143.8 mm
    In the year 1989 the rainiest month was Dec with 143.8 mm
    In the year 1990 the rainiest month was Feb with 122.3 mm
    In the year 1991 the rainiest month was Jun with 102.0 mm
    In the year 1992 the rainiest month was Nov with 132.8 mm
    In the year 1993 the rainiest month was Dec with 133.9 mm
    In the year 1994 the rainiest month was Jan with 115.6 mm
    In the year 1995 the rainiest month was Jan with 143.1 mm
    In the year 1996 the rainiest month was Nov with 122.6 mm
    In the year 1997 the rainiest month was Jun with 100.6 mm
    In the year 1998 the rainiest month was Oct with 128.1 mm
    In the year 1999 the rainiest month was Dec with 109.5 mm


That is quite an achievement, given the limited amount of programming
you know so far.

If you go through this though, you will (should) see that it is really
not very efficient.

For example:

::

    we read all the data in and then filter out the years we want (what if the dataset were huge?)
    we loop over the 100 years multiple times
    we store intermediate results

For this exercise, you should look through the code we developed and try
to make it more efficient.

Efficiency should not override clarity and understanding though, so make
sure you can understand what is going on at each stage.

Answer 2.5
----------

.. code:: python

    # specify filename
    filename = 'files/data/HadSEEP_monthly_qc.txt'
    
    fp = open(filename,'r')
    
    # years range
    years = range(1900,2000)
    
    # set up list to store data in
    c20_data = []
    
    # loop over each line
    for line_data in fp.readlines()[4:]:
        # split on white space
        # convert data to float
        year_data = [float(i) for i in line_data.split()] 
        
        if year_data[0] in years:
            c20_data.append(year_data)
            
    # Aside: show which month that was
    month_names = [ "Jan", "Feb", "Mar", "Apr", \
        "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
    
    print "In South East England"
    for row,year in enumerate(years):
        max_precip = max(c20_data[row])
        month = c20_data[row].index(max_precip)
    
        print "In the year",year,"the rainiest month was",month_names[month],"with",max_precip,"mm"
        
    fp.close()


.. parsed-literal::

    In South East England
    In the year 1900 the rainiest month was Jan with 1900.0 mm
    In the year 1901 the rainiest month was Jan with 1901.0 mm
    In the year 1902 the rainiest month was Jan with 1902.0 mm
    In the year 1903 the rainiest month was Jan with 1903.0 mm
    In the year 1904 the rainiest month was Jan with 1904.0 mm
    In the year 1905 the rainiest month was Jan with 1905.0 mm
    In the year 1906 the rainiest month was Jan with 1906.0 mm
    In the year 1907 the rainiest month was Jan with 1907.0 mm
    In the year 1908 the rainiest month was Jan with 1908.0 mm
    In the year 1909 the rainiest month was Jan with 1909.0 mm
    In the year 1910 the rainiest month was Jan with 1910.0 mm
    In the year 1911 the rainiest month was Jan with 1911.0 mm
    In the year 1912 the rainiest month was Jan with 1912.0 mm
    In the year 1913 the rainiest month was Jan with 1913.0 mm
    In the year 1914 the rainiest month was Jan with 1914.0 mm
    In the year 1915 the rainiest month was Jan with 1915.0 mm
    In the year 1916 the rainiest month was Jan with 1916.0 mm
    In the year 1917 the rainiest month was Jan with 1917.0 mm
    In the year 1918 the rainiest month was Jan with 1918.0 mm
    In the year 1919 the rainiest month was Jan with 1919.0 mm
    In the year 1920 the rainiest month was Jan with 1920.0 mm
    In the year 1921 the rainiest month was Jan with 1921.0 mm
    In the year 1922 the rainiest month was Jan with 1922.0 mm
    In the year 1923 the rainiest month was Jan with 1923.0 mm
    In the year 1924 the rainiest month was Jan with 1924.0 mm
    In the year 1925 the rainiest month was Jan with 1925.0 mm
    In the year 1926 the rainiest month was Jan with 1926.0 mm
    In the year 1927 the rainiest month was Jan with 1927.0 mm
    In the year 1928 the rainiest month was Jan with 1928.0 mm
    In the year 1929 the rainiest month was Jan with 1929.0 mm
    In the year 1930 the rainiest month was Jan with 1930.0 mm
    In the year 1931 the rainiest month was Jan with 1931.0 mm
    In the year 1932 the rainiest month was Jan with 1932.0 mm
    In the year 1933 the rainiest month was Jan with 1933.0 mm
    In the year 1934 the rainiest month was Jan with 1934.0 mm
    In the year 1935 the rainiest month was Jan with 1935.0 mm
    In the year 1936 the rainiest month was Jan with 1936.0 mm
    In the year 1937 the rainiest month was Jan with 1937.0 mm
    In the year 1938 the rainiest month was Jan with 1938.0 mm
    In the year 1939 the rainiest month was Jan with 1939.0 mm
    In the year 1940 the rainiest month was Jan with 1940.0 mm
    In the year 1941 the rainiest month was Jan with 1941.0 mm
    In the year 1942 the rainiest month was Jan with 1942.0 mm
    In the year 1943 the rainiest month was Jan with 1943.0 mm
    In the year 1944 the rainiest month was Jan with 1944.0 mm
    In the year 1945 the rainiest month was Jan with 1945.0 mm
    In the year 1946 the rainiest month was Jan with 1946.0 mm
    In the year 1947 the rainiest month was Jan with 1947.0 mm
    In the year 1948 the rainiest month was Jan with 1948.0 mm
    In the year 1949 the rainiest month was Jan with 1949.0 mm
    In the year 1950 the rainiest month was Jan with 1950.0 mm
    In the year 1951 the rainiest month was Jan with 1951.0 mm
    In the year 1952 the rainiest month was Jan with 1952.0 mm
    In the year 1953 the rainiest month was Jan with 1953.0 mm
    In the year 1954 the rainiest month was Jan with 1954.0 mm
    In the year 1955 the rainiest month was Jan with 1955.0 mm
    In the year 1956 the rainiest month was Jan with 1956.0 mm
    In the year 1957 the rainiest month was Jan with 1957.0 mm
    In the year 1958 the rainiest month was Jan with 1958.0 mm
    In the year 1959 the rainiest month was Jan with 1959.0 mm
    In the year 1960 the rainiest month was Jan with 1960.0 mm
    In the year 1961 the rainiest month was Jan with 1961.0 mm
    In the year 1962 the rainiest month was Jan with 1962.0 mm
    In the year 1963 the rainiest month was Jan with 1963.0 mm
    In the year 1964 the rainiest month was Jan with 1964.0 mm
    In the year 1965 the rainiest month was Jan with 1965.0 mm
    In the year 1966 the rainiest month was Jan with 1966.0 mm
    In the year 1967 the rainiest month was Jan with 1967.0 mm
    In the year 1968 the rainiest month was Jan with 1968.0 mm
    In the year 1969 the rainiest month was Jan with 1969.0 mm
    In the year 1970 the rainiest month was Jan with 1970.0 mm
    In the year 1971 the rainiest month was Jan with 1971.0 mm
    In the year 1972 the rainiest month was Jan with 1972.0 mm
    In the year 1973 the rainiest month was Jan with 1973.0 mm
    In the year 1974 the rainiest month was Jan with 1974.0 mm
    In the year 1975 the rainiest month was Jan with 1975.0 mm
    In the year 1976 the rainiest month was Jan with 1976.0 mm
    In the year 1977 the rainiest month was Jan with 1977.0 mm
    In the year 1978 the rainiest month was Jan with 1978.0 mm
    In the year 1979 the rainiest month was Jan with 1979.0 mm
    In the year 1980 the rainiest month was Jan with 1980.0 mm
    In the year 1981 the rainiest month was Jan with 1981.0 mm
    In the year 1982 the rainiest month was Jan with 1982.0 mm
    In the year 1983 the rainiest month was Jan with 1983.0 mm
    In the year 1984 the rainiest month was Jan with 1984.0 mm
    In the year 1985 the rainiest month was Jan with 1985.0 mm
    In the year 1986 the rainiest month was Jan with 1986.0 mm
    In the year 1987 the rainiest month was Jan with 1987.0 mm
    In the year 1988 the rainiest month was Jan with 1988.0 mm
    In the year 1989 the rainiest month was Jan with 1989.0 mm
    In the year 1990 the rainiest month was Jan with 1990.0 mm
    In the year 1991 the rainiest month was Jan with 1991.0 mm
    In the year 1992 the rainiest month was Jan with 1992.0 mm
    In the year 1993 the rainiest month was Jan with 1993.0 mm
    In the year 1994 the rainiest month was Jan with 1994.0 mm
    In the year 1995 the rainiest month was Jan with 1995.0 mm
    In the year 1996 the rainiest month was Jan with 1996.0 mm
    In the year 1997 the rainiest month was Jan with 1997.0 mm
    In the year 1998 the rainiest month was Jan with 1998.0 mm
    In the year 1999 the rainiest month was Jan with 1999.0 mm


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

Answer 2.6
----------

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

.. code:: python

    !wget -O files/data/heathrowdata.txt http://www.metoffice.gov.uk/climate/uk/stationdata/heathrowdata.txt

.. parsed-literal::

    --2014-09-30 11:13:08--  http://www.metoffice.gov.uk/climate/uk/stationdata/heathrowdata.txt
    Resolving www.metoffice.gov.uk... 213.120.162.233, 213.120.162.211
    Connecting to www.metoffice.gov.uk|213.120.162.233|:80... connected.
    HTTP request sent, awaiting response... 301 Moved Permanently
    Location: http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt [following]
    --2014-09-30 11:13:08--  http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt
    Reusing existing connection to www.metoffice.gov.uk:80.
    HTTP request sent, awaiting response... 200 OK
    Length: 41280 (40K) [text/plain]
    Saving to: ‘files/data/heathrowdata.txt’
    
    100%[======================================>] 41,280      --.-K/s   in 0s      
    
    2014-09-30 11:13:09 (206 MB/s) - ‘files/data/heathrowdata.txt’ saved [41280/41280]
    


.. code:: python

    ifile = 'files/data/heathrowdata.txt'
    fp = open(ifile)
    raw_data = fp.readlines()
    fp.close()
    
    raw_data = raw_data[7:] # Skip headers
.. code:: python

    # set up the problem
    start_year = 1960
    end_year = 1990
    
    tmax = []
    
    for l in raw_data:
        s = l.split()
        year = int( s[0] )
        if year >= start_year and year < end_year:
            month = int ( s[1] )
            if month == 1:
                tmax.append([])
            tmax[-1].append(float ( s[2] ))
    
    for l in tmax:
        print l

.. parsed-literal::

    [6.9, 7.9, 10.2, 14.3, 18.4, 22.1, 20.1, 20.3, 18.5, 14.2, 11.2, 6.9]
    [6.9, 10.3, 13.9, 15.0, 16.8, 21.7, 22.1, 21.7, 20.9, 15.6, 9.9, 6.8]
    [7.9, 7.6, 7.4, 12.7, 15.0, 20.4, 20.6, 20.0, 17.8, 15.7, 9.1, 5.0]
    [0.8, 2.8, 10.7, 13.6, 16.0, 20.8, 21.1, 19.8, 18.0, 14.8, 11.8, 5.4]
    [5.8, 7.6, 7.6, 12.8, 19.6, 19.3, 22.8, 22.3, 21.1, 13.7, 11.2, 7.1]
    [6.6, 5.9, 10.5, 13.4, 16.8, 19.7, 19.3, 20.8, 17.4, 16.2, 8.4, 8.4]
    [5.3, 9.3, 10.9, 12.2, 17.0, 21.8, 20.1, 20.6, 19.6, 14.7, 8.8, 9.3]
    [7.3, 9.3, 11.6, 12.5, 15.6, 20.1, 23.5, 21.5, 18.5, 15.0, 9.7, 7.2]
    [7.2, 5.7, 11.1, 13.7, 15.4, 20.6, 20.7, 20.2, 18.8, 16.5, 9.5, 5.4]
    [8.9, 4.9, 8.0, 13.6, 17.1, 20.6, 23.9, 21.8, 19.6, 18.2, 9.6, 6.1]
    [7.1, 7.2, 8.1, 11.4, 19.2, 23.6, 21.3, 22.3, 20.3, 15.7, 11.9, 7.0]
    [7.8, 8.6, 9.1, 12.2, 18.1, 17.8, 24.1, 21.3, 20.7, 17.2, 10.4, 9.3]
    [6.9, 7.9, 12.4, 12.9, 16.0, 17.5, 22.3, 21.8, 17.3, 15.6, 9.9, 9.4]
    [7.3, 8.1, 11.5, 12.5, 16.9, 21.9, 21.4, 23.7, 20.7, 13.9, 10.3, 8.6]
    [9.6, 9.2, 10.3, 14.0, 17.0, 20.1, 20.9, 21.5, 17.5, 11.0, 10.6, 11.0]
    [10.3, 9.3, 8.4, 13.3, 15.1, 21.8, 24.1, 25.9, 19.5, 14.4, 10.1, 7.6]
    [8.8, 7.8, 9.5, 13.7, 19.3, 25.5, 26.6, 25.1, 19.0, 14.9, 9.9, 5.6]
    [6.1, 9.6, 11.2, 12.2, 16.4, 17.4, 22.4, 20.3, 18.0, 16.3, 10.4, 9.2]
    [6.7, 6.2, 11.3, 10.7, 17.2, 19.7, 20.5, 20.7, 20.1, 17.1, 12.6, 7.8]
    [3.8, 4.5, 9.2, 12.7, 15.9, 19.0, 22.5, 21.0, 19.6, 16.4, 10.8, 9.2]
    [6.0, 9.9, 9.0, 14.0, 17.3, 19.8, 19.7, 21.9, 20.1, 14.0, 9.3, 8.9]
    [8.1, 7.1, 11.8, 12.9, 16.1, 18.5, 22.0, 22.8, 20.3, 12.9, 11.5, 4.4]
    [6.9, 8.4, 11.1, 14.3, 18.0, 21.5, 22.7, 22.2, 20.8, 14.1, 11.4, 8.2]
    [10.0, 5.5, 10.8, 12.4, 15.6, 20.8, 27.6, 24.5, 19.3, 15.1, 11.3, 9.2]
    [8.0, 7.4, 8.9, 14.6, 14.9, 21.3, 24.2, 24.4, 18.6, 15.8, 12.2, 8.7]
    [4.1, 6.3, 9.4, 14.0, 16.4, 18.5, 22.9, 20.3, 20.6, 16.1, 8.1, 10.0]
    [7.2, 1.7, 10.1, 10.9, 16.3, 21.8, 22.6, 20.0, 17.4, 16.4, 12.1, 9.7]
    [3.6, 7.7, 8.5, 15.8, 16.3, 18.6, 21.8, 21.8, 19.3, 15.0, 9.8, 8.9]
    [8.8, 8.7, 10.7, 13.5, 18.0, 19.7, 20.0, 21.8, 18.8, 15.5, 9.9, 10.4]
    [9.5, 10.2, 12.9, 11.5, 21.0, 22.1, 25.8, 24.2, 20.7, 17.1, 10.9, 9.4]


.. code:: python

    monthly_avg = []
    n_years = len(tmax)
    
    
    for month in xrange ( len(tmax[0]) ):
        temp = 0.
        for year in xrange (n_years):
            temp += tmax[year][month]
        monthly_avg.append(temp/n_years)

.. code:: python

    print "T results for",n_years,"years:",start_year,"to",end_year
    
    month_names = [ "Jan", "Feb", "Mar", "Apr", \
        "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
    
    print "\n\tMonth\tTmaxAvg\n"
    for i, mname in enumerate ( month_names ):
        print '\t',mname,'\t',monthly_avg[i]

.. parsed-literal::

    T results for 30 years: 1960 to 1990
    
    	Month	TmaxAvg
    
    	Jan 	7.00666666667
    	Feb 	7.42
    	Mar 	10.2033333333
    	Apr 	13.11
    	May 	16.9566666667
    	Jun 	20.4666666667
    	Jul 	22.32
    	Aug 	21.8833333333
    	Sep 	19.2933333333
    	Oct 	15.3033333333
    	Nov 	10.42
    	Dec 	8.00333333333


Exercise 2.7
------------

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
    


**You should modify the example above to make it simpler, if you can
spot any places for that (don't make it more complicated!).**

**You should then modify it so that the list of files that we want to
process is printed to a file.**

Answer 2.7
----------

Probably the main place you could make the code simpler would be in the
loop:

.. code:: python

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

Really, we don't need the ``count`` variable and structure in here, and
we could replace this by:

.. code:: python

        # 3a. Read the file list
        fp = open(sub_dict['file_list'],'r')
        
        # 3b. find the doy range
        doy_range = range(int(sub_dict['doy_start']),\
                              int(sub_dict['doy_end']))
        
        # 3c. loop over each file read from
        #     sub_dict['file_list']
        for this_file in fp.readlines():
        
            # 3d. extract doy from the file name
            doy = int(this_file.split('.')[1][-3:])
            
            # 3e. see if doy is in the range we want?
            if doy in doy_range:
            
                # 3f. store the filename in the list
                wanted_files.append("%s/%s"%(sub_dict['dir'],this_file))

        # close the file here now
        fp.close()

If you wanted, you could also do some clever things with ``and``:

.. code:: python

        # 3a. Read the file list
        fp = open(sub_dict['file_list'],'r')
        
        # 3b. find the doy range
        doy_range = range(int(sub_dict['doy_start']),\
                              int(sub_dict['doy_end']))
        
        # 3c. loop over each file read from
        #     sub_dict['file_list']
        for this_file in fp.readlines():
        
            # 3d. extract doy from the file name
            doy = int(this_file.split('.')[1][-3:])
            
            # 3e. see if doy is in the range we want
            # and put in list if so
            doy in doy_range and \
                wanted_files.append("%s/%s"%(sub_dict['dir'],this_file))

        # close the file here now
        fp.close()

Writing the results to file should be straightforward enough for you
now.

You could do it at the end:

.. code:: python

    # 1. Read the configuration file
    # into the dict modis
    import ConfigParser
    
    # good to open the file early on
    # in case it fails
    ofile = 'files/data/modis_files.dat'
    ofp = open(ofile,"w")
    
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
        
        # 3b. find the doy range
        doy_range = range(int(sub_dict['doy_start']),\
                              int(sub_dict['doy_end']))
        
        # 3c. loop over each file read from
        #     sub_dict['file_list']
        for this_file in fp.readlines():
        
            # 3d. extract doy from the file name
            doy = int(this_file.split('.')[1][-3:])
            # 3e. see if doy is in the range we want
            # and put in list if so
            doy in doy_range and \
                wanted_files.append("%s/%s"%(sub_dict['dir'],this_file))
        fp.close()
                
    print "I found %d files to process"%len(wanted_files)
    
    ofp.writelines(wanted_files)
    ofp.close()


.. parsed-literal::

    I found 62 files to process


.. code:: python

    !head -10 < files/data/modis_files.dat

.. parsed-literal::

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


Or you could print as you go along in the loop:

.. code:: python

    # 1. Read the configuration file
    # into the dict modis
    import ConfigParser
    
    # good to open the file early on
    # in case it fails
    ofile = 'files/data/modis_files.dat'
    ofp = open(ofile,"w")
    
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
        
        # 3b. find the doy range
        doy_range = range(int(sub_dict['doy_start']),\
                              int(sub_dict['doy_end']))
        
        # 3c. loop over each file read from
        #     sub_dict['file_list']
        for this_file in fp.readlines():
        
            # 3d. extract doy from the file name
            # 3e. see if doy is in the range we want
            # and put in list if so
            (int(this_file.split('.')[1][-3:]) in doy_range) and \
                    ofp.write("%s/%s"%(sub_dict['dir'],this_file))
        fp.close()
                
    ofp.close()

.. code:: python

    !head -10 < files/data/modis_files.dat

.. parsed-literal::

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

