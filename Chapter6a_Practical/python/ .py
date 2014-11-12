import numpy as np
import datetime

import os
if 'GDAL_DATA' not in os.environ:
    os.environ["GDAL_DATA"] = '/opt/anaconda/share/gdal'

def interp0(s):
  # transform the first one
  ds = np.array(s.split('-')).astype(int)
  return float(datetime.datetime(ds[0],ds[1],ds[2]).strftime('%Y.%j'))

file = 'data/delnorte.dat'
data = np.loadtxt(file,converters={2:interp0},usecols=(2,3),unpack=True,dtype=float)
year = np.array([int(i) for i in data[0]])
doy  = np.array([int(i*1000) - int(i)*1000 for i in data[0]])
flow = data[1]

# filter it
ww = np.in1d(year,[2005])
doy = doy[ww]
flow = flow[ww]

data = np.loadtxt('data/delNorteT.dat',skiprows=2,unpack=True)
year = data[0]
# filter it
ww = np.in1d(year,[2005])
tmax = data[3][ww]
tmin = data[4][ww]
temp = (0.5*(tmax+tmin) - 32.)* 5./ 9.

from scipy import interpolate
mask = temp < 100

f = interpolate.interp1d(doy[mask],temp[mask],kind='linear')
temp = f(doy)


import numpy as np
snowProp = np.load('data/snowprop.npz')['snowProp']

import pickle

data = {'snowprop':snowProp,'doy':doy,'temp':temp,'flow':flow}


pkl_file = open('data/data.pkl', 'wb')

pickle.dump(data,pkl_file)


