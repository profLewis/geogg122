import numpy as np
import sys,os

here = os.path.realpath(__file__)
sys.path.insert(0,here)


tile = 'h17v03'
year = '2005'

# specify the file with the urls in
ifile= 'files/data/modis_lai_%s_%s.txt'%(tile,year)

get_filename = lambda f: f.split('/')[-1]
filelist = np.loadtxt(ifile,dtype='str',converters={0:get_filename})

from get_lai import *

try:
    data = lai['Lai_1km']
    sd = lai['LaiStdDev_1km']
except:
    lai = read_lai(filelist,country='IRELAND')
    data = lai['Lai_1km']
    sd = lai['LaiStdDev_1km']
    
thresh = 0.1
sd[sd<thresh] = thresh



