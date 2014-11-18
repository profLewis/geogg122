
7.0 Fire/ENSO teleconnections
=============================

7.1 Introduction
----------------

There is much public and scientific interest in monitoring and
predicting the activity of wildfires and such topics are `often in the
media <http://www.bbc.co.uk/news/science-environment-15691060>`__.

Part of this interest stems from the role fire plays in issues such as
land cover change, deforestation and forest degradation and `Carbon
emissions <http://www.google.com/url?sa=t&rct=j&q=fire%20carbon%20emissions&source=web&cd=6&ved=0CFEQFjAF&url=http%3A%2F%2Fwww.kcl.ac.uk%2Fsspp%2Fdepartments%2Fgeography%2Fpeople%2Facademic%2Fwooster%2F30yongwoosteretal.pdf&ei=4FPCTuvZE9Gg8gPZybyxBA&usg=AFQjCNG81fTRoCcK1nhKnk3u0b8az24bGQ&sig2=EjJYm2S-_2gHu2vgt4ByvA&cad=rja>`__
from the land surface to the atmosphere, but also of concern are human
health impacts. The impacts of fire should not however be considered as
wholy negative, as it plays a `significant role in natural ecosystem
processes <http://www.fl-dof.com/publications/fires_natural_role.html#firerole>`__.

For many regions of the Earth, there are large inter-annual variations
in the timing, frequency and severity of wildfires. Whilst anthropogenic
activity accounts for a `large and probably increasing
proportion <http://www.google.com/url?sa=t&rct=j&q=fire%20frequency%20july%204th&source=web&cd=7&ved=0CFIQFjAG&url=http%3A%2F%2Farctic.synergiesprairies.ca%2Farctic%2Findex.php%2Farctic%2Farticle%2Fdownload%2F2806%2F2783&ei=K1bCTqv1MYS28QOR9ekG&usg=AFQjCNFKillAOZMXrT5xpFhckMKvqW50Vg&sig2=r3J6454VcvI1xpC3Sf3RKw&cad=rja>`__
of fires started, this is not in itself `a new
phenomenon <http://www.google.com/url?sa=t&rct=j&q=anthropogenic%20fire&source=web&cd=2&ved=0CCcQFjAB&url=http%3A%2F%2Fwww.as.ua.edu%2Fant%2Fbindon%2Fant475%2FPapers%2FHamm.pdf&ei=rFXCTu-PHsay8QPdy-2MBA&usg=AFQjCNGUMrfnDTwRDBxFB-wioZokBt8EtA&sig2=Zt1nfHoKktbka-pEZs6NGw&cad=rja>`__.

Fires spread where: (i) there is an ignition source (lightning or man,
mostly); (ii) sufficient combustible fuel to maintain the fire. The
latter is strongly dependent on fuel loads and mositure content, as well
as meteorological conditions. Generally then, when conditions are drier
(and there is sufficient fuel and appropriate weather conditions), we
would expect fire spread to increase. If the number of ignitions
remained approximately constant, this would mean more fires. `Many
models of fire
activity <http://www.nasa.gov/images/content/492949main_Figure-2-Wildfires.jpg>`__
predict increases in fire frequency in the coming decades, although
there may well be `different behaviours in differet parts of the
world <http://news.sciencemag.org/sciencenow/2009/04/10-02.html>`__.

|image0|

Satellite data has been able to provide us with increasingly useful
tools for monitoring wildfire activity, particularly since 2000 with the
MODIS instruments on the NASA Terra and Aqua (2002) satellites. A suite
of `‘fire’ products <http://modis-fire.umd.edu/index.html>`__ have been
generated from these data that have been used in a large number of
`publications <http://modis-fire.umd.edu/Publications.html>`__ and
`practical/management
projects <https://earthdata.nasa.gov/data/near-real-time-data/firms>`__.

There is growing evidence of ‘teleconnection’ links between fire
occurence and large scale climate patterns, such as
`ENSO <http://www.esrl.noaa.gov/psd/enso/>`__.

|image1|

The proposed mechanisms are essentially that such climatic patterns are
linked to local water status and temperature and thus affect the ability
of fires to spread. For some regions of the Earth, empirical models
built from such considerations have quite reasonable predictive skill,
meaning that fire season severity might be predicted `some months ahead
of time <http://www.sciencemag.org/content/334/6057/787.full>`__.

.. |image0| image:: files/images/492949main_Figure-2-Wildfires_s3.jpg
   :target: http://www.nasa.gov/images/content/492949main_Figure-2-Wildfires.jpg
.. |image1| image:: http://www.esrl.noaa.gov/psd/enso/mei/ts.gif
   :target: http://www.esrl.noaa.gov/psd/enso/mei/

7.2 A Practical Exercise
------------------------

7.2.1 In This Session
~~~~~~~~~~~~~~~~~~~~~

In this session, you will be working in groups (of 3 or 4) to build a
computer code in python to explore links between fire activity and Sea
Surface Temperature anomalies.

