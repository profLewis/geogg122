
A4.1. Getting MODIS URLs
========================

Access to MODIS data is now through ``http``, which means that previous
methods using ``ftp`` no longer operate.

In some ways, this complicates automatic download (also, download seems
now to be throttled, which means it takes longer to access the data).

That said, you can of course still easily order data through NASA tools
such as `reverb <http://reverb.echo.nasa.gov>`__.

Some tools have been developed to allow automated access to MODIS
products from Python, such as
`get\_modis <https://github.com/jgomezdans/get_modis>`__, but here, we
will demonstrate how you can do it yourself, semi-automatically.

We will see that a large part of the overhead and complexity is
negotiating the directory structure.

We have provided a shell programme ```zat`` <files/python/zat>`__ that
will produce a list of urls of the MODIS products on the USGS server
(use ``zat >`` ```urls.txt`` <files/data/robot.txt>`__), which you would
probably find more convenient than this section.

So, only go through section A1 if you are particularly intererested in
trawling directories with http ...

Once we have a full list of the urls of the hdf files that we want, life
is much simpler. Such a list of urls is *exactly* what
`reverb <http://reverb.echo.nasa.gov>`__ supplies you with.

A4.1.1 Identify the server and directory structure
--------------------------------------------------

First, you need to identify which datasets you want. You should explore
the data products e.g. through `reverb <http://reverb.echo.nasa.gov>`__
to do this.

If you go through the ordering system for one tile of these products,
you can get the information you need for further data download. When you
come to order the data, it will give you a download file.

As an example:

-  MODIS LAI/fAPAR for Trerra and Aqua 8 day composite for 17 Jan 2013
   for tile h18v03

                http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2013.01.17/MCD15A2.A2013017.h18v03.005.2013026065052.hdf
http://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2013.01.26/BROWSE.MCD15A2.A2013017.h18v03.005.2013026065052.1.jpg
http://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2013.01.26/BROWSE.MCD15A2.A2013017.h18v03.005.2013026065052.2.jpg
http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2013.01.17/MCD15A2.A2013017.h18v03.005.2013026065052.hdf.xml
                
A4.1.2 Identify the available dates
-----------------------------------

From this, we see that the server is ``e4ftl01.cr.usgs.gov``, that the
``hdf`` data (the spatial dataset we want) for the product ``MCD15A2``
version ``005`` is in the directory
``MODIS_Composites/MOTA/MCD15A2.005``.

Below that, we have the date and then the filename.

Let's use ``urllib2`` to explore this:

.. code:: python

    import urllib2
    url_base = 'http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005'
    response = urllib2.urlopen(url_base)
    html = response.read()
.. code:: python

    # print the first 30 lines
    html.split('\n')[:30]
This is an html directory listing. We can identify the directories as
lines that contain ``[DIR]``.

We can use ``find`` to identify lines that have this field:

.. code:: python

    dirs = []
    for line in html.split('\n'):
        if line.find('[DIRS]'):
            dirs.append(line)
.. code:: python

    # or more succinctly
    dirs = [line for line in html.split('\n') if line.find('[DIR]') != -1]
.. code:: python

    dirs[:3]
We notice that the first such line is the directory listing information,
so, what we really want is:

.. code:: python

    dirs = [line for line in html.split('\n') if line.find('[DIR]') != -1][1:]
.. code:: python

    dirs[:3]
The subdirectory name is jusr after the field ``href="``:

.. code:: python

    print dirs[1]
.. code:: python

    print dirs[1].split('href="')[1]
.. code:: python

    print dirs[1].split('href="')[1].split('/">')[0]
So, in this case, we can get the subdirectory names with:

.. code:: python

    dirs = [line.split('href="')[1].split('/">')[0] for line in html.split('\n') if line.find('[DIR]') != -1][1:]
.. code:: python

    # print the first 10
    dirs[:10]
The pattern is ``YYYY.MM.DD``. So we could split these as we go along.
It would be convenient to have this as a numpy array:

.. code:: python

    dirs = np.array([line.split('href="')[1].split('/">')[0].split('.') \
                     for line in html.split('\n') if line.find('[DIR]') != -1][1:])
.. code:: python

    dirs[:10]
.. code:: python

    all_years = np.sort(np.unique(dirs[:,0]))
    all_months = np.sort(np.unique(dirs[:,1]))
    all_doys = np.sort(np.unique(dirs[:,2]))
.. code:: python

    years,months,doys
A4.1.3 Identify the datasets
----------------------------

We know the full url is of the form:

``http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2013.01.17/MCD15A2.A2013017.h18v03.005.2013026065052.hdf``

Simplifying what we did above:

.. code:: python

    import urllib2
    url_base = 'http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005'
    response = urllib2.urlopen(url_base)
    dirs = np.array([line.split('href="')[1].split('/">')[0] for line in html.split('\n') if line.find('[DIR]') != -1][1:])
