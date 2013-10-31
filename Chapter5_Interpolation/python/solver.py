#!/usr/bin/python
import numpy,scipy 
import scipy.optimize



def dbl_logistic_model ( p_in, t ):
        import numpy
        """A double logistic model, as in Sobrino and Juliean, or Zhang et al"""
        p = p_in.copy()
        # scale p[3] and p[5]
        p[3] *= 365
        p[5] *= 365.
        return p[0] - p[1]* ( 1./(1+numpy.exp(p[2]*(t-p[3]))) + \
                              1./(1+numpy.exp(-p[4]*(t-p[5])))  - 1 )

def mismatch_function(p, x, y, unc):
    import numpy
    y_hat = dbl_logistic_model(p, x)
    diff = (y_hat - y)/unc
    return diff

def sse(p,x,y,unc):
    '''Sum of squared error'''
    # penalise p[3] > p[5]
    import numpy
    err = numpy.max([0.,(p[3] - p[5])])*1e4
    return (mismatch_function(p,x,y,unc)**2).sum()+err

def solve(sse,p,x,y,unc):
    import numpy 
    import scipy.optimize
    bound = numpy.array([(0.,10.),(0.,10.),\
                  (0.01,1.),(50./365,150./365.),(0.01,1.),(100./365,300./365)])
    return scipy.optimize.fmin_l_bfgs_b(sse,p,approx_grad=True,iprint=-1,\
                                args=(x,y,unc),bounds=bound,factr=1e6)

tile = 'h17v03'
year = '2005'

# specify the file with the urls in
ifile= 'files/data/modis_lai_%s_%s.txt'%(tile,year)

fp = open(ifile)
filelist = [url.split('/')[-1].strip() for url in fp.readlines()]
fp.close()
import sys
sys.path.insert(0,'files/python')

from get_lai import *

try:
    data = lai['Lai_1km']
    sd = lai['LaiStdDev_1km']
except:
    lai = read_lai(filelist,country='IRELAND')
    data = lai['Lai_1km']
    sd = lai['LaiStdDev_1km']
    
thresh = 0.25
sd[sd<thresh] = thresh

import pp
import sys
sys.path.insert(0,'.')

# and run over each pixel ... this will take some time

# pixels that have some data
mask = (~data.mask).sum(axis=0)

pdata = np.zeros((7,) + mask.shape)

rows,cols = np.where(mask>0)
len_x = len(rows)

# lets just do the first few to start with
rows = rows[:1000]
cols = cols[:1000]

len_x = len(rows)

job_server = pp.Server()
jobs = []


for i in xrange(len_x):
    r,c = rows[i],cols[i]
    # progress bar
    #if i%(len_x/20) == 0:
    #    print '... %4.2f percent'%(i*100./float(len_x))
    
    y = data[:,r,c]
    mask = ~y.mask
    y = np.array(y[mask])
    x = (np.arange(46)*8+1.)[mask]
    unc = np.array(sd[:,r,c][mask])
    
    # need to get an initial estimate of the parameters
    
    # some stats on y
    ysd = np.std(y)
    ymean = np.mean(y)
    p = np.zeros(6)
    p[0] = ymean - 1.151*ysd;   # minimum  (1.151 is 75% CI)
    p[1] = 2*1.151*ysd          # range
    p[2] = 0.19                 # related to up slope
    p[3] = 140/365.                  # midpoint of up slope
    p[4] = 0.13                 # related to down slope
    p[5] = 220/365.                  # midpoint of down slope

    
    # set factr to quite large number (relative error in solution)
    # as it'll take too long otherwise
    
    #psolve = optimize.fmin_l_bfgs_b(sse,p,approx_grad=True,iprint=-1,\
    #                            args=(x,y,unc),bounds=bound,factr=1e6)
    jobs.append(job_server.submit(solve,(sse,p,x,y,unc),\
                    (numpy,scipy,scipy.optimize,solver),\
                    ('dbl_logistic_model','sse','mismatch_function','solve')))

for i,s in enumerate(jobs):
    psolve = s()
    pdata[:-1,rows[i],cols[i]] = psolve[0]
    pdata[-1,rows[i],cols[i]] = psolve[1] # sse


