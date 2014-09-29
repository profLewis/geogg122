
.. code:: python

    %pylab inline
    %config InlineBackend.figure_format = 'svg'

.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib


Incoming solar radiation
========================

Incoming solar radiation, :math:`A`, ignoring the effect of the
atmosphere, clouds, etc is given by

.. math::


   A = E_{0}\sin\theta

where :math:`E_{0}` is the solar constant (given as
:math:`1360Wm^{-2}`), and :math:`\theta` is the `solar elevation
angle <http://en.wikipedia.org/wiki/Solar_elevation_angle#Solar_elevation_angle>`__.
The solar elevation angle is approximately given by

.. math::


   \sin \theta = \cos h \cos \delta \cos \varphi + \sin \delta \sin \varphi

where :math:`h` is the `hour
angle <http://en.wikipedia.org/wiki/Hour_angle#Solar_hour_angle>`__,
:math:`\delta` is the `solar declination
angle <http://en.wikipedia.org/wiki/Position_of_the_Sun#Calculations>`__
and :math:`\varphi` is the latitude. The solar declination can be
approximated by

.. math::


   \delta = - \arcsin \left [ 0.39779 \cos \left ( 0.98565 \left (N + 10 \right ) + 1.914 \sin \left ( 0.98565 \left ( N - 2 \right ) \right ) \right ) \right ]

where :math:`N` is the day of year beginning with N=0 at 00:00:00 UTC on
January 1

.. code:: python

    e0 = 1360.
    latitude = np.deg2rad ( 45. )
    N = np.arange ( 0.5, 366, 1 )
    h = -22.5
    t0 = np.deg2rad (0.98565*(N-2))
    t1 = 0.39779*np.cos( np.deg2rad ( 0.98565*(N+10) + 1.914*np.sin ( t0 ) ) )
    t2 = -np.arcsin ( t1 )
    
    sin_theta = np.cos (np.deg2rad(h))*np.cos (t2)*np.cos(latitude) + np.sin ( t2)*np.sin(latitude)
    incoming_rad = e0*sin_theta
    plt.plot ( N, incoming_rad , label="10:30AM")
    h = 0
    t0 = np.deg2rad (0.98565*(N-2))
    t1 = 0.39779*np.cos( np.deg2rad ( 0.98565*(N+10) + 1.914*np.sin ( t0 ) ) )
    t2 = -np.arcsin ( t1 )
    
    sin_theta = np.cos (np.deg2rad(h))*np.cos (t2)*np.cos(latitude) + np.sin ( t2)*np.sin(latitude)
    incoming_rad = e0*sin_theta
    
    plt.plot ( N, incoming_rad , label="12:00PM")
    
    plt.xlabel("Day of Year")
    plt.ylabel('Incoming solar radiation $[W\\cdot m^{-2}]$')



.. parsed-literal::

    <matplotlib.text.Text at 0x4543590>




.. image:: solar_radiation_files/solar_radiation_3_1.svg

