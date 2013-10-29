import numpy as np
import numpy.ma as ma
import gdal


def get_lai(filename, \
           qc_layer = 'FparLai_QC',\
           scale = [0.1, 0.1],\
           mincol=0,minrow=0,ncol=None,nrow=None,\
           selected_layers = ["Lai_1km", "LaiStdDev_1km"]):

    # force these to be int
    xoff = int(mincol)
    yoff = int(minrow)
    xsize = ncol and int(ncol)
    ysize = nrow and int(nrow)

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
        band = g.GetRasterBand(1) 
        data[layer] = band.ReadAsArray(xoff,yoff,xsize,ysize) * scale[i]

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


def read_lai(filelist,datadir='files/data',\
		country=None,verbose=False):
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
    if country:
        if verbose:
		print "creating mask of %s"%country
        # make a raster mask
        # from the layer UNITED KINGDOM in world.shp
        file_template = 'HDF4_EOS:EOS_GRID:"%s":MOD_Grid_MOD15A2:%s'
        file_spec = file_template%('files/data/%s'%filelist[0],'Lai_1km')
                                   
        mask = raster_mask(file_spec,\
                           target_vector_file = "files/data/world.shp",\
                           attribute_filter = "NAME = '%s'"%country)
        # extract just the area we want
        # by getting the min/max rows/cols
        # of the data mask
        # The mask is False for the area we want
        rowpix,colpix = np.where(mask == False)
        mincol,maxcol = min(colpix),max(colpix)
        minrow,maxrow = min(rowpix),max(rowpix)
        ncol = maxcol - mincol + 1
        nrow = maxrow - minrow + 1
        # and make a small mask
        small_mask = mask[minrow:minrow+nrow,mincol:mincol+ncol]
    else:
        # no country
        mincol = 0
        maxcol = 0
        ncol = None
        nrow = None

    # data_fields with empty lists
    data_fields = {'LaiStdDev_1km':[],'Lai_1km':[]}
    
    # make a dictionary and put the filenames in it
    # along with the mask and min/max info
    lai = {'filenames':np.sort(filelist),\
           'minrow':minrow,'mincol':mincol,\
           'mask':small_mask}
    
    # combine the dictionaries
    lai.update(data_fields)
    
    # loop over each filename
    for f in np.sort(lai['filenames']):
        if verbose:
		print '...',f
        this_lai = get_lai('files/data/%s'%f,\
                           mincol=mincol,ncol=ncol,\
                           minrow=minrow,nrow=nrow)
        for layer in data_fields.keys():
            # apply the mask
            if country:
                new_mask = this_lai[layer].mask | small_mask
                this_lai[layer] = ma.array(this_lai[layer],mask=new_mask)
            lai[layer].append(this_lai[layer])    
    if verbose:
      print '... done' 
    for layer in data_fields.keys():
      lai[layer] = ma.array(lai[layer])
       
    return lai


import pylab as plt
import os

def make_movie(lai,root,layer='Lai_1km',vmax=4.,vmin=0.,do_plot=False):
    '''
    Make an animated gif from MODIS LAI data in
    dictionary 'lai'.
    
    Parameters:
    lai    : data dictionary
    root   : root file /directory name of frames and movie
    
    layer  : data layer to plot 
    vmax   : max value for plotting
    vmin   : min value for plotting
    do_plot: set True if you want the individual plots
             to display
    
    Returns:
    movie name    
    
    '''
    cmap = plt.cm.Greens
    
    for i,f in enumerate(lai['filenames']):
        fig = plt.figure(figsize=(7,7))
        # get some info from filename
        file_id = f.split('/')[-1].split('.')[-5][1:]
        print file_id
        plt.imshow(lai[layer][i],cmap=cmap,interpolation='none',\
                   vmax=vmax,vmin=vmin)
        # plot a jpg
        plt.title(file_id)
        plt.colorbar()
        plt.savefig('%s_%s.jpg'%(root,file_id))
        if not do_plot:
            plt.close(fig)
        
    cmd = 'convert -delay 100 -loop 0 {0}_*.jpg {0}_movie.gif'.format(root)
    os.system(cmd)
    return '{0}_movie.gif'.format(root)

from regularise import regularise

def smooth_pixel(r,c,data,sd,order=2,wsd=0.003,thresh=0.25):
    pixel = data[:,r,c]
    pixel_sd =   sd[:,r,c]
    
    # original x,y
    y_  = pixel
    x_  = (np.arange(len(y_))*8.+1)[~pixel.mask]
    sd_ = pixel_sd[~pixel.mask]
    # threshold sd 
    sd_[sd_<thresh] = thresh
    y_  = y_[~pixel.mask]
    # weights from std
    w_ = 1./(sd_**2)
        # make an array with the samples in
    # at the correct x locations
    x_full = np.arange(1.,366.)
    y_full = np.zeros_like(x_full)
    w_full = np.zeros_like(x_full)
    
    mask = np.in1d(x_full,x_)
    y_full[mask] = y_
    w_full[mask] = w_
    
    # extend: using np.tile() to repeat data
    y_extend = np.tile(y_full,3)
    w_extend = np.tile(w_full,3)
    # extend: using vstack to stack 3 different arrays
    x_extend = np.hstack((x_full-46*8,x_full,x_full+46*8))
    
    # which samples we want
    want_samples = ((x_extend >= 1) & (x_extend <=365))
    # call the smoother    
    z,sd_z = regularise(x_extend,y_extend,w=w_extend,wsd=wsd,order=order)
    return z[want_samples],(sd_z[want_samples],x_full,x_,y_,sd_)

