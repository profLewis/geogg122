#!/usr/bin/env python
import sys
from ftplib import FTP
from types import *

assert type(year) is  IntType, 'must set variable "year" as inti: %s'%str(year)
print 'year',year

HOST='n5eil01u.ecs.nsidc.org'
USER='anonymous'
PASSWD='yourid@ucl.ac.uk'
FILE='data/robot_snow.%d.txt'%year

ftp = FTP(HOST)
ftp.login(user=USER,passwd=PASSWD) 


fp = open(FILE,'w')

for m in xrange(1,13):
  print 'month',m
  for d in xrange(1,32):
    try:
      a = ftp.nlst('DP0/MOSA/MYD10A1.005/%4d.%02d.%02d'%(year,m,d))
      a = ['ftp://%s/%s\n'%(HOST,x) for x in a if (x[-4:] == '.hdf') ]
      fp.writelines(a)
    except:
      pass

    try:
      a = ftp.nlst('DP0/MOST/MYD10A1.005/%4d.%02d.%02d'%(year,m,d))
      a = ['ftp://%s/%s\n'%(HOST,x) for x in a if (x[-4:] == '.hdf') ]
      fp.writelines(a)
    except:
      pass

fp.close()
#print data