This is a team exercise, but does not form part of your formal
assessment for this course. You should be able to complete the exercise
in the 3 hour session, if you work effectively as a team. Staff will be
on hand to provide pointers.

You should be able to complete the exercise using coding skills and
python modules that you have previously experience of, though we will
also provide some pointers to get you started.

7.2.2 Statement of the problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using monthly fire count data from MODIS Terra, develop and test a
predictive model for the number of fires per unit area per year driven
by Sea Surface Temperature anomaly data.

7.2.3 Datasets
~~~~~~~~~~~~~~

We suggest that the datasets you use of this analysis, following Chen at
al. (2011), are:

-  MODIS Terra fire counts (2001-2011) (MOD14CMH). The particular
   dataset you will want from the file is ‘SUBDATASET\_2 [360x720]
   CloudCorrFirePix (16-bit integer)’.
-  Climate index data from NOAA

If you ever wish to take this study further, you can find various other
useful datasets such as these.

Fire Data
^^^^^^^^^

The MOD14CMH `CMG
data <http://nsidc.org/data/modis/data_summaries/cmg_sample.html>`__ are
available from the `UMD ftp
server <ftp://fire:burnt@fuoco.geog.umd.edu/modis/C5/cmg/monthly/hdf>`__
but the data you will need are also directly available from
/data/geospatial\_10/ucfajlg/MOD14CMH/. Note that, if you are on the UCL
system, you do not need to copy the data, just use them from where they
are.

If for any reason, you *did* want to copy or update them, use the
following unix command:

``wget 'ftp://fire:burnt@fuoco.geog.umd.edu/modis/C5/cmg/monthly/hdf/*'``

(though you may need to update the password). The data are in
`data <data>`__ and are in HDF format, so you should know how to read
them into a numpy array in python.

