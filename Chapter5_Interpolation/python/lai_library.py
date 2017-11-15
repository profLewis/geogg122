import numpy as np
import numpy.ma as ma
from osgeo import ogr,osr
import gdal

from regularise import regularise

def rasterise_vector ( raster_fname, vector_fname, where_statement, 
                      output_fname="", output_format="MEM",verbose=False):
    """Rasterises a vector file to produce a mask where some condition 
    in the vector dataset is true. The mask will have the same extent and
    projection as a (provided) 'master' dataset. The selection of the feature
    for the mask will be performed by a command of the form field_name='Value',
    where the single quotes are mandatory (e.g. NAME='Ireland').
    
    Parameters
    -----------
    raster_fname: str
        A GDAL-compatible raster filename that will be used to extract the
        shape, projection, resolution, ... for the rasterisation.
    vector_fname: str
        The vector filename (e.g. Shapefile)
    where_statement: str
        The where statement (e.g. "NAME='Colombia'").
    output_fname: str, optinal
        The output filename, if not provided, an "in-memory array" will be 
        selected. If not provided and the output_format is other than `MEM`
        an error will be raised.
    output_format: str, optional
        An output format. By default, `MEM`
    verbose: Boolean
        Whether to get some extra inforamation
    
    Returns
    --------
    The mask as a Numpy array, 0 where the mask is off, 1 where it is on.    
    
    """
    if output_fname == "" and output_format != "MEM":
        raise ValueError("You need to provide an ouput filename" +
                         " for format{:s}".format(output_format))
    g = gdal.Open(raster_fname)
    if g is None:
        raise IOError("Could not open file {:s}".format(raster_fname))
    raster_proj = g.GetProjectionRef()
    geoT = g.GetGeoTransform()
    if verbose:
        print ">>> Opened file {:s}".format(raster_fname)
        print ">>> Projection: {:s}".format(raster_proj)
    xs = []
    ys = []
    for x,y in [ [0, 0], [0, g.RasterYSize], [g.RasterXSize, g.RasterYSize], [g.RasterXSize, 0]]:
        xx, yy = gdal.ApplyGeoTransform(geoT, x,y)
        xs.append(xx)
        ys.append(yy)
    extent = [min(xs), min(ys), max(xs), max(ys)]
    xRes = geoT[1]
    yRes = geoT[-1]
    nx = g.RasterXSize
    ny = g.RasterYSize
    if verbose:
        print ">>> File size {:d} rows, {:d} columns".format(nx, ny)
        print ">>> UL corner: {:g}, {:g}".format(min(xs), max(ys))
    
    src_ds = gdal.OpenEx(vector_fname)
    if src_ds is None:
        raise IOError("Can't read the vector file {}".format(vector_fname))
    v = gdal.VectorTranslate('', src_ds, format = 'Memory', dstSRS=raster_proj,
                            where=where_statement)
    gg = gdal.Rasterize(output_fname, v,
                    format=output_format, outputType=gdal.GDT_Byte, xRes=xRes, yRes=yRes, 
                    where=where_statement,
                    outputBounds=[min(xs), min(ys), max(xs), max(ys)], 
                    width=nx, height=ny, noData=0, burnValues=1)
    
    if gg is not None:
        print "Done!"
    else:
        raise ValueError("Couldn't generate the mask. Check input parameters")
    return gg.ReadAsArray()



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
        odata[layer] = np.where( qc == 0, data[layer], np.nan)

    return odata
 
def read_lai(filelist,country=None):
    '''
    Read MODIS LAI data from a set of files
    in the list filelist. Data assumed to be in
    directory datadir.
    
    Parameters:
    filelist : list of LAI files
    
    Options:
    country  : country name (in data/world.shp)
    
    Returns:
    lai dictionary
    '''
    if country:
        # make a raster mask
        # from the layer UNITED KINGDOM in world.shp
        filename = filelist[0]
        file_template = 'HDF4_EOS:EOS_GRID:"%s":MOD_Grid_MOD15A2:%s'
        file_spec = file_template%(filename,'Lai_1km')

        mask = rasterise_vector ( file_spec, 
                                 "data/ne_50m_admin_0_countries.shp", "NAME = '{}'".format(country), 
                                 verbose=False)

        # extract just the area we want
        # by getting the min/max rows/cols
        # of the data mask
        # The mask is True for the area we want
        rowpix,colpix = np.where(mask == True)
        mincol,maxcol = min(colpix),max(colpix)
        minrow,maxrow = min(rowpix),max(rowpix)
        ncol = maxcol - mincol + 1
        nrow = maxrow - minrow + 1
        # and make a small mask
        small_mask = mask[minrow:minrow+nrow, mincol:mincol+ncol]

        small_mask = np.where(small_mask == 1, 1., np.nan)
    else:
        # no country
        mincol = 0
        maxcol = 0
        ncol = None
        nrow = None

    # data_fields with empty lists
    data_fields = ['LaiStdDev_1km','Lai_1km']
    
    # make a dictionary and put the filenames in it
    # along with the mask and min/max info
    lai = {'filenames':np.sort(filelist),
           'minrow':minrow,'mincol':mincol,
           'mask':small_mask, 
           'Lai_1km': [],
           'LaiStdDev_1km': []}
    

    
    # loop over each filename
    for f in np.sort(lai['filenames']):
        this_lai = get_lai(f,
                           mincol=mincol,ncol=ncol,
                           minrow=minrow,nrow=nrow)
        for layer in data_fields:
            if country:
                # apply the mask
                lai_p = this_lai[layer]
                this_lai[layer] = lai_p*small_mask
                lai[layer].append(this_lai[layer])
            else:
                lai_p = this_lai[layer]
                lai[layer].append(this_lai[layer])
            
    return lai


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