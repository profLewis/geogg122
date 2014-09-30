
Recollision Probability Theory
==============================

A useful source of information quantifying vegetation amount is the Leaf
Area Index (LAI). To interpret LAI from satellite data, we build models
of radiative transfer.

One of the simplest such models that we can use at optical wavelengths
uses what is known as 'p theory' or 'recollision probability theory'
(Lewis and Disney, 2007; Huang et al., 2007).

**The task today is to use p-theory to estimate LAI over some
agricultural fields.**

References

-  P. Lewis and M. Disney (2007) Spectral invariants and scattering
   across multiple scales from within-leaf to canopy, `Remote Sensing of
   Environment 109,
   196-206. <http://www2.geog.ucl.ac.uk/~mdisney/papers/lewis_disney_prospect.pdf>`__
-  D. Huang, Y. Knyazikhin, R.E. Dickinson, M. Rautiainen, P. Stenberg,
   M. Disney, P. Lewis, A. Cescatti, Y. Tian, W. Verhoef, and R.B.
   Myneni (2007), Canopy spectral invariants for remote sensing and
   model applications, `Remote Sensing of Environment, 106,
   106-122 <http://www2.geog.ucl.ac.uk/~plewis/Huang_Spectral_Revised.pdf>`__
-  Knyazikhin Y, Schull MA, Stenberg P, Mottus M, Rautiainen M, Yang Y,
   Marshak A, Latorre Carmona P, Kaufmann RK, Lewis P, Disney MI,
   Vanderbilt V, Davis AB, Baret F, Jacquemoud S, Lyapustin A, Myneni
   RB. (2013) Hyperspectral remote sensing of foliar nitrogen content.
   Proc Natl Acad Sci USA,
   `10.1073/pnas.1210196109 <http://cybele.bu.edu/download/manuscripts/knyazikhin-pnas-hypspec.pdf>`__.

Data
====

The dataset you have available is an airborne hyperspectral image
(HYMAP) dataset for which you have a 512x512 pixel subscene taken in 125
wavebands with a spatial resolution of 4m. The data were obtained on 17
June 2000 over Barton Bendish Farms, Norfolk during the BNSC/NERC SHAC
campaign.

The data are available as a compressed *flat binary* file in the
directory ```files/data`` <files/data>`__.

First, uncompress the dataset:

.. code:: python

    # or try zcat if gzcat isnt there
    !gzcat files/data/bbHYMAP.dat.gz > files/data/bbHYMAP.dat
.. code:: python

    !ls -l files/data/bbHYMAP.dat

.. parsed-literal::

    -rw-r--r--  1 plewis  staff  131072000 26 Nov 17:31 files/data/bbHYMAP.dat


The file is 131072000 bytes in 32 bit floating point format:

.. code:: python

    print 'nbands =',131072000/(512*512*4)

.. parsed-literal::

    nbands = 125


.. code:: python

    # we wuill use memmap to read the data in
    from numpy import memmap
.. code:: python

    hymap = memmap('files/data/bbHYMAP.dat',dtype=np.float32,mode='r',shape=(125,512,512))
.. code:: python

    plt.imshow(hymap[10],interpolation='nearest')



.. parsed-literal::

    <matplotlib.image.AxesImage at 0x10598edd0>




.. image:: Ptheory_files/Ptheory_10_1.png


The wavelengths associated with each band are stored in
```files/data/wavebands.dat`` <files/data/wavebands.dat>`__.

.. code:: python

    mean = hymap.mean(axis=(1,2))
    wavelength = np.loadtxt('files/data/wavebands.dat')
    plt.plot(wavelength,mean)



.. parsed-literal::

    [<matplotlib.lines.Line2D at 0x10f089790>]




.. image:: Ptheory_files/Ptheory_12_1.png


Theory
======

The simplest form of model in p-theory assumes that the photon
recollision probability is constant with wavelength and scattering
order. Under this assumption, the total scattering from the canopy,
:math:`W` is:

.. math::


   W = i_0 \frac{(1 - p) \omega}{1 - p \omega}

where :math:`i_0` is the canopy interception probability, :math:`\omega`
is the leaf-level scattering (the leaf single scattering albedo) and
:math:`p` is the recollision probability: the probability that a photon,
having intercepted a canopy element, will recollide with another element
rather than escape the canopy.

We can develop from this a model of the canopy *reflectance*
:math:`\rho` (i.e. that portion scattered upwards, perhaps in a
particular direction):

.. math::


   \rho = \frac{a \omega}{1 - p \omega}

