import numpy as np
import pylab as plt
import numpy.ma as ma
import sys,os
import gdal
from glob import glob
# file list

files = np.sort(glob('data/MOD14CMH.*.005.01.hdf'))

year = np.array([f.split(os.sep)[-1].split('.')[1][:4] for f in files]).astype(int)
month= np.array([f.split(os.sep)[-1].split('.')[1][4:] for f in files]).astype(int)

def reader(hdf):
  pattern = 'HDF4_SDS:UNKNOWN:"%s":1'%hdf
  g = gdal.Open(pattern)
  d = g.ReadAsArray()
  # invalid is -1
  mask = (d == -1)
  d[mask] = 0.0
  # fix any -ve numbers
  mask[d<0] = True
  d[d<0] = 0
  return d,mask

mask = reader(files[0])[1]
data = [reader(f)[0] for f in files]
masks = np.array([mask]*len(data))

data = ma.array(data,mask=masks)

