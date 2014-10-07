import numpy as np
import numpy.ma as ma
import gdal


def masked(root='data/',years=[2009],months=[],\
            layers = ['BHR_VIS']):
    '''
    Method to read GlobAlbedo files
    '''
    file_template = 'NETCDF:"%s":%s'
    
    if len(months) == 0:
        months = xrange(1,13)
    
    
    data = []   
 
    for year in years:
        for month in months:
            for layer in layers:

                # what does this do???
                filename = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)

                g = gdal.Open (  file_template % ( filename, layer ) )

                if g is None:
                  raise IOError
                band = g.ReadAsArray()
                masked_band = ma.array(band,mask=np.isnan(band))
                data.append(masked_band)
    return(ma.array(data))

