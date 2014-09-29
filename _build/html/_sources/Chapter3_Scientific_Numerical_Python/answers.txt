
E3 Answers to Exercise
======================

E3.2 Exercise: listing
----------------------

**Using Python, produce a listing of the files in the subdirectory
``data`` of ``geogg122/Chapter3_Scientific_Numerical_Python`` that end
with ``.nc`` and put this listing in a file called
``files/data/data.dat`` with each entry on a different line**

A3.2 Answer: listing
--------------------

Hopefully, you should already be in the directory
``geogg122/Chapter3_Scientific_Numerical_Python``, if not, you may like
to go there before starting this exercise.

If you were to do this from unix, you would getr the listing with:

.. code:: python

    !ls -l data/*.nc

.. parsed-literal::

    -rw-r--r--  1 plewis  staff  115202868 11 Oct 09:53 data/GlobAlbedo.1998145.h17v03.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:07 data/GlobAlbedo.200901.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:07 data/GlobAlbedo.200902.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200903.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200904.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200905.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200906.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18758652 11 Oct 20:08 data/GlobAlbedo.200907.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200908.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200909.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200910.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200911.mosaic.5.nc
    -rw-r--r--  1 plewis  staff   18669672 11 Oct 20:08 data/GlobAlbedo.200912.mosaic.5.nc


or similar.

To do this in Python, you should use ``glob``, and the same 'pattern':

.. code:: python

    import glob
    
    files = glob.glob('data/*.nc')
    print files

.. parsed-literal::

    ['data/GlobAlbedo.1998145.h17v03.nc', 'data/GlobAlbedo.200901.mosaic.5.nc', 'data/GlobAlbedo.200902.mosaic.5.nc', 'data/GlobAlbedo.200903.mosaic.5.nc', 'data/GlobAlbedo.200904.mosaic.5.nc', 'data/GlobAlbedo.200905.mosaic.5.nc', 'data/GlobAlbedo.200906.mosaic.5.nc', 'data/GlobAlbedo.200907.mosaic.5.nc', 'data/GlobAlbedo.200908.mosaic.5.nc', 'data/GlobAlbedo.200909.mosaic.5.nc', 'data/GlobAlbedo.200910.mosaic.5.nc', 'data/GlobAlbedo.200911.mosaic.5.nc', 'data/GlobAlbedo.200912.mosaic.5.nc']


This is a list. We want to write this to a file called
``files/data/data.dat``.

First we open it, then simply use ``writelines`` to write the list of
strings, the close the file.

.. code:: python

    filename = 'files/data/data.dat'
    
    # open in write mode
    fp = open(filename,'w')
    fp.writelines(files)
    fp.close()
Hopefully, that all worked well, but just to check from unix:

.. code:: python

    !cat files/data/data.dat

.. parsed-literal::

    data/GlobAlbedo.1998145.h17v03.ncdata/GlobAlbedo.200901.mosaic.5.ncdata/GlobAlbedo.200902.mosaic.5.ncdata/GlobAlbedo.200903.mosaic.5.ncdata/GlobAlbedo.200904.mosaic.5.ncdata/GlobAlbedo.200905.mosaic.5.ncdata/GlobAlbedo.200906.mosaic.5.ncdata/GlobAlbedo.200907.mosaic.5.ncdata/GlobAlbedo.200908.mosaic.5.ncdata/GlobAlbedo.200909.mosaic.5.ncdata/GlobAlbedo.200910.mosaic.5.ncdata/GlobAlbedo.200911.mosaic.5.ncdata/GlobAlbedo.200912.mosaic.5.nc

which isn't quite what we wanted: we need to insert a newline character
at the end of each string before writing.

There are several ways to do this, e.g.:

.. code:: python

    files = glob.glob('data/*.nc')
    
    for i,file in enumerate(files):
        files[i] = file + '\n'
    print files

.. parsed-literal::

    ['data/GlobAlbedo.1998145.h17v03.nc\n', 'data/GlobAlbedo.200901.mosaic.5.nc\n', 'data/GlobAlbedo.200902.mosaic.5.nc\n', 'data/GlobAlbedo.200903.mosaic.5.nc\n', 'data/GlobAlbedo.200904.mosaic.5.nc\n', 'data/GlobAlbedo.200905.mosaic.5.nc\n', 'data/GlobAlbedo.200906.mosaic.5.nc\n', 'data/GlobAlbedo.200907.mosaic.5.nc\n', 'data/GlobAlbedo.200908.mosaic.5.nc\n', 'data/GlobAlbedo.200909.mosaic.5.nc\n', 'data/GlobAlbedo.200910.mosaic.5.nc\n', 'data/GlobAlbedo.200911.mosaic.5.nc\n', 'data/GlobAlbedo.200912.mosaic.5.nc\n']


.. code:: python

    files = glob.glob('data/*.nc')
    
    # or:
    files = [file + '\n' for file in files]
    
    print files

.. parsed-literal::

    ['data/GlobAlbedo.1998145.h17v03.nc\n', 'data/GlobAlbedo.200901.mosaic.5.nc\n', 'data/GlobAlbedo.200902.mosaic.5.nc\n', 'data/GlobAlbedo.200903.mosaic.5.nc\n', 'data/GlobAlbedo.200904.mosaic.5.nc\n', 'data/GlobAlbedo.200905.mosaic.5.nc\n', 'data/GlobAlbedo.200906.mosaic.5.nc\n', 'data/GlobAlbedo.200907.mosaic.5.nc\n', 'data/GlobAlbedo.200908.mosaic.5.nc\n', 'data/GlobAlbedo.200909.mosaic.5.nc\n', 'data/GlobAlbedo.200910.mosaic.5.nc\n', 'data/GlobAlbedo.200911.mosaic.5.nc\n', 'data/GlobAlbedo.200912.mosaic.5.nc\n']


.. code:: python

    # or all at once if you like:
    
    files = [file + '\n' for file in glob.glob('data/*.nc')]
    
    print files

.. parsed-literal::

    ['data/GlobAlbedo.1998145.h17v03.nc\n', 'data/GlobAlbedo.200901.mosaic.5.nc\n', 'data/GlobAlbedo.200902.mosaic.5.nc\n', 'data/GlobAlbedo.200903.mosaic.5.nc\n', 'data/GlobAlbedo.200904.mosaic.5.nc\n', 'data/GlobAlbedo.200905.mosaic.5.nc\n', 'data/GlobAlbedo.200906.mosaic.5.nc\n', 'data/GlobAlbedo.200907.mosaic.5.nc\n', 'data/GlobAlbedo.200908.mosaic.5.nc\n', 'data/GlobAlbedo.200909.mosaic.5.nc\n', 'data/GlobAlbedo.200910.mosaic.5.nc\n', 'data/GlobAlbedo.200911.mosaic.5.nc\n', 'data/GlobAlbedo.200912.mosaic.5.nc\n']


or several other ways ...

Putting this together:

.. code:: python

    import glob
    
    files = [file + '\n' for file in glob.glob('data/*.nc')]
    
    filename = 'files/data/data.dat'
    
    # open in write mode
    fp = open(filename,'w')
    fp.writelines(files)
    fp.close()
then checking:

.. code:: python

    !cat files/data/data.dat

.. parsed-literal::

    data/GlobAlbedo.1998145.h17v03.nc
    data/GlobAlbedo.200901.mosaic.5.nc
    data/GlobAlbedo.200902.mosaic.5.nc
    data/GlobAlbedo.200903.mosaic.5.nc
    data/GlobAlbedo.200904.mosaic.5.nc
    data/GlobAlbedo.200905.mosaic.5.nc
    data/GlobAlbedo.200906.mosaic.5.nc
    data/GlobAlbedo.200907.mosaic.5.nc
    data/GlobAlbedo.200908.mosaic.5.nc
    data/GlobAlbedo.200909.mosaic.5.nc
    data/GlobAlbedo.200910.mosaic.5.nc
    data/GlobAlbedo.200911.mosaic.5.nc
    data/GlobAlbedo.200912.mosaic.5.nc


which *is* what we wanted.

E3.2 Exercise: Making Movies
----------------------------

E3.2.1 Software
~~~~~~~~~~~~~~~

You can *sort of* make `movies in
pylab <http://matplotlib.org/faq/howto_faq.html#make-a-movie>`__, but
you generally have to make a system call to unix at some point, so it's
probably easier to do this all in unix with the utility
```convert`` <http://www.imagemagick.org/script/convert.php>`__.

At the unix prompt, chack that you have access to convert:

.. code:: bash

    berlin% which convert
    /usr/bin/convert

If this doesn't come up with anything useful, there is probably a
version in ``/usr/bin/convert`` or ``/usr/local/bin/convert`` (If you
don't have it on your local machine, install
```ImageMagick`` <http://www.imagemagick.org/script/index.php>`__ which
contains the command line tool ``convert``).

To use this, e.g.:

from the unix command line:

.. code:: bash

    berlin% cd ~/Data/geogg122/Chapter3_Scientific_Numerical_Python  
    berlin% convert files/data/albedo.jpg files/data/albedo.gif  

or from within a notebook:

.. code:: python

    !convert files/data/albedo.jpg files/data/albedo.gif
Or, more practically here, you can run a unix command directly from
Python:

.. code:: python

    import os
    cmd = 'convert files/data/albedo.jpg files/data/albedo.gif'
    os.system(cmd)



.. parsed-literal::

    0



This will convert the file ``files/data/albedo.jpg`` (in jpeg format) to
``files/data/albedo.gif`` (in gif format).

.. figure:: files/data/albedo.gif
   :alt: albedo

   albedo

We can also use ``convert`` to make animated gifs, which is one way of
making a movie.

E3.2.2 Looping over a set of images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have all of the code you need above to be able to read a GlobAlbedo
file for a given month and waveband in Python and save a picture in jpeg
format, but to recap for ``BHR_VIS``:

.. code:: python

    from netCDF4 import Dataset
    import pylab as plt
    import os
    
    root = 'files/data/'
    
    month_list = ['January','February','March','April','May','June',\
                  'July','August','September','October','November','December']
    # make a dictionary from 2 lists
    month_dict = dict(zip(range(1,13),month_list))
    
    # example filename : use formatting string:
    # %d%02d
    year = 2009
    
    
    # set the month
    month = 1
    
    ''' Read the data '''
    local_file = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
    # load the netCDF data from the file f.filename
    nc = Dataset(local_file,'r')
    band = nc.variables['DHR_VIS']
    
    ''' Plot the data and save as picture jpeg format '''
    # make a string with the output file name
    out_file = root + 'GlobAlbedo.%d%02d.jpg'%(year,month)
    # plot
    plt.figure(figsize=(10, 5))
    plt.clf()
    # %9s forces the string to be 9 characters long
    plt.title('VIS BHR albedo for %9s %d'%(month_dict[month],year))
    # use nearest neighbour interpolation
    plt.imshow(band,interpolation='nearest',cmap=plt.get_cmap('Spectral'),vmin=0.0,vmax=1.0)
    # show a colour bar 
    plt.colorbar()
    plt.savefig(out_file)
    
    ''' Convert the file to gif '''
    # set up the unix command which is of the form 
    # convert input output
    # Here input will be out_file
    # and output we can get with out_file.replace('.jpg','.gif')
    # i.e. replacing where it says .jpg with .gif
    cmd = 'convert %s %s'%(out_file,out_file.replace('.jpg','.gif'))
    os.system(cmd)



.. parsed-literal::

    0




.. image:: answers_files/answers_32_1.png


**Modify the code above to loop over each month, so that it generates a
set of gif format files for the TOTAL SHORTWAVE ALBEDO**

You should confirm that these exist, and that the file modification time
is when you ran it (not when I generated the files for these notes,
which is Oct 10 2013).

.. code:: python

    ls -l files/data/GlobAlbedo*gif

.. parsed-literal::

    -rw-r--r--  1 plewis  staff  340658 11 Oct 20:00 files/data/GlobAlbedo.2009.SW.1.gif
    -rw-r--r--  1 plewis  staff  340658 11 Oct 19:59 files/data/GlobAlbedo.2009.SW.gif
    -rw-r--r--  1 plewis  staff   55299 11 Oct 20:21 files/data/GlobAlbedo.200901.gif
    -rw-r--r--  1 plewis  staff   28139 11 Oct 19:59 files/data/GlobAlbedo.200902.gif
    -rw-r--r--  1 plewis  staff   28259 11 Oct 19:59 files/data/GlobAlbedo.200903.gif
    -rw-r--r--  1 plewis  staff   28249 11 Oct 19:59 files/data/GlobAlbedo.200904.gif
    -rw-r--r--  1 plewis  staff   28468 11 Oct 19:59 files/data/GlobAlbedo.200905.gif
    -rw-r--r--  1 plewis  staff   28672 11 Oct 19:59 files/data/GlobAlbedo.200906.gif
    -rw-r--r--  1 plewis  staff   28656 11 Oct 19:59 files/data/GlobAlbedo.200907.gif
    -rw-r--r--  1 plewis  staff   28275 11 Oct 19:59 files/data/GlobAlbedo.200908.gif
    -rw-r--r--  1 plewis  staff   28952 11 Oct 19:59 files/data/GlobAlbedo.200909.gif
    -rw-r--r--  1 plewis  staff   28450 11 Oct 19:59 files/data/GlobAlbedo.200910.gif
    -rw-r--r--  1 plewis  staff   28570 11 Oct 19:59 files/data/GlobAlbedo.200911.gif
    -rw-r--r--  1 plewis  staff   28438 11 Oct 19:59 files/data/GlobAlbedo.200912.gif


A3.2.2 Answer: Looping over a set of images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Really all you need to do here is to make ``month`` appear in a loop,
e.g. using:

``for month in range(1,13):``

and then make sure that all of the code below is in that loop (i.e.
indented) as below.

One additional thing is to make sure you select the waveband you were
supposed to (shortwave albedo)

``band = nc.variables['DHR_SW']``

and finally, make sure you change the title:

You should *also* however, go through the code above line by line,
making sure you appreciate what is going on at each stage and why we
have done these things (in this oroder).

.. code:: python

    from netCDF4 import Dataset
    import pylab as plt
    import os
    
    root = 'files/data/'
    
    month_list = ['January','February','March','April','May','June',\
                  'July','August','September','October','November','December']
    # make a dictionary from 2 lists
    month_dict = dict(zip(range(1,13),month_list))
    
    # example filename : use formatting string:
    # %d%02d
    year = 2009
    
    
    # set the month
    for month in range(1,13):
        ''' Read the data '''
        local_file = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
        # load the netCDF data from the file f.filename
        nc = Dataset(local_file,'r')
        # select which band we want
        band = nc.variables['DHR_SW']
        
        ''' Plot the data and save as picture jpeg format '''
        # make a string with the output file name
        out_file = root + 'GlobAlbedo.%d%02d.jpg'%(year,month)
        # plot
        plt.figure()
        plt.clf()
        # %9s forces the string to be 9 characters long
        plt.title('SW BHR albedo for %9s %d'%(month_dict[month],year))
        # use nearest neighbour interpolation
        plt.imshow(band,interpolation='nearest',cmap=plt.get_cmap('Spectral'),vmin=0.0,vmax=1.0)
        # show a colour bar 
        plt.colorbar()
        plt.savefig(out_file)
        
        ''' Convert the file to gif '''
        # set up the unix command which is of the form 
        # convert input output
        # Here input will be out_file
        # and output we can get with out_file.replace('.jpg','.gif')
        # i.e. replacing where it says .jpg with .gif
        cmd = 'convert %s %s'%(out_file,out_file.replace('.jpg','.gif'))
        os.system(cmd)


.. image:: answers_files/answers_37_0.png



.. image:: answers_files/answers_37_1.png



.. image:: answers_files/answers_37_2.png



.. image:: answers_files/answers_37_3.png



.. image:: answers_files/answers_37_4.png



.. image:: answers_files/answers_37_5.png



.. image:: answers_files/answers_37_6.png



.. image:: answers_files/answers_37_7.png



.. image:: answers_files/answers_37_8.png



.. image:: answers_files/answers_37_9.png



.. image:: answers_files/answers_37_10.png



.. image:: answers_files/answers_37_11.png


E3.2.3 Make the movie
~~~~~~~~~~~~~~~~~~~~~

The unix command to convert these files to an animated gif is:

.. code:: bash

    convert -delay 100 -loop 0 files/data/GlobAlbedo.2009??.gif files/data/GlobAlbedo.2009.SW.gif

**Run this (ideally, from within Python) to create the animated gif
GlobAlbedo.2009.SW.gif**

Again, confirm that *you* created this file (and it is not just a
version you downloaded):

.. code:: python

    ls -l files/data/GlobAlbedo.2009.SW.gif

.. parsed-literal::

    -rw-r--r--  1 plewis  staff  340658 11 Oct 19:59 files/data/GlobAlbedo.2009.SW.gif


A3.2.3 Answer: Make the movie
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You could just type the command at the unix prompt ... but to do it
using a ``system`` call from within Python, e.g.:

.. code:: python

    import os
    
    # this is quite a neat way of generating the string for the input files
    out_file = 'files/data/GlobAlbedo.%d.SW.1.gif'%year
    in_files = out_file.replace('.SW.1.gif','??.gif')
    
    cmd = 'convert -delay 100 -loop 0 %s %s'%(in_files,out_file)
    # check the cmd is ok
    print cmd

.. parsed-literal::

    convert -delay 100 -loop 0 files/data/GlobAlbedo.2009??.gif files/data/GlobAlbedo.2009.SW.1.gif


.. code:: python

    # good ... so now run it
    os.system(cmd)



.. parsed-literal::

    0



.. figure:: files/data/GlobAlbedo.2009.SW.1.gif
   :alt: 

To view the animated gif you have generated, open it in a browser.

E3.3 Exercise: 3D Masked Array
------------------------------

.. code:: python

    from netCDF4 import Dataset
    import numpy as np
    
    root = 'files/data/'
    year = 2009
    
    # which months?
    months = xrange(1,13)
    
    # empty list
    data = []
    
    # loop over month
    # use enumerate so we have an index counter
    for i,month in enumerate(months):
        # this then is the file we want
        local_file = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
        
        # load the netCDF data from the file local_file
        nc = Dataset(local_file,'r')
        # append what we read to the list called data
        data.append(np.array(nc.variables['DHR_SW']))
        
    # convert data to a numpy array (its a list of arrays at the moment)
    data = np.array(data)
N.B. Do this exercise before proceeding to the next section.

**Taking the code above as a starting point, generate a masked array of
the GlobAlbedo dataset for the year 2009.**

A3.3 Answer: 3D Masked Array
----------------------------

To recap, to make a masked array, we use some code such as:

.. code:: python

    import numpy.ma as ma
    
    band = np.array(nc.variables['DHR_SW'])
    
    masked_band = ma.array(band,mask=np.isnan(band))
    print masked_band.mask

.. parsed-literal::

    [[ True  True  True ...,  True  True  True]
     [ True  True  True ...,  True  True  True]
     [ True  True  True ...,  True  True  True]
     ..., 
     [False False False ..., False False False]
     [False False False ..., False False False]
     [False False False ..., False False False]]


So we can do this for each band as we loop over each month:

.. code:: python

    from netCDF4 import Dataset
    import numpy as np
    import numpy.ma as ma
    
    root = 'files/data/'
    year = 2009
    
    # which months?
    months = xrange(1,13)
    
    # empty list
    data = []
    
    # loop over month
    # use enumerate so we have an index counter
    for i,month in enumerate(months):
        # this then is the file we want
        local_file = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
        
        # load the netCDF data from the file local_file
        nc = Dataset(local_file,'r')
        # load into the variable 'band'
        band = np.array(nc.variables['DHR_SW'])
        # convert to a masked array
        masked_band = ma.array(band,mask=np.isnan(band))
        # append what we read to the list called data
        data.append(masked_band)
        
    # convert data to a numpy array (its a list of arrays at the moment)
    data = np.array(data)
That's a good start, but we used:

::

    data = np.array(data)

at the end, which means that we have a 3D numpy array ... rather than a
masked array:

.. code:: python

    print type(data)
    print data.shape
    print data.ndim

.. parsed-literal::

    <type 'numpy.ndarray'>
    (12, 360, 720)
    3


so we need to replace this with a function to make it into a masked
array:

.. code:: python

    from netCDF4 import Dataset
    import numpy as np
    import numpy.ma as ma
    
    root = 'files/data/'
    year = 2009
    
    # which months?
    months = xrange(1,13)
    
    # empty list
    data = []
    
    # loop over month
    # use enumerate so we have an index counter
    for i,month in enumerate(months):
        # this then is the file we want
        local_file = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
        
        # load the netCDF data from the file local_file
        nc = Dataset(local_file,'r')
        # load into the variable 'band'
        band = np.array(nc.variables['DHR_SW'])
        # convert to a masked array
        masked_band = ma.array(band,mask=np.isnan(band))
        # append what we read to the list called data
        data.append(masked_band)
        
    # convert data to a numpy array (its a list of arrays at the moment)
    data = ma.array(data)
.. code:: python

    print type(data)
    print data.shape
    print data.ndim

.. parsed-literal::

    <class 'numpy.ma.core.MaskedArray'>
    (12, 360, 720)
    3


we might notice that now, the data mask (``data.mask``) is a 3D mask:

.. code:: python

    print data.mask.shape
    print data.mask.ndim

.. parsed-literal::

    (12, 360, 720)
    3


and we might just check that the mask is the same for all months:

First, lets sum the masks over axis 0 (i.e. over all months):

.. code:: python

    sum = (data.mask).sum(axis=0)
    print sum.shape

.. parsed-literal::

    (360, 720)


.. code:: python

    print sum

.. parsed-literal::

    [[12 12 12 ..., 12 12 12]
     [12 12 12 ..., 12 12 12]
     [12 12 12 ..., 12 12 12]
     ..., 
     [ 0  0  0 ...,  0  0  0]
     [ 0  0  0 ...,  0  0  0]
     [ 0  0  0 ...,  0  0  0]]


This should be 12 (where ``mask`` is ``True``) or 0 (where mask is
``False``). How can we chack that quickly?

Fortunately, there is a convenient numpy function ``np.unique`` that
will give you the unique values in an array:

.. code:: python

    np.unique(sum)



.. parsed-literal::

    array([ 0, 12])



The only values in here are 12 and 0, so the masks must be consistent!