.. code:: python

    years = np.array([i.split('.')[0] for i in dirs])
    # year mask
    year = '2012'
    mask = (year == years)
    sub_dirs = dirs[mask]
    print sub_dirs
.. code:: python

    # test with first one
    this_date = sub_dirs[0]
    
    url_date = url_base + '/' + this_date
    print url_date
    response1 = urllib2.urlopen(url_date)
    html1 = response1.read()
.. code:: python

    # print the first 21 lines
    html1.split('\n')[:21]
We note that the directory contains data for all tiles.

Lets filter only lines that have the tile we want in:

.. code:: python

    tile = 'h18v03'
    lines = [line for line in html1.split('\n') if line.find(tile) != -1]
.. code:: python

    lines
We want the ``.hdf`` file, so refine the filter:

.. code:: python

    tile = 'h18v03'
    hdf_lines = [i for i in [line for line in html1.split('\n') \
                             if line.find(tile) != -1] if i.find('.hdf"') != -1]
.. code:: python

    hdf_lines
Now split this to get the filename we want:

.. code:: python

    hdf_lines[0].split('<a href="')[1]
.. code:: python

    hdf_lines[0].split('<a href="')[1].split('">')[0]
So, putting all of that together:

.. code:: python

    tile = 'h18v03'
    hdf_lines = [i for i in [line for line in html1.split('\n') \
                             if line.find(tile) != -1] if i.find('.hdf"') != -1]
    hdf_file = hdf_lines[0].split('<a href="')[1].split('">')[0]
A4.1.4 Some code for MODIS LAI filenames for a year
---------------------------------------------------

The http access is quite slow, so this may take some minutes to run.

.. code:: python

    year = '2012'
    tile = 'h17v03'
    
    
    hdf_files = []
    
    import urllib2
    
    # base URL for the product
    url_base = 'http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005'
    
    response = urllib2.urlopen(url_base)
    html = response.read()
    
    dirs = np.array([line.split('href="')[1].split('/">')[0] for line in html.split('\n') if line.find('[DIR]') != -1][1:])
    
    # identify years
    years = np.array([i.split('.')[0] for i in dirs])
    # year mask
    mask = (year == years)
    sub_dirs = dirs[mask]
    
    for this_date in sub_dirs:
        url_date = url_base + '/' + this_date
        print url_date
        response1 = urllib2.urlopen(url_date)
        html1 = response1.read()
        hdf_lines = [i for i in [line for line in html1.split('\n') \
                                 if line.find(tile) != -1] if i.find('.hdf"') != -1]
        hdf_file = url_date + '/' + hdf_lines[0].split('<a href="')[1].split('">')[0]
        hdf_files.append(hdf_file+'\n')
        

.. parsed-literal::

    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.01
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.09
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.17
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.25
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.02
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.10
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.18
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.26
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.05
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.13
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.21
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.29
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.06
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.14
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.22
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.30
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.05.08
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.05.16
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.05.24
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.01
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.09
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.17
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.25
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.03
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.11
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.19
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.27
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.04
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.12
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.20
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.28
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.05
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.13
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.21
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.29
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.07
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.15
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.23
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.31
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.11.08
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.11.16
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.11.24
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.02
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.10
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.18
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.26


In case download fails later, lets save this list ``hdf_files``.

.. code:: python

    f = open('files/data/lai_list.txt','w')
    f.writelines(hdf_files)
    f.close()
A4.1.5 Pull Data from url
-------------------------

This part is actually faster than doing all of that messing around with
directories.

You don't really want to have to do too much of the directory
exploration, so it is *probably* a good idea to just periodically scan
the whole structure and store that in a local file. You can then parse
the local file much more easily (that is what we do in the main part of
the class).

This is achieved for instance with the shell
```zat`` <files/python/zat>`__ (use ``zat >``
```urls.txt`` <files/data/robot.txt>`__) if you want to do an update, or
just use the existing `url file <files/data/robot.txt>`__.

.. code:: python

    import urllib2
    
    f = open('files/data/lai_list.txt','r')
    hdf_files = f.readlines()
    f.close()
    
    for url in hdf_files:
        url = url.strip()
        print url
        response = urllib2.urlopen(url.strip())
        ofile = 'files/data/' + url.split('/')[-1]
        f = open(ofile,'w')
        f.write(response.read())
        f.close()

