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


