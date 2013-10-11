from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma

def masked(dataset='BHR_SW'):
  root = 'files/data/'
  year = 2009

  # which months?
  months = xrange(1,13)

  # empty list
  data = []

  # loop over month
  # use enumerate so we have an index counter
  for i,month in enumerate(months):
    # this then is the file we want
    local_file = root + 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
    
    # load the netCDF data from the file local_file
    nc = Dataset(local_file,'r')
    # load into the variable 'band'
    band = np.array(nc.variables[dataset])
    # convert to a masked array
    masked_band = ma.array(band,mask=np.isnan(band))
    # append what we read to the list called data
    data.append(masked_band)
    
  # convert data to a numpy array (its a list of arrays at the moment)
  data = ma.array(data)
  return data

