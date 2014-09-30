
.. code:: python

    # example of importing a module 
    # here, we want the method factorial
    # from the library called math
    from math import factorial
    
    # perform an inefficient prime number test
    # 
    # Wilson's theorum 
    # http://mathworld.wolfram.com/WilsonsTheorem.html
    # states that p is a prime number 
    # iff (p-1)! == -1, mod p
    
    # test number
    p = 7919
    
    # calculate the factorial
    p1_fact = factorial(p-1)
    
    # do the comparison in modulo p
    is_prime = (p1_fact % p == -1 % p)
    
    if is_prime:
        print p,"is a prime number"
    else:
        print p,"is not a prime number"

.. parsed-literal::

    7919 is a prime number


As an example of data masking, consider the QA mask in the `MODIS Leaf
Area Index
(LAI) <https://lpdaac.usgs.gov/products/modis_products_table/leaf_area_index_fraction_of_photosynthetically_active_radiation/8_day_l4_global_1km/mod15a2>`__
product:

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Bit number

.. raw:: html

   </td>

.. raw:: html

   <td>

Parameter Name

.. raw:: html

   </td>

.. raw:: html

   <td>

Bit combination

.. raw:: html

   </td>

.. raw:: html

   <td>

Interpretation

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

0

.. raw:: html

   </td>

.. raw:: html

   <td>

MODLAND\_QC bits

.. raw:: html

   </td>

.. raw:: html

   <td>

0

.. raw:: html

   </td>

.. raw:: html

   <td>

Good quality (main algorithm with or without saturation)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

1

.. raw:: html

   </td>

.. raw:: html

   <td>

Other Quality (back-up algorithm or fill values)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

1

.. raw:: html

   </td>

.. raw:: html

   <td>

Sensor

.. raw:: html

   </td>

.. raw:: html

   <td>

0

.. raw:: html

   </td>

.. raw:: html

   <td>

Terra

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

1

.. raw:: html

   </td>

.. raw:: html

   <td>

Aqua

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

2

.. raw:: html

   </td>

.. raw:: html

   <td>

DeadDetector

.. raw:: html

   </td>

.. raw:: html

   <td>

0

.. raw:: html

   </td>

.. raw:: html

   <td>

Detectors apparently fine for up to 50% of channels

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

1

.. raw:: html

   </td>

.. raw:: html

   <td>

Dead detectors caused >50% adjacent detector retrieval

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

3-4

.. raw:: html

   </td>

.. raw:: html

   <td>

CloudState

.. raw:: html

   </td>

.. raw:: html

   <td>

00

.. raw:: html

   </td>

.. raw:: html

   <td>

Significant clouds NOT present (clear)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

01

.. raw:: html

   </td>

.. raw:: html

   <td>

Significant clouds WERE present

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

10

.. raw:: html

   </td>

.. raw:: html

   <td>

Mixed cloud present on pixel

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

11

.. raw:: html

   </td>

.. raw:: html

   <td>

Cloud state not defined (assumed clear)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

5-7

.. raw:: html

   </td>

.. raw:: html

   <td>

CF\_QC

.. raw:: html

   </td>

.. raw:: html

   <td>

000

.. raw:: html

   </td>

.. raw:: html

   <td>

Main (RT) method used (best result possible (no saturation))

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

001

.. raw:: html

   </td>

.. raw:: html

   <td>

Main (RT) method used with saturation. (usable)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

010

.. raw:: html

   </td>

.. raw:: html

   <td>

Main (RT) method failed due to bad geometry (empirical algorithm used)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

010

.. raw:: html

   </td>

.. raw:: html

   <td>

Main (RT) method failed due to problems other than geometry (empirical
algorithm used)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

010

.. raw:: html

   </td>

.. raw:: html

   <td>

Pixel not produced at all.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

So, the MODIS LAI QA information is contained in one byte (8 bits),
which encodes data about five different categories of QA information.

When using such data, we need to make choices about what quality of data
we are willing to accept.

For the moment, you can ignore this piece of code below. We will learn
of such things later, but here we read in some data into a variable
``qa``, and diaplay those data:

.. code:: python

    # jump ahead a bit in the course
    # to read some data in from a npz file
    # and show it
    import numpy as np
    f = np.load('data/MCD15A2.A2011185.h09v05.005.npz')
    lai = f['lai']
    lai_sd = f['lai_sd']
    qa = f['qc']
    plt.imshow(qa)
    plt.colorbar()



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0x106b92320>




.. image:: spares_files/spares_3_1.png


We now want to be able to interpret those qa codes:

From the table above, we want to access the ``MODLAND_QC bits`` which
are in the first bit of this:

We can simply access this applying a bitwise and operation with bit mask
of value 1 (to pull the information on the first bit). This then will
have values of zero or one. We can convert these to ``bool``,so now zero
values are ``False``.

The table above tells us that we want values of zero here, so we take a
ones complement so that ``mask`` is ``True`` where we want the data.

.. code:: python

    mask = ~((qa & 0b1).astype(bool))
    plt.imshow(mask,interpolation='nearest')
    plt.colorbar()



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0x11401d8c0>




.. image:: spares_files/spares_5_1.png


.. code:: python

    mask = ~((qa & 0b1).astype(bool))
    plt.imshow(lai*mask,interpolation='nearest')
    plt.colorbar()



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0x115143d40>




.. image:: spares_files/spares_6_1.png


.. code:: python

    mask = ~((qa & 0b1).astype(bool))
    plt.imshow(lai_sd*mask,interpolation='nearest')
    plt.colorbar()



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0x1151cfef0>




.. image:: spares_files/spares_7_1.png


