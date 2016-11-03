file = "files/data/Hydrologic_Units/HUC_Polygons.shp"

import sys
sys.path.insert(0,'files/python')

from raster_mask import *

modis_file = 'files/data/MYD10A1.A2003026.h09v05.005.2008047035848.hdf'
data_layer = 'MOD_Grid_Snow_500m:Fractional_Snow_Cover'
fname = 'HDF4_EOS:EOS_GRID:"%s":%s'%(modis_file,data_layer)

m = raster_mask2(fname,\
                target_vector_file="files/data/Hydrologic_Units/HUC_Polygons.shp",\
                attribute_filter=2)