.. parsed-literal::

    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.01/MCD15A2.A2012001.h17v03.005.2012017211237.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.09/MCD15A2.A2012009.h17v03.005.2012019044037.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.17/MCD15A2.A2012017.h17v03.005.2012026072526.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.01.25/MCD15A2.A2012025.h17v03.005.2012052124839.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.02/MCD15A2.A2012033.h17v03.005.2012042060649.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.10/MCD15A2.A2012041.h17v03.005.2012050092057.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.18/MCD15A2.A2012049.h17v03.005.2012068144447.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.02.26/MCD15A2.A2012057.h17v03.005.2012068140544.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.05/MCD15A2.A2012065.h17v03.005.2012075021749.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.13/MCD15A2.A2012073.h17v03.005.2012083010304.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.21/MCD15A2.A2012081.h17v03.005.2012090131602.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.03.29/MCD15A2.A2012089.h17v03.005.2012107201245.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.06/MCD15A2.A2012097.h17v03.005.2012108125047.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.14/MCD15A2.A2012105.h17v03.005.2012116125519.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.22/MCD15A2.A2012113.h17v03.005.2012122072153.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.04.30/MCD15A2.A2012121.h17v03.005.2012137221611.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.05.08/MCD15A2.A2012129.h17v03.005.2012142001241.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.05.16/MCD15A2.A2012137.h17v03.005.2012153021910.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.05.24/MCD15A2.A2012145.h17v03.005.2012160130927.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.01/MCD15A2.A2012153.h17v03.005.2012166161748.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.09/MCD15A2.A2012161.h17v03.005.2012170080216.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.17/MCD15A2.A2012169.h17v03.005.2012181134242.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.06.25/MCD15A2.A2012177.h17v03.005.2012188150145.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.03/MCD15A2.A2012185.h17v03.005.2012208181105.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.11/MCD15A2.A2012193.h17v03.005.2012202144013.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.19/MCD15A2.A2012201.h17v03.005.2012215131931.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.07.27/MCD15A2.A2012209.h17v03.005.2012219144450.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.04/MCD15A2.A2012217.h17v03.005.2012228215213.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.12/MCD15A2.A2012225.h17v03.005.2012234105932.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.20/MCD15A2.A2012233.h17v03.005.2012242093511.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.08.28/MCD15A2.A2012241.h17v03.005.2012250182515.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.05/MCD15A2.A2012249.h17v03.005.2012261231425.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.13/MCD15A2.A2012257.h17v03.005.2012270114223.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.21/MCD15A2.A2012265.h17v03.005.2012276134731.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.09.29/MCD15A2.A2012273.h17v03.005.2012297134400.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.07/MCD15A2.A2012281.h17v03.005.2012297135831.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.15/MCD15A2.A2012289.h17v03.005.2012299194634.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.23/MCD15A2.A2012297.h17v03.005.2012306163257.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.10.31/MCD15A2.A2012305.h17v03.005.2012314140451.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.11.08/MCD15A2.A2012313.h17v03.005.2012322095802.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.11.16/MCD15A2.A2012321.h17v03.005.2012335133638.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.11.24/MCD15A2.A2012329.h17v03.005.2012340181739.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.02/MCD15A2.A2012337.h17v03.005.2012346165133.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.10/MCD15A2.A2012345.h17v03.005.2012356133200.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.18/MCD15A2.A2012353.h17v03.005.2012363125132.hdf
    http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005/2012.12.26/MCD15A2.A2012361.h17v03.005.2013007202756.hdf


A4.2 GDAL tools and HDF format
==============================

`HDF <http://www.hdfgroup.org/HDF-FAQ.html>`__\ (Hierarchical Data
Format) and `HDF-EOS <http://hdfeos.org/>`__ are common formats for EO
data so you need to have some idea how to use and manipulate them.

A hierarchical data format is essentially a format that ‘packs’ together
various aspects of a dataset (metadata, raster data etc.) into a binary
file. There are many tools for manipulating and reading HDF in python,
but we will use one of the more generic tools,
`gdal <http://gdal.org>`__ here.

When using HDF files, we need to have some idea of the stucture of the
contents, although you can clearly explore that yourself in an
interactive session. MODIS products have extensive information available
to help you interpret the datasets, for example the MODIS LAI/fAPAR
product
`MOD15A2 <https://lpdaac.usgs.gov/products/modis_products_table/leaf_area_index_fraction_of_photosynthetically_active_radiation/8_day_l4_global_1km/mod15a2>`__.
We will use this as an example to explore a dataset.

You will need access to the file
```files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf`` <files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf>`__,
which you might access from the `MODIS Land Products
site <https://lpdaac.usgs.gov/>`__

Before going into the Python coding for GDAL, it is worthwhile looking
over some of the tools that are provided with GDAL and that can be run
from the shell. In particular, we can use the ``gdalinfo`` program, that
takes a filename and will output a copious description of the data,
including metadata, but also geogrpahic projection, size, number of
bands, etc.

Here, we will look at the first 20 lines that come out of ``gdalinfo``:

.. code:: python

    !gdalinfo files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf | head -20

