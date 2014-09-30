
GDAL and related codes and libraries
====================================

GDAL does not always come with your Python distribution.

It can sometimes be a little tricky to install.

Yopu **do not** need it for this class as you can always run things on
the UCL Geography system via ``ssh``, but *might like* to install it, so
we'll try to keep some notes up to date here on how to do that (and
typical problems you encounter).

Since it relies on libraries not written in Python, you need to get
these libraries installed. You may also want to install the GDAL tools.

There are many ways of doing this that you can find by searching on the
internet.

A good place to start is
`trac.osgeo.org <http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries>`__.

Here, we try to give some practical guidance. (Note: I've note been able
to test this under windows, so `give me some
feedback <mailto:p.lewis@ucl.ac.uk>`__ about what works or doesn't).

OS X
----

Pre-compiled GDAL utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several places you can download pre-compiled versions of the
GDAL utilities from.

Oner example is http://www.kyngchaos.com/software:frameworks. If you
install ``GDAL complete`` from there, you should find the GDAL utilities
in ``/Library/Frameworks/GDAL.framework/Programs``:

.. code:: python

    !ls /Library/Frameworks/GDAL.framework/Programs

.. parsed-literal::

    [31mepsg_tr.py[m[m         [31mgdal_fillnodata.py[m[m [31mgdalchksum.py[m[m      [31mgdaltindex[m[m
    [31mesri2wkt.py[m[m        [31mgdal_grid[m[m          [31mgdaldem[m[m            [31mgdaltransform[m[m
    [31mgcps2vec.py[m[m        [31mgdal_merge.py[m[m      [31mgdalenhance[m[m        [31mgdalwarp[m[m
    [31mgcps2wld.py[m[m        [31mgdal_polygonize.py[m[m [31mgdalident.py[m[m       [31mmkgraticule.py[m[m
    [31mgdal-config[m[m        [31mgdal_proximity.py[m[m  [31mgdalimport.py[m[m      [31mnearblack[m[m
    [31mgdal2tiles.py[m[m      [31mgdal_rasterize[m[m     [31mgdalinfo[m[m           [31mogr2ogr[m[m
    [31mgdal2xyz.py[m[m        [31mgdal_retile.py[m[m     [31mgdallocationinfo[m[m   [31mogrinfo[m[m
    [31mgdal_auth.py[m[m       [31mgdal_sieve.py[m[m      [31mgdalmanage[m[m         [31mogrtindex[m[m
    [31mgdal_calc.py[m[m       [31mgdal_translate[m[m     [31mgdalmove.py[m[m        [31mpct2rgb.py[m[m
    [31mgdal_contour[m[m       [31mgdaladdo[m[m           [31mgdalserver[m[m         [31mrgb2pct.py[m[m
    [31mgdal_edit.py[m[m       [31mgdalbuildvrt[m[m       [31mgdalsrsinfo[m[m        [31mtestepsg[m[m


If you want this in your path, put the following line at the bottom of
the file ``~/.bashrc`` (if using ``bash``):

``export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH``

or, if using ``tcsh`` or ``csh``, puth this at the end of your file
``~/.cshrc``:

``setenv PATH "/Library/Frameworks/GDAL.framework/Programs:${PATH}"``

or

``set path = (/Library/Frameworks/GDAL.framework/Programs $path)``

and then type:

``source ~/.bashrc``

or

``source ~/.cshrc``

as appropriate (or open new shells).

You can test that you can access the gdal commands with e.g.:

.. code:: python

    !which gdalinfo
    !gdalinfo --version

.. parsed-literal::

    /Library/Frameworks/GDAL.framework/Programs/gdalinfo
    GDAL 1.10.1, released 2013/08/26


Compiling source (use ``homebrew``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to compile ``GDAL`` yourself for OS X, it is probably
easiest to install the `Homebrew <http://brew.sh/>`__ software, type:

``rehash``

at the unix prompt (to update your path) and follow any instructions it
gives you to sort out any conflicts you might have, then simply:

``brew install gdal``