.. code:: python

    !ls data/*hdf

.. parsed-literal::

    data/MOD14CMH.200011.005.01.hdf  data/MOD14CMH.201211.005.01.hdf
    data/MOD14CMH.200012.005.01.hdf  data/MOD14CMH.201212.005.01.hdf
    data/MOD14CMH.200101.005.01.hdf  data/MOD14CMH.201301.005.01.hdf
    data/MOD14CMH.200102.005.01.hdf  data/MOD14CMH.201302.005.01.hdf
    data/MOD14CMH.200103.005.01.hdf  data/MOD14CMH.201303.005.01.hdf
    data/MOD14CMH.200104.005.01.hdf  data/MOD14CMH.201304.005.01.hdf
    data/MOD14CMH.200105.005.01.hdf  data/MOD14CMH.201305.005.01.hdf
    data/MOD14CMH.200106.005.01.hdf  data/MOD14CMH.201306.005.01.hdf
    data/MOD14CMH.200107.005.01.hdf  data/MOD14CMH.201307.005.01.hdf
    data/MOD14CMH.200108.005.01.hdf  data/MOD14CMH.201308.005.01.hdf
    data/MOD14CMH.200109.005.01.hdf  data/MYD14CMH.200207.005.01.hdf
    data/MOD14CMH.200110.005.01.hdf  data/MYD14CMH.200208.005.01.hdf
    data/MOD14CMH.200111.005.01.hdf  data/MYD14CMH.200209.005.01.hdf
    data/MOD14CMH.200112.005.01.hdf  data/MYD14CMH.200210.005.01.hdf
    data/MOD14CMH.200201.005.01.hdf  data/MYD14CMH.200211.005.01.hdf
    data/MOD14CMH.200202.005.01.hdf  data/MYD14CMH.200212.005.01.hdf
    data/MOD14CMH.200203.005.01.hdf  data/MYD14CMH.200301.005.01.hdf
    data/MOD14CMH.200204.005.01.hdf  data/MYD14CMH.200302.005.01.hdf
    data/MOD14CMH.200205.005.01.hdf  data/MYD14CMH.200303.005.01.hdf
    data/MOD14CMH.200206.005.01.hdf  data/MYD14CMH.200304.005.01.hdf
    data/MOD14CMH.200207.005.01.hdf  data/MYD14CMH.200305.005.01.hdf
    data/MOD14CMH.200208.005.01.hdf  data/MYD14CMH.200306.005.01.hdf
    data/MOD14CMH.200209.005.01.hdf  data/MYD14CMH.200307.005.01.hdf
    data/MOD14CMH.200210.005.01.hdf  data/MYD14CMH.200308.005.01.hdf
    data/MOD14CMH.200211.005.01.hdf  data/MYD14CMH.200309.005.01.hdf
    data/MOD14CMH.200212.005.01.hdf  data/MYD14CMH.200310.005.01.hdf
    data/MOD14CMH.200301.005.01.hdf  data/MYD14CMH.200311.005.01.hdf
    data/MOD14CMH.200302.005.01.hdf  data/MYD14CMH.200312.005.01.hdf
    data/MOD14CMH.200303.005.01.hdf  data/MYD14CMH.200401.005.01.hdf
    data/MOD14CMH.200304.005.01.hdf  data/MYD14CMH.200402.005.01.hdf
    data/MOD14CMH.200305.005.01.hdf  data/MYD14CMH.200403.005.01.hdf
    data/MOD14CMH.200306.005.01.hdf  data/MYD14CMH.200404.005.01.hdf
    data/MOD14CMH.200307.005.01.hdf  data/MYD14CMH.200405.005.01.hdf
    data/MOD14CMH.200308.005.01.hdf  data/MYD14CMH.200406.005.01.hdf
    data/MOD14CMH.200309.005.01.hdf  data/MYD14CMH.200407.005.01.hdf
    data/MOD14CMH.200310.005.01.hdf  data/MYD14CMH.200408.005.01.hdf
    data/MOD14CMH.200311.005.01.hdf  data/MYD14CMH.200409.005.01.hdf
    data/MOD14CMH.200312.005.01.hdf  data/MYD14CMH.200410.005.01.hdf
    data/MOD14CMH.200401.005.01.hdf  data/MYD14CMH.200411.005.01.hdf
    data/MOD14CMH.200402.005.01.hdf  data/MYD14CMH.200412.005.01.hdf
    data/MOD14CMH.200403.005.01.hdf  data/MYD14CMH.200501.005.01.hdf
    data/MOD14CMH.200404.005.01.hdf  data/MYD14CMH.200502.005.01.hdf
    data/MOD14CMH.200405.005.01.hdf  data/MYD14CMH.200503.005.01.hdf
    data/MOD14CMH.200406.005.01.hdf  data/MYD14CMH.200504.005.01.hdf
    data/MOD14CMH.200407.005.01.hdf  data/MYD14CMH.200505.005.01.hdf
    data/MOD14CMH.200408.005.01.hdf  data/MYD14CMH.200506.005.01.hdf
    data/MOD14CMH.200409.005.01.hdf  data/MYD14CMH.200507.005.01.hdf
    data/MOD14CMH.200410.005.01.hdf  data/MYD14CMH.200508.005.01.hdf
    data/MOD14CMH.200411.005.01.hdf  data/MYD14CMH.200509.005.01.hdf
    data/MOD14CMH.200412.005.01.hdf  data/MYD14CMH.200510.005.01.hdf
    data/MOD14CMH.200501.005.01.hdf  data/MYD14CMH.200511.005.01.hdf
    data/MOD14CMH.200502.005.01.hdf  data/MYD14CMH.200512.005.01.hdf
    data/MOD14CMH.200503.005.01.hdf  data/MYD14CMH.200601.005.01.hdf
    data/MOD14CMH.200504.005.01.hdf  data/MYD14CMH.200602.005.01.hdf
    data/MOD14CMH.200505.005.01.hdf  data/MYD14CMH.200603.005.01.hdf
    data/MOD14CMH.200506.005.01.hdf  data/MYD14CMH.200604.005.01.hdf
    data/MOD14CMH.200507.005.01.hdf  data/MYD14CMH.200605.005.01.hdf
    data/MOD14CMH.200508.005.01.hdf  data/MYD14CMH.200606.005.01.hdf
    data/MOD14CMH.200509.005.01.hdf  data/MYD14CMH.200607.005.01.hdf
    data/MOD14CMH.200510.005.01.hdf  data/MYD14CMH.200608.005.01.hdf
    data/MOD14CMH.200511.005.01.hdf  data/MYD14CMH.200609.005.01.hdf
    data/MOD14CMH.200512.005.01.hdf  data/MYD14CMH.200610.005.01.hdf
    data/MOD14CMH.200601.005.01.hdf  data/MYD14CMH.200611.005.01.hdf
    data/MOD14CMH.200602.005.01.hdf  data/MYD14CMH.200612.005.01.hdf
    data/MOD14CMH.200603.005.01.hdf  data/MYD14CMH.200701.005.01.hdf
    data/MOD14CMH.200604.005.01.hdf  data/MYD14CMH.200702.005.01.hdf
    data/MOD14CMH.200605.005.01.hdf  data/MYD14CMH.200703.005.01.hdf
    data/MOD14CMH.200606.005.01.hdf  data/MYD14CMH.200704.005.01.hdf
    data/MOD14CMH.200607.005.01.hdf  data/MYD14CMH.200705.005.01.hdf
    data/MOD14CMH.200608.005.01.hdf  data/MYD14CMH.200706.005.01.hdf
    data/MOD14CMH.200609.005.01.hdf  data/MYD14CMH.200707.005.01.hdf
    data/MOD14CMH.200610.005.01.hdf  data/MYD14CMH.200708.005.01.hdf
    data/MOD14CMH.200611.005.01.hdf  data/MYD14CMH.200709.005.01.hdf
    data/MOD14CMH.200612.005.01.hdf  data/MYD14CMH.200710.005.01.hdf
    data/MOD14CMH.200701.005.01.hdf  data/MYD14CMH.200711.005.01.hdf
    data/MOD14CMH.200702.005.01.hdf  data/MYD14CMH.200712.005.01.hdf
    data/MOD14CMH.200703.005.01.hdf  data/MYD14CMH.200801.005.01.hdf
    data/MOD14CMH.200704.005.01.hdf  data/MYD14CMH.200802.005.01.hdf
    data/MOD14CMH.200705.005.01.hdf  data/MYD14CMH.200803.005.01.hdf
    data/MOD14CMH.200706.005.01.hdf  data/MYD14CMH.200804.005.01.hdf
    data/MOD14CMH.200707.005.01.hdf  data/MYD14CMH.200805.005.01.hdf
    data/MOD14CMH.200708.005.01.hdf  data/MYD14CMH.200806.005.01.hdf
    data/MOD14CMH.200709.005.01.hdf  data/MYD14CMH.200807.005.01.hdf
    data/MOD14CMH.200710.005.01.hdf  data/MYD14CMH.200808.005.01.hdf
    data/MOD14CMH.200711.005.01.hdf  data/MYD14CMH.200809.005.01.hdf
    data/MOD14CMH.200712.005.01.hdf  data/MYD14CMH.200810.005.01.hdf
    data/MOD14CMH.200801.005.01.hdf  data/MYD14CMH.200811.005.01.hdf
    data/MOD14CMH.200802.005.01.hdf  data/MYD14CMH.200812.005.01.hdf
    data/MOD14CMH.200803.005.01.hdf  data/MYD14CMH.200901.005.01.hdf
    data/MOD14CMH.200804.005.01.hdf  data/MYD14CMH.200902.005.01.hdf
    data/MOD14CMH.200805.005.01.hdf  data/MYD14CMH.200903.005.01.hdf
    data/MOD14CMH.200806.005.01.hdf  data/MYD14CMH.200904.005.01.hdf
    data/MOD14CMH.200807.005.01.hdf  data/MYD14CMH.200905.005.01.hdf
    data/MOD14CMH.200808.005.01.hdf  data/MYD14CMH.200906.005.01.hdf
    data/MOD14CMH.200809.005.01.hdf  data/MYD14CMH.200907.005.01.hdf
    data/MOD14CMH.200810.005.01.hdf  data/MYD14CMH.200908.005.01.hdf
    data/MOD14CMH.200811.005.01.hdf  data/MYD14CMH.200909.005.01.hdf
    data/MOD14CMH.200812.005.01.hdf  data/MYD14CMH.200910.005.01.hdf
    data/MOD14CMH.200901.005.01.hdf  data/MYD14CMH.200911.005.01.hdf
    data/MOD14CMH.200902.005.01.hdf  data/MYD14CMH.200912.005.01.hdf
    data/MOD14CMH.200903.005.01.hdf  data/MYD14CMH.201001.005.01.hdf
    data/MOD14CMH.200904.005.01.hdf  data/MYD14CMH.201002.005.01.hdf
    data/MOD14CMH.200905.005.01.hdf  data/MYD14CMH.201003.005.01.hdf
    data/MOD14CMH.200906.005.01.hdf  data/MYD14CMH.201004.005.01.hdf
    data/MOD14CMH.200907.005.01.hdf  data/MYD14CMH.201005.005.01.hdf
    data/MOD14CMH.200908.005.01.hdf  data/MYD14CMH.201006.005.01.hdf
    data/MOD14CMH.200909.005.01.hdf  data/MYD14CMH.201007.005.01.hdf
    data/MOD14CMH.200910.005.01.hdf  data/MYD14CMH.201008.005.01.hdf
    data/MOD14CMH.200911.005.01.hdf  data/MYD14CMH.201009.005.01.hdf
    data/MOD14CMH.200912.005.01.hdf  data/MYD14CMH.201010.005.01.hdf
    data/MOD14CMH.201001.005.01.hdf  data/MYD14CMH.201011.005.01.hdf
    data/MOD14CMH.201002.005.01.hdf  data/MYD14CMH.201012.005.01.hdf
    data/MOD14CMH.201003.005.01.hdf  data/MYD14CMH.201101.005.01.hdf
    data/MOD14CMH.201004.005.01.hdf  data/MYD14CMH.201102.005.01.hdf
    data/MOD14CMH.201005.005.01.hdf  data/MYD14CMH.201103.005.01.hdf
    data/MOD14CMH.201006.005.01.hdf  data/MYD14CMH.201104.005.01.hdf
    data/MOD14CMH.201007.005.01.hdf  data/MYD14CMH.201105.005.01.hdf
    data/MOD14CMH.201008.005.01.hdf  data/MYD14CMH.201106.005.01.hdf
    data/MOD14CMH.201009.005.01.hdf  data/MYD14CMH.201107.005.01.hdf
    data/MOD14CMH.201010.005.01.hdf  data/MYD14CMH.201108.005.01.hdf
    data/MOD14CMH.201011.005.01.hdf  data/MYD14CMH.201109.005.01.hdf
    data/MOD14CMH.201012.005.01.hdf  data/MYD14CMH.201110.005.01.hdf
    data/MOD14CMH.201101.005.01.hdf  data/MYD14CMH.201111.005.01.hdf
    data/MOD14CMH.201102.005.01.hdf  data/MYD14CMH.201112.005.01.hdf
    data/MOD14CMH.201103.005.01.hdf  data/MYD14CMH.201201.005.01.hdf
    data/MOD14CMH.201104.005.01.hdf  data/MYD14CMH.201202.005.01.hdf
    data/MOD14CMH.201105.005.01.hdf  data/MYD14CMH.201203.005.01.hdf
    data/MOD14CMH.201106.005.01.hdf  data/MYD14CMH.201204.005.01.hdf
    data/MOD14CMH.201107.005.01.hdf  data/MYD14CMH.201205.005.01.hdf
    data/MOD14CMH.201108.005.01.hdf  data/MYD14CMH.201206.005.01.hdf
    data/MOD14CMH.201109.005.01.hdf  data/MYD14CMH.201207.005.01.hdf
    data/MOD14CMH.201110.005.01.hdf  data/MYD14CMH.201208.005.01.hdf
    data/MOD14CMH.201111.005.01.hdf  data/MYD14CMH.201209.005.01.hdf
    data/MOD14CMH.201112.005.01.hdf  data/MYD14CMH.201210.005.01.hdf
    data/MOD14CMH.201201.005.01.hdf  data/MYD14CMH.201211.005.01.hdf
    data/MOD14CMH.201202.005.01.hdf  data/MYD14CMH.201212.005.01.hdf
    data/MOD14CMH.201203.005.01.hdf  data/MYD14CMH.201301.005.01.hdf
    data/MOD14CMH.201204.005.01.hdf  data/MYD14CMH.201302.005.01.hdf
    data/MOD14CMH.201205.005.01.hdf  data/MYD14CMH.201303.005.01.hdf
    data/MOD14CMH.201206.005.01.hdf  data/MYD14CMH.201304.005.01.hdf
    data/MOD14CMH.201207.005.01.hdf  data/MYD14CMH.201305.005.01.hdf
    data/MOD14CMH.201208.005.01.hdf  data/MYD14CMH.201306.005.01.hdf
    data/MOD14CMH.201209.005.01.hdf  data/MYD14CMH.201307.005.01.hdf
    data/MOD14CMH.201210.005.01.hdf  data/MYD14CMH.201308.005.01.hdf


If you are **really** stuck on reading the data, or just want to move on
to the next parts, you can use
```python/reader.py`` <python/reader.py>`__ which will create a masked
array in ``data``, and an array of years (``year``) and months
(``month``):

.. code:: python

    run python/reader
.. code:: python

    plt.figure(figsize=(10,6))
    x = year + month/12.
    y = np.sum(data,axis=(1,2))
    plt.plot(x,y)
    plt.ylabel('global fire count')
    plt.xlabel('time')



.. parsed-literal::

    <matplotlib.text.Text at 0x7fe70671a8d0>




.. image:: ENSO_files/ENSO_13_1.png


This dataset is at 0.5 degree resolution and we want to perform tha
analysis as 5 degrees.

We need to shrink the dataset by a factor of 10 then.

There are different ways to achive this, but one way would be to
reoganise the data:

.. code:: python

    rdata = [data[:,i::10,j::10] for i in xrange(10) for j in xrange(10)]
    rdata = ma.array(rdata) 
    
    print rdata.shape

.. parsed-literal::

    (100, 154, 36, 72)


So, we have made the dataset which as ``(154, 360, 720)`` into a shape
``(100, 154, 36, 72)``.

We can now get the total fire counts easily at 5 degrees by summing over
those 100 cells (axis=0):

.. code:: python

    fdata = rdata.sum(axis=0)
    print fdata.shape
    
    lf = np.log(fdata)
    vmax = np.max(lf[lf>0])
    
    plt.figure(figsize=(10,5))
    plt.imshow(lf[8],interpolation='nearest',vmax=vmax)
    plt.colorbar()
    plt.title('log fire count for %d month %02d'%(year[8],month[8]))

.. parsed-literal::

    (154, 36, 72)




.. parsed-literal::

    <matplotlib.text.Text at 0x7fe706560390>




.. image:: ENSO_files/ENSO_17_2.png


.. code:: python

    # or even make a movie
    lf = np.log(fdata)
    vmax = np.max(lf[lf>0])
    
    root = 'images/'
    for i in xrange(lf.shape[0]):
        fig = plt.figure(figsize=(10,5))
        plt.imshow(np.log(fdata[i]),interpolation='nearest',vmax=vmax)
        plt.colorbar()
        file_id = '%d month %02d'%(year[i],month[i])
        plt.title('log fire count for %s'%file_id)
        plt.savefig('%s_%s.jpg'%(root,file_id.replace(' ','_')))
        plt.close(fig)
.. code:: python

    cmd = 'convert -delay 100 -loop 0 {0}_*month*.jpg {0}fire_movie3.gif'.format(root)
    os.system(cmd)



.. parsed-literal::

    0



.. figure:: files/images/fire_movie3.gif
   :alt: 

The information we want is the peak fire count and to know which month
this occurred in.

To do this, we might reoder the data first:

.. code:: python

    nlatlon = fdata.shape[1:]
    min_year = year[0]
    max_year = year[-1]
    # number of years
    nyears = max_year - min_year + 1
    
    # set up a big array
    f2data  = np.zeros((12,nyears)+nlatlon)
    f2datam = np.ones((12,nyears)+nlatlon).astype(bool)
    
    for i,(y,m) in enumerate(zip(year-year[0],month-1)):
        f2data[m,y] = fdata[i]
        f2datam[m,y] = (fdata[i] <= 0)
    # mask it
    f2data = ma.array(f2data,mask=f2datam)
    print f2data.shape
    
    # test it
    m = 8
    y = 2005
    plt.figure(figsize=(10,5))
    plt.imshow(np.log(f2data[m-1,y-year[0]]),interpolation='nearest')
    plt.colorbar()
    plt.title('log fire count for %d month %02d'%(y,m))

.. parsed-literal::

    (12, 14, 36, 72)




.. parsed-literal::

    <matplotlib.text.Text at 0x7fe715cfb510>




.. image:: ENSO_files/ENSO_22_2.png


.. code:: python

    # which month has the highest fire count
    # NB 0-based here but we use a masked array
    
    # total fire count summed over month (axis 0)
    fmask = f2data.sum(axis=0) == 0
    
    # which month (axis 0) has the max value?
    fire_month = np.argmax(f2data,axis=0)
    
    # masked array of this
    fire_month = ma.array(fire_month,mask=fmask)
    
    y = 2005
    plt.figure(figsize=(10,5))
    plt.imshow(fire_month[y-year[0]],interpolation='nearest')
    plt.colorbar()
    plt.title('Peak fire month for %d'%(y))
    
    # suppose this is the same for all years:
    av_fire_month = np.median(fire_month,axis=0).astype(int)
    plt.figure(figsize=(10,5))
    plt.imshow(av_fire_month,interpolation='nearest')
    plt.colorbar()
    plt.title('Average peak fire month')



.. parsed-literal::

    <matplotlib.text.Text at 0x7fe7062909d0>




.. image:: ENSO_files/ENSO_23_1.png



.. image:: ENSO_files/ENSO_23_2.png


.. code:: python

    # and now get the fire count for that month
    # lets try this by hand first
    
    peak_count = np.zeros_like(f2data[0])
    
    y = 2001
    m = 0
    
    fmask = (av_fire_month == m)
    peak_count[y-year[0]][fmask] = f2data[m,y-year[0]][fmask]

.. code:: python

    # and now extend it
    peak_count = np.zeros_like(f2data[0])
    
    for m in xrange(f2data.shape[0]):
        fmask = (av_fire_month == m)
        for y in xrange(f2data.shape[1]):
            peak_count[y][fmask] = f2data[m,y][fmask]
            
    
    # test it
    y = 1
    plt.figure(figsize=(10,5))
    plt.imshow(np.log(peak_count[y]),interpolation='nearest')
    plt.colorbar()
    plt.title('Log Peak count for year %d'%(min_year+y))



.. parsed-literal::

    <matplotlib.text.Text at 0x7fe706330f10>




.. image:: ENSO_files/ENSO_25_1.png


.. code:: python

    # In summary, we have developed the following datasets:
    
    print 'peak_count',peak_count.shape
    print 'av_fire_month',av_fire_month.shape
    print 'min_year',min_year

.. parsed-literal::

    peak_count (14, 36, 72)
    av_fire_month (36, 72)
    min_year 2000


Climate Data
^^^^^^^^^^^^

The climate data you will want will be some form of Sea Surface
Temperature (SST) anomaly measure. There is a long list of such measures
on
`http://www.esrl.noaa.gov/psd/data/climateindices/list <http://www.esrl.noaa.gov/psd/data/climateindices/list/>`__.

Examples would be
`AMO <http://www.esrl.noaa.gov/psd/data/correlation/amon.us.data>`__ or
`ONI <http://www.esrl.noaa.gov/psd/data/correlation/oni.data>`__. Note
that some of these measures are smoothed and others not.

Suppose we had selected AMO and we want to read directly from the url:

.. code:: python

    import urllib2
    
    url = 'http://www.esrl.noaa.gov/psd/data/correlation/amon.us.data'
    
    req = urllib2.Request ( url )
    raw_data = urllib2.urlopen(req).readlines()
.. code:: python

    # we notice from inspection that 
    # we want data from rows 1 to -4
    raw_data[:2]



.. parsed-literal::

    ['  1948         2014\n',
     ' 1948   -0.006   -0.018    0.037   -0.061    0.005    0.064   -0.030   -0.013   -0.043    0.017    0.144    0.072\n']



.. code:: python

    raw_data[-10:-4]



.. parsed-literal::

    [' 2009   -0.039   -0.145   -0.141   -0.111   -0.042    0.141    0.247    0.172    0.077    0.184    0.089    0.102\n',
     ' 2010    0.059    0.197    0.307    0.445    0.479    0.467    0.470    0.545    0.469    0.344    0.255    0.227\n',
     ' 2011    0.163    0.128    0.075    0.112    0.172    0.198    0.111    0.167    0.164    0.083   -0.051   -0.025\n',
     ' 2012   -0.045    0.024    0.046    0.100    0.184    0.320    0.395    0.451    0.468    0.349    0.185    0.161\n',
     ' 2013    0.148    0.135    0.178    0.156    0.121    0.066    0.210    0.214    0.275    0.367    0.148    0.056\n',
     ' 2014   -0.042   -0.023   -0.061   -0.074    0.019    0.082    0.242    0.355    0.328    0.312  -99.990  -99.990\n']



.. code:: python

    cdata = np.array([r.split() for r in raw_data[1:-4]]).astype(float)
    
    cmask = (cdata < -50 )
    cdata = ma.array(cdata,mask=cmask).T
    cyears = cdata[0]
    cdata = cdata[1:]
    
    # now we have the climate data as a masked array
    # column 0 is years, column 1 is Jan etc.
.. code:: python

    plt.plot(cyears,cdata[0])
    plt.xlabel('year')
    plt.ylabel('January AMO')
    print cdata.shape

.. parsed-literal::

    (12, 67)



.. image:: ENSO_files/ENSO_32_1.png


7.2.4 Code to perform correlation analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The idea here is, for a particular (or set of) SST anomaly measures,
work out which ‘lag’ month gives the highest correlation coefficient
with fire count.

By ‘lag’ month, we mean that e.g. if the peak fire month for a
particular pixel was September, which month prior to that has a set of
SST anomalies over the sample years that is most strongly correlated
with fire count.

So, if we were using a single SST anomaly measure (e.g. AMO or ONI) and
sample years 2001 to 2009 to build our model, then we would do a linear
regression of fire count for a particular pixel over these years against
e.g. AMO data for September (lag 0) then August (lag 1) then July (lag
2) etc. and see which produced the highest :math:`R^2`.

Before we get into that, let's look again at the data structure we have:

.. code:: python

    # climate data
    print 'cdata',cdata.shape
    print 'cyears',cyears.shape
    
    # From the fire data
    
    print 'peak_count',peak_count.shape
    print 'av_fire_month',av_fire_month.shape
    print 'min_year',min_year

.. parsed-literal::

    cdata (12, 67)
    cyears (67,)
    peak_count (14, 36, 72)
    av_fire_month (36, 72)
    min_year 2000


So, if we want to select data for particular years:

.. code:: python

    # which years (inclusive)
    years = [2001,2010]
    
    ypeak_count = peak_count[years[0]-min_year:years[1] - min_year + 1]
    ycdata  =  cdata[:,years[0] - cyears[0]:years[1] - cyears[0] + 1]
    
    # check the shape
    print ycdata.shape,ypeak_count.shape,av_fire_month.shape

.. parsed-literal::

    (12, 10) (10, 36, 72) (36, 72)


We need to consider a little carefully the implementation of lag ...

.. code:: python

    # we will need to access ycdata[month - n][year]
    # which is a bit fiddly as e.g. -3 will be interpreted as
    # October for that same year, rather than the previous year
    y = 2001 - min_year
    m = 2
    lag = 5
    print m - lag,y

.. parsed-literal::

    -3 1


.. code:: python

    # so one way to fix this is to decrease y by one
    # if m - lag is -ve
    Y = y - (m - lag < 0)
    print m-lag,Y

.. parsed-literal::

    -3 0


.. code:: python

    from scipy.stats import linregress
    
    # examine an example row col
    # for a given month over all years
    
    c = 24
    r = 19
    m = av_fire_month[r,c]
    # pull the data
    yyears = np.arange(years[1]-years[0]+1)
    
    R2 = np.array([linregress(\
                ycdata[m-n,yyears - (m - n < 0)],\
                ypeak_count[yyears - (m - n < 0),r,c]\
            )[2] for n in xrange(12)])
    
    n = np.argmax(R2)
    
    x  = ycdata[m-n,yyears - (m - n < 0)]
    y = ypeak_count[yyears - (m - n < 0),r,c]
    slope,intercept,R,p,err = linregress(x,y)
    
    print slope,intercept,p,err
    plt.plot(ycdata[m-n],y,'r+')
    plt.xlabel('Climate Index')
    plt.ylabel('Fire count')
    plt.plot([x.min(),x.max()],\
             [intercept+slope*x.min(),intercept+slope*x.max()],'k--')
    plt.title('Fire count at r %03d c %03d: R^2 = %.3f: lag %d'%(r,c,R2[n],n))

.. parsed-literal::

    10797.4828941 2787.9505669 0.0231916998529 3856.00735281




.. parsed-literal::

    <matplotlib.text.Text at 0x7fe706aae3d0>




.. image:: ENSO_files/ENSO_41_2.png


.. code:: python

    # looper
    
    data_mask = ypeak_count.sum(axis=0)>100
    
    rs,cs = np.where(data_mask)
    
    results = {'intercept':0,'slope':0,'p':0,'R':0,'stderr':0,'lag':0}
    for k in results.keys():
        results[k] = np.zeros_like(av_fire_month).astype(float)
        results[k] = ma.array(results[k],mask=~data_mask)
        
    for r,c in zip(rs,cs):
        m = av_fire_month[r,c]
        # pull the data
        yyears = np.arange(years[1]-years[0]+1)
        R2 = np.array([\
                linregress(\
                    ycdata[m-n,yyears - (m - n < 0)],\
                    ypeak_count[yyears - (m - n < 0),r,c]\
                )[2] for n in xrange(12)])
        
        n = np.argmax(R2)
        results['lag'][r,c] = n
        x  = ycdata[m-n,yyears - (m - n < 0)]
        y = ypeak_count[yyears - (m - n < 0),r,c]
        results['slope'][r,c],results['intercept'][r,c],\
        results['R'][r,c],results['p'][r,c],\
        results['stderr'][r,c] = linregress(x,y)

.. code:: python

    plt.figure(figsize=(10,4))
    plt.imshow(results['R'],interpolation='nearest')
    plt.colorbar()
    plt.title('R')
    
    plt.figure(figsize=(10,4))
    plt.imshow(results['p'],interpolation='nearest')
    plt.colorbar()
    plt.title('p')
    
    
    plt.figure(figsize=(10,4))
    plt.imshow(results['slope'],interpolation='nearest')
    plt.colorbar()
    plt.title('slope')
    
    
    plt.figure(figsize=(10,4))
    plt.imshow(results['lag'],interpolation='nearest')
    plt.colorbar()
    plt.title('lag')



.. parsed-literal::

    <matplotlib.text.Text at 0x7fe716362510>




.. image:: ENSO_files/ENSO_43_1.png



.. image:: ENSO_files/ENSO_43_2.png



.. image:: ENSO_files/ENSO_43_3.png



.. image:: ENSO_files/ENSO_43_4.png


which we can now predict:

.. code:: python

    # prediction year
    pyear = 2012
    
    # which month?
    M = av_fire_month - results['lag']
    Y = np.zeros_like(M) + pyear
    Y[M<0] -= 1
.. code:: python

    # lets look at that ...
    plt.imshow(Y,interpolation='nearest')



.. parsed-literal::

    <matplotlib.image.AxesImage at 0x7fe717339590>




.. image:: ENSO_files/ENSO_46_1.png


.. code:: python

    # climate data
    scdata = np.zeros_like(Y).astype(float)
    
    for y in [pyear,pyear-1]:
        for m in xrange(12):
            scdata[(Y == y) & (M == m)] = cdata[m,y-cyears[0]]
    
    plt.imshow(scdata,interpolation='nearest')



.. parsed-literal::

    <matplotlib.image.AxesImage at 0x7fe71674f450>




.. image:: ENSO_files/ENSO_47_1.png


.. code:: python

    # now predict
    
    fc_predict = results['intercept'] + results['slope'] * scdata
    
    plt.figure(figsize=(10,4))
    plt.imshow(fc_predict,interpolation='nearest',vmin=0,vmax=10000)
    plt.colorbar()
    plt.title('predicted peak fire count for %d'%pyear)
    
    plt.figure(figsize=(10,4))
    plt.imshow(peak_count[pyear-min_year],\
               interpolation='nearest',vmin=0,vmax=10000)
    plt.colorbar()
    plt.title('actual peak fire count for %d'%pyear)



.. parsed-literal::

    <matplotlib.text.Text at 0x7fe716431250>




.. image:: ENSO_files/ENSO_48_1.png



.. image:: ENSO_files/ENSO_48_2.png


.. code:: python

    x = peak_count[pyear-min_year].flatten()
    y = fc_predict.flatten()
    
    slope,intercept,R,p,err = linregress(x,y)
    
    plt.plot(x,y,'+')
    plt.xlabel('measured fire count')
    plt.ylabel('predicted fire count')
    cc = np.array([0.,x.max()])
    
    plt.plot(cc,cc,'k--')
    plt.plot(cc,slope*cc+intercept,'k-')
    plt.title('fire count predictions')
    print slope,intercept,R,p,err

.. parsed-literal::

    0.805181670827 -6.33987111286 0.882914718951 0.0 0.00841379095649



.. image:: ENSO_files/ENSO_49_1.png

