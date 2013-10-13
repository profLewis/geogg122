from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma
import sys,os
sys.path.insert(0,['.','files/python'])

from gzurl import gzurl

# NB dataset is a list here

def masked(dataset=['BHR_SW'],year=2009):
  # codes for url specification on globalbedo.org
  years = range(1998,2012)
  codes = [95,95,97,97,26,66,54,54,29,25,53,56,56,78]
  XX = dict(zip(years,codes))

  root = 'http://www.globalbedo.org/GlobAlbedo%d/mosaics/%d/0.5/monthly/'%\
        (XX[year],year)


  # which months?
  months = xrange(1,13)

  # empty list
  data = []

  # loop over month
  # use enumerate so we have an index counter
  for i,month in enumerate(months):

    base = 'GlobAlbedo.%d%02d.mosaic.5.nc'%(year,month)
    url = root + base + '.gz'
    # specify a local filename
    # work out how / why this works ...
    local = os.path.join('files{0}data{0}'.format(os.sep),base)
    
    try:
      # load the netCDF data from the file local_file
      nc = Dataset(local,'r')
    except:
      f = gzurl(url,filename=local)
      nc = Dataset(local,'r')
      f.close()

    this_dataset = []
    for d in dataset:
      # load into the variable 'band'
      band = np.array(nc.variables[d])
      # convert to a masked array
      masked_band = ma.array(band,mask=np.isnan(band))
      # append what we read to the list 
      this_dataset.append(masked_band)

    data.append(this_dataset)
  
  
  # reorganise
  nd = len(dataset)
  all_data = []
  for n in xrange(nd):
    this_data = []
    for d in xrange(len(months)):
      this_data.append(data[d][n])
    this_data = ma.array(this_data)
    all_data.append(this_data.copy())

  return dict(zip(dataset,all_data))

