import numpy as np
import numpy.ma as ma
import gdal

def get_lai(filename, \
           qc_layer = 'FparLai_QC',\
           scale = [0.1, 0.1],\
           selected_layers = ["Lai_1km", "LaiStdDev_1km"]):

    # get the QC layer too
    selected_layers.append(qc_layer)
    scale.append(1)
    # We will store the data in a dictionary
    # Initialise an empty dictionary
    data = {}
    # for convenience, we will use string substitution to create a 
    # template for GDAL filenames, which we'll substitute on the fly:
    file_template = 'HDF4_EOS:EOS_GRID:"%s":MOD_Grid_MOD15A2:%s'
    # This has two substitutions (the %s parts) which will refer to:
    # - the filename
    # - the data layer
    for i,layer in enumerate(selected_layers):
        this_file = file_template % ( filename, layer )
        g = gdal.Open ( this_file )

        if g is None:
            raise IOError

        data[layer] = g.ReadAsArray() * scale[i]

    qc = data[qc_layer] # Get the QC data
    # find bit 0
    qc = qc & 1

    odata = {}
    for layer in selected_layers[:-1]:
        odata[layer] = ma.array(data[layer],mask=qc)

    return odata

# thats quite good, so put as a function:
import numpy.ma as ma
import numpy as np
import sys
sys.path.insert(0,'files/python')
from get_lai import get_lai
from raster_mask import raster_mask


def read_lai(filelist,datadir='files/data',country=None):
    '''
    Read MODIS LAI data from a set of files
    in the list filelist. Data assumed to be in
    directory datadir.
    
    Parameters:
    filelist : list of LAI files
    
    Options:
    datadir  : data directory
    country  : country name (in files/data/world.shp)
    
    Returns:
    lai dictionary
    '''
    fields = {'LaiStdDev_1km':[],'Lai_1km':[]}
    
    # make a dictionary
    lai = {'filenames':np.sort(filelist)}
    lai.update(fields)
    
    # make a raster mask
    # from the layer IRELAND in world.shp
    filename = lai['filenames'][0]
    file_template = 'HDF4_EOS:EOS_GRID:"%s":MOD_Grid_MOD15A2:%s'
    file_spec = file_template%('files/data/%s'%filename,'Lai_1km')
                            
    if country:
        mask = raster_mask(file_spec,\
                       target_vector_file = "files/data/world.shp",\
                       attribute_filter = "NAME = '%s'"%country)
        all_mask = ~mask
        coords = np.where(all_mask)
        # find the min/max extent of these
        cmin = np.min(coords,axis=1)
        cmax = np.max(coords,axis=1)
        mask = mask[cmin[0]:cmax[0]+1,cmin[1]:cmax[1]+1]

    for f in np.sort(lai['filenames']):
        # would be more efficient to just read
        # the required area
        this_lai = get_lai('files/data/%s'%f)
        for layer in fields.keys():
            if country:
              this_lai[layer] = \
		this_lai[layer][cmin[0]:cmax[0]+1,cmin[1]:cmax[1]+1]
            lai[layer].append(this_lai[layer])
    
    # put the mask in
    for layer in fields.keys():
        # first convert the list to a masked array
        masked = ma.array(lai[layer])
        if country:
            # then and it with the country mask
            lai[layer] = ma.array(lai[layer],mask=(mask | masked.mask)) 
        else:
            lai[layer] = masked

    if not country:            
      # a little bit of code to extract just the part we want ...
      # sum the mask to see where there are valid data
      all_mask = (~lai[selected_layers[0]].mask).sum(axis=0)
      mask = np.zeros_like(all_mask).astype(bool)
      mask[all_mask>0] = True
      # use np.where to get the r,c coordinates 
      # of valid pixels
      coords = np.where(all_mask)
      # find the min/max extent of these
      cmin = np.min(coords,axis=1)
      cmax = np.max(coords,axis=1)
      for layer in selected_layers[:-1]:
        lai[layer] = lai[layer][:,cmin[0]:cmax[0]+1,cmin[1]:cmax[1]+1]
    lai['offset'] = cmin
    
    return lai