For a closed canopy, or one with only little soil influence, this will
describe the spectral reflectance for some given leaf single scattering
albedo spectrum and given :math:`p`.

If we know :math:`\omega` then, and have a measurement of :math:`\rho`,
we can estimate :math:`p`. From :math:`p`, we can estimate LAI according
to Lewis and Disney (2007) by:

.. math::


   p = 0.88 \left( 1 - exp(- 0.7 LAI^{0.75}) \right)

.. code:: python

    LAI = np.arange(0,12,0.01)
    p = 0.88*(1 - np.exp(-0.7 * LAI**0.75))
    plt.plot(LAI,p)
    plt.xlabel('LAI')
    plt.ylabel('p')



.. parsed-literal::

    <matplotlib.text.Text at 0x10f12f0d0>




.. image:: Ptheory_files/Ptheory_15_1.png


There are several ways we could estimate :math:`p`. An interesting
feature exploited by Knyazikhin et al. (2013) follows from:

.. math::


   \frac{\rho}{\omega} = \frac{a}{1 - p \omega}

so

.. math::


   \frac{\rho}{\omega}  = a + p \rho

So that if we plot :math:`\frac{\rho}{\omega}` as a function of
:math:`\rho`, this theory predicts we should see a straight line.

An example leaf single scattering albedo is given in
```files/data/ssalbedo.dat`` <files/data/ssalbedo.dat>`__:

.. code:: python

    ssalbedo = np.loadtxt('files/data/ssalbedo.dat').T
    plt.plot(ssalbedo[0],ssalbedo[1])
    plt.xlabel('wavelength / nm')
    plt.ylabel('single scattering albedo')
    plt.xlim(ssalbedo[0][0],ssalbedo[0][-1])



.. parsed-literal::

    (400.0, 2400.0)




.. image:: Ptheory_files/Ptheory_17_1.png


which is sampled every 1 nm from 400 to 2400 nm.

We will clearly need to resample this to the same wavebands as the
hyperspectral data:

.. code:: python

    from scipy.interpolate import interp1d
    from scipy.stats import linregress
.. code:: python

    f = interp1d(ssalbedo[0],ssalbedo[1])
    omega = f(wavelength[wavelength<=2400])
The theory becomes more complicated when multiple absorbing constituents
are involved, so we select here only wavelengths between 710 and 790 nm
(on the 'red edge'), where the main absorbing constituent is
chlorophyll.

.. code:: python

    # wavelength
    W = (wavelength >= 710) & (wavelength <= 790)
    
    wave = wavelength[W]
    # single scattering albedo
    omega = f(wavelength[W])
    # reflectance
    rho = hymap[W]
.. code:: python

    # lets see if its a straight line!
    mean = rho.mean(axis=(1,2))
    plt.plot(mean,mean/omega,'+')
    
    # linear fit
    slope, intercept, r_value, p_value, std_err = linregress(mean,mean/omega)
    x = np.array([mean[0],mean[-1]])
    plt.plot(x,x*slope+intercept)
    print 'slope',slope,'intercept',intercept

.. parsed-literal::

    slope 0.710882123721 intercept 0.125383329915



.. image:: Ptheory_files/Ptheory_23_1.png


So, here, :math:`p` is 0.71088

.. code:: python

    #p = 0.88*(1 - np.exp(-0.7 * LAI**0.75))
    LAI = (np.log(1 - slope/0.88)/-0.7)**(4./3.)
    print LAI

.. parsed-literal::

    3.13529156174


Following Knyazikhin et al. (2013) we can calculate the ``DASF``
(Directional Area Scattering Function) from:

.. code:: python

    DASF = intercept/(1 - slope)
    print DASF

.. parsed-literal::

    0.43367546666


and from that, :math:`W`:

.. code:: python

    W = mean/DASF
    plt.plot(wave,W)
    plt.plot(wave,omega)



.. parsed-literal::

    [<matplotlib.lines.Line2D at 0x11b5d1410>]




.. image:: Ptheory_files/Ptheory_29_1.png


which in turn can give access to leaf biochemistry.

The Task
========

The output of this exercise should be a spatial dataset of LAI.

The processing for this task is quite straightforward, and you *should*
be able to develop a neat algorithm given the information above.

You should work in teams for this exercise as in previous weeks, and
assign tasks for people to complete after you have discussed an overall
algorithm and defined any interfaces you will need.

If you finish the task quickly, you could explore the impact of the the
leaf single scattering albedo assumed, and/or examine the impact of
widening the wavelength range used here.
