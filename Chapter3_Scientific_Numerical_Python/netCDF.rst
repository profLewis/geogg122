
How to read netCDF files if the format is not included in gdal
==============================================================

On the whole, we use ``gdal`` in these notes for consistency. The
package understands many file formats, but is generally *not* compiled
with netCDF. You *can* recompile the library, but it is often easier to
use a different package to read netCDF files.

First, we will see if ``gdal`` is working as we wish:

.. code:: python

    import gdal
    # example filename : use formatting string:
    # %d%02d
    layer = 'DHR_VIS'
    year = 2009
    month = 1
    filename = 'data/GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
    template = 'NETCDF:"%s":%s'%(filename,layer)
    
    print filename
    
    # this is is way we read a data layer using gdal
    try:
        data = gdal.Open(template).ReadAsArray()
    except:
        print 'unable to open netcdf file'


.. parsed-literal::

    data/GlobAlbedo.200901.mosaic.5.nc
    unable to open netcdf file


So, let's try an alternative.

.. code:: python

    from scipy.io import netcdf
    
    # example filename : use formatting string:
    # %d%02d
    layer = 'DHR_VIS'
    year = 2009
    month = 1
    filename = 'data/GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
    print filename
    
    data = netcdf.netcdf_file(filename,'r').variables[layer]
    
    print data

.. parsed-literal::

    data/GlobAlbedo.200901.mosaic.5.nc
    <scipy.io.netcdf.netcdf_variable object at 0x10a828910>


which does work with defalt packages and settings.

Note that at this point, the contents are not yet read from disk into
the array ``data``. If we want to force that, use:

.. code:: python

    data = netcdf.netcdf_file(filename,'r').variables[layer][:]
If you want to wrap this up into a ``readGA`` method as in the notes,
but still try ``gdal``:

.. code:: python

    import gdal
    
    def readGA(root='data/',year=2009,month=1,layer = 'BHR_VIS'\
               ,filename=None):
        '''
        Method to read a GlobAlbedo file
        '''
        file_template = 'NETCDF:"%s":%s'
    
        filename = filename or root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
    
        try:
            # try gdal
            data = gdal.Open (  file_template % ( filename, layer ) ).ReadAsArray()
        except:
            # nope ... so try netcdf library
            from scipy.io import netcdf
            data = netcdf.netcdf_file(filename,'r').variables[layer][:]
            
        # return a numpy array
        return(np.array(data))
.. code:: python

    data = readGA()