.. parsed-literal::

    Driver: HDF4/Hierarchical Data Format Release 4
    Files: files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf
    Size is 512, 512
    Coordinate System is `'
    Metadata:
      ALGORITHMPACKAGEACCEPTANCEDATE=10-01-2004
      ALGORITHMPACKAGEMATURITYCODE=Normal
      ALGORITHMPACKAGENAME=MCDPR_15A2
      ALGORITHMPACKAGEVERSION=5
      ASSOCIATEDINSTRUMENTSHORTNAME=MODIS
      ASSOCIATEDINSTRUMENTSHORTNAME=MODIS
      ASSOCIATEDPLATFORMSHORTNAME=Aqua
      ASSOCIATEDPLATFORMSHORTNAME=Terra
      ASSOCIATEDSENSORSHORTNAME=MODIS
      ASSOCIATEDSENSORSHORTNAME=MODIS
      AUTOMATICQUALITYFLAG=Passed
      AUTOMATICQUALITYFLAGEXPLANATION=No automatic quality assessment is performed in the PGE
      CHARACTERISTICBINANGULARSIZE=30.0
      CHARACTERISTICBINSIZE=926.625433055556
      DATACOLUMNS=1200


We can use standard unix filters (e.g. ``grep``) to look at particular
fields:

.. code:: python

    # Filter lines that do not have BOUNDINGCOORDINATE in them
    file=files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf
    gdalinfo $file | grep BOUNDINGCOORDINATE

.. parsed-literal::

      EASTBOUNDINGCOORDINATE=-92.3664205550513
      NORTHBOUNDINGCOORDINATE=39.9999999964079
      SOUTHBOUNDINGCOORDINATE=29.9999999973059
      WESTBOUNDINGCOORDINATE=-117.486656023174


We can check this against e.g. the `UNH MODIS tile
calculator <http://remotesensing.unh.edu/modis/modis.shtml>`__, just to
confirm that we have interpreted the coordinates correctly.

We can apply other shell GDAL tools, e.g. to perform a reprojection from
the native `MODIS
sinusoidal <http://modis-land.gsfc.nasa.gov/MODLAND_grid.html>`__
projection, to the `Contiguous United States NAD27 Albers Equal
Area <http://spatialreference.org/ref/sr-org/7271/>`__:

.. code:: python

    # a bash script
    
    # set the variables file to be the filename for convenience
    file=files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf
    
    # dselete the output file if it exists
    rm -f files/data/output_file.tif 
    
    # reproject the data
    gdalwarp -of GTiff \
        -t_srs '+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=23 +lon_0=-96 +x_0=0 \
        +y_0=0 +ellps=clrk66 +units=m +no_defs' -tr 1000 1000 \
        'HDF4_EOS:EOS_GRID:'${file}':MOD_Grid_MOD15A2:Lai_1km' files/data/output_file.tif
    
    # convert to gif for viewing
    gdal_translate -outsize 30% 30% -of gif \
        files/data/output_file.tif files/data/output_file.gif

.. parsed-literal::

    Creating output file that is 2152P x 1323L.
    Processing input file HDF4_EOS:EOS_GRID:files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf:MOD_Grid_MOD15A2:Lai_1km.
    Using internal nodata values (eg. 255) for image HDF4_EOS:EOS_GRID:files/data/MCD15A2.A2011185.h09v05.005.2011213154534.hdf:MOD_Grid_MOD15A2:Lai_1km.
    0...10...20...30...40...50...60...70...80...90...100 - done.
    Input file size is 2152, 1323
    0...10...20...30...40...50...60...70...80...90...100 - done.


.. figure:: files/data/output_file.gif
   :alt: 

where ``MCD15A2.A2011185.h09v05.005.2011213154534.hdf`` is the name of
the input HDF file, ``MOD_Grid_MOD15A2:Lai_1km`` is the data product we
want, and the rather menacing string
``+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=23 +lon_0=-96 +x_0=0 +y_0=0 +ellps=clrk66 +units=m +no_defs``
specifies the projection in Proj4 format. You can typically find the
projection you want on
`spatialreference.org <http://spatialreference.org>`__, and just copy
and paste the contents of `Proj4
definition <http://spatialreference.org/ref/sr-org/7271/proj4/>`__
(remember to surround it by quotes). The option ``-tr xres yres``
specifies the desired resolution of the output dataset (1000 by 1000 m
in the case above). ``-of GTiff`` specifies the GeoTiff format to be
used as as output.

A4.3 Further Geospatial Notes
=============================

There are additonal notes that go into the details of ``gdal`` and
vectors processing tools.

Follow these on:

-  `gdal <GDAL_Python_bindings.ipynb>`__
-  `ogr <OGR_Python>`__

There are no explicit advanced exercises this week. Instead, you should
eplore these notes and see if you can apply the concepts to your own
datasets.
