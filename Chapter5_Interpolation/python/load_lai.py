import numpy as np
import sys,os
import numpy.ma as ma
import pickle

here, filename = os.path.split(os.path.abspath(__file__))
sys.path.insert(0,here)


tile = 'h17v03'
year = '2005'
country = 'IRELAND'
pklfile = ('%s/../data/lai_%s_%s_%s.pkl'%\
	     (here,country,tile,year)).replace('/',os.sep)
ifile= ('files/data/modis_lai_%s_%s.txt'%(tile,year)).replace('/',os.sep)

try:
  data = lai['Lai_1km']
  sd = lai['LaiStdDev_1km']
  filelist = lai['filelist']
except:
  try:
    print 'read from',pklfile
    # try to load from pkl file
    lai = pickle.load(open(pklfile))
    data = lai['Lai_1km']
    sd = lai['LaiStdDev_1km']
    filelist = lai['filenames']
  except:
    print'read from source files'
    # failed: read from original files

    get_filename = lambda f: f.split('/')[-1]
    filelist = np.loadtxt(ifile,dtype='str',converters={0:get_filename})

    from get_lai import *
    lai = read_lai(filelist,country=country)
    data = lai['Lai_1km']
    sd = lai['LaiStdDev_1km']

    # save it
    with open(pklfile, 'wb') as outfile:
      pickle.dump(lai,outfile,protocol=pickle.HIGHEST_PROTOCOL)

thresh = 0.1
sd[sd<thresh] = thresh


