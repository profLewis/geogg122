#!/usr/bin/env python
"""Some functions to plot data, fit models etc."""

import pdb
import os
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
from osgeo import gdal

from pheno_utils import *

def quadratic_model ( p, agdd ):
    """A quadratic phenology model. Takes in a lenght 3 vector with parameters
    for a quadratic function of AGDD ``agdd``"""
    return p[0]*agdd**2 + p[1]*agdd + p[2]
    
def fourier_model ( p, agdd, n_harm):
    """A simple Fourier model Takes in the Fourier coefficients and phase and 
    uses AGDD ``agdd`` as its time axis. By default ``n_harm`` harmonics are 
    used."""
    
    integration_time = len ( agdd )
    t = np.arange ( 1, integration_time + 1)
    result = t*.0 + p[0]
    w=1
    for i in xrange ( 1, n_harm*4, 4 ):
        result =result + p[i]*np.cos ( 2.0*np.pi*w*t/integration_time + p[i+1] ) \
            + p[i+2]*np.sin ( 2.0*np.pi*w*t/integration_time + p[i+3] )    
        w = w+1
    return result
    
def dbl_logistic_model ( p, agdd ):
    """A double logistic model, as in Sobrino and Juliean, or Zhang et al"""
    return p[0] + p[1]* ( 1./(1+np.exp(p[2]*(agdd-p[3]))) + \
                          1./(1+np.exp(-p[4]*(agdd-p[5])))  - 1 )

                          
def mismatch_function ( p, pheno_func, ndvi, agdd, years, n_harm=3 ):
    """The NDVI/Phenology model mismatch function. This can be a multi-year
    function that will be minimised wrt to the VI observations. This function
    will take different phenology models, and NDVI and AGDD datasets. Note that
    if you want to use some other temporal reference, this can be quite easily
    be passed through instead of AGDD. ``n_harm`` is only used when pheno_model
    is set to fourier, and controls the number of harmonics that will be used"""

    # output stores the predictions    
    output = []
    ndvi_daily = interpolate_daily ( ndvi )
    for year in years:
        if year%4 == 0:
            ndvid = ndvi_daily[ (year-2001)*365:( year - 2001 + 1)*366 ]
            agdd_i =  agdd [ (year-2001)*365:( year - 2001 + 1)*366 ]
        else:
            ndvid = ndvi_daily[ (year-2001)*365:( year - 2001 + 1)*365 ]
            agdd_i =  agdd [ (year-2001)*365:( year - 2001 + 1)*365 ]
        
        if pheno_func.__name__ != "fourier_model":
            fitness = lambda p, ndvi_in, agdd: ndvi_in - pheno_func ( p, agdd )
            oot = fitness ( p, ndvid, agdd_i )            
            [ output.append ( x ) for x in oot ]
        else:
            fitness = lambda p, ndvi_in, agdd, n_harm: \
                    ndvi_in - pheno_func ( p, agdd, n_harm=n_harm )
            oot = fitness ( p, ndvid, agdd_i, n_harm )            
            [ output.append ( x ) for x in oot ]
    return np.array(output).squeeze()
        
        
def fit_phenology_model ( longitude, latitude, year,temp, pheno_model,  \
            xinit=None, tbase=10, tmax=40, n_harm=3, do_agdd=False ):
    """This function fits a phenology model of choice for a given location and
    time period. The user can also modify the base and maximum temperature for
    AGDD calculations, as well as the number of harmonics used by the Fourier
    phenology model."""
    from scipy.optimize import leastsq
    # Find the number of parameters and a pointer to the phenology model func.
    if pheno_model == "quadratic":
        pheno_func = quadratic_model
        n_params = 3 # 3 terms
    elif pheno_model == "fourier":
        pheno_func = fourier_model
        n_params = 1 + n_harm*4 # 1 DC term + 2 phase + 2 magnitude per harmonic
    elif pheno_model == "dbl_logistic":
        n_params = 6 # 6 terms
        pheno_func = dbl_logistic_model

    # This test is to see whether we get a list of years, or a single year
    if isinstance ( year, list ):
        years = year
    elif isinstance ( year, int ) or isinstance ( year, float ):
        years = [ year]
    else:
        raise TypeError, "year has to be a scalar or  list"
    ndvi_all = get_ndvi (  longitude, latitude )/10000.

    agdd_all = calculate_gdd ( temp, tbase=tbase, tmax=tmax )
    t_axis = []
    for y in xrange ( 2001, 2012 ):
        if y % 4 == 0:
            if do_agdd:
                t_axis = np.r_[t_axis, agdd_all[ (y-2001)*365:(y-2001+1)*367] ]
            else:
                t_axis = np.r_[t_axis, np.arange ( 1, 367) ]
        else:
            if do_agdd:
                t_axis = np.r_[t_axis, agdd_all[ (y-2001)*365:(y-2001+1)*366] ]
            else:
                t_axis = np.r_[t_axis, np.arange ( 1, 366) ]
                    
    if xinit is None:
        # The user hasn't provided a starting guess
        xinit = [.5,] * n_params
        # Dbl_logistic might require sensible starting point
        if pheno_model == "dbl_logistic":
            xinit[0] = ndvi_all.min()
            xinit[1] = ndvi_all.max() - ndvi_all.min()
            xinit[2] = 0.19
            xinit[3] = 120
            xinit[4] = 0.13
            xinit[5] = 200
    ( xsol, msg ) = leastsq ( mismatch_function, xinit, \
        args=( pheno_func, ndvi_all, t_axis, years, n_harm ), maxfev=1000000 )
    fwd_model = []
    if pheno_model != "fourier":
        for y in xrange( 2001, 2012):
            if y % 4 == 0:
                if do_agdd:
                    ax = pheno_func ( xsol, agdd_all[ \
                            (y-2001)*365:(y-2001+1)*367] )
                else:
                    ax = pheno_func ( xsol, np.arange(1, 367) )
                [fwd_model.append ( x ) for x in ax]
            else:
                if do_agdd:
                    ax = pheno_func ( xsol, agdd_all[ \
                    (y-2001)*365:(y-2001+1)*366] )
                else:
                    ax = pheno_func ( xsol, np.arange(1, 366) )
                [fwd_model.append ( x ) for x in ax]
                    
    else:
        for y in xrange( 2001, 2012):
            if y % 4 == 0:
                if do_agdd:
                    ax = pheno_func ( xsol, agdd_all[ \
                            (y-2001)*365:(y-2001+1)*367], n_harm )
                else:
                    ax = pheno_func ( xsol, np.arange(1, 367), n_harm )
                [fwd_model.append ( x ) for x in ax]
            else:
                if do_agdd:
                    ax = pheno_func ( xsol, agdd_all[ \
                    (y-2001)*365:(y-2001+1)*366], n_harm )
                else:
                    ax = pheno_func ( xsol, np.arange(1, 366), n_harm )
                [fwd_model.append ( x ) for x in ax]
                    
    return ( agdd_all, interpolate_daily( ndvi_all ), xsol, msg, \
            np.array (fwd_model) )
    
def get_temperature ( year=None, latitude=None, longitude=None, \
        fname="/data/geospatial_20/ucfajlg/meteo/temp_2m.tif" ):
    """This function grabs the temperature for a given year (or all of them if
    set ``year`` is set to ``None``, for the whole globe or for a given location.
    """
    # These are factors for the ERA data
    a = 0.0020151192442093
    b = 258.72093867714
    # Check that year range is OK
    assert ( (year >= 2001 and year <= 2011) or (year is None) )
    if year is not None:
        if year == 2004 or year == 2008:
            n_doys = 366
        else:
            n_doys = 365
        year = year - 2001
    if (latitude is None):
        # Grab a whole year of data
        # Longitude has to be None too...
        assert ( longitude is None ) 
        g = gdal.Open ( fname )
        if year is not None:
            temp = g.ReadAsArray()[((year)*n_doys):((year+1)*n_doys), :, :]
        else:
            temp = g.ReadAsArray()
        # Scale to degree C
        temp = np.where ( temp!=-32767, temp*a + b - 273.15, -32767)
    else:
        assert ( longitude >= -180 and longitude <= 180 )
        assert ( latitude >= -90 and latitude <= 90 )
        (ix, iy) = pixel_loc ( longitude, latitude )
        ix = int ( np.floor ( ix ) )
        iy = int ( np.floor ( iy ) )
        g = gdal.Open ( fname )

        if year is not None:
            n_bands = np.arange ( ((year)*n_doys), ((year+1)*n_doys) ) + 1
        else:
            n_bands = np.arange ( g.RasterCount ) + 1

        buf = g.ReadRaster( ix, iy, 1, 1,  buf_xsize=1, buf_ysize=1, \
                band_list=n_bands )
        temp = np.frombuffer(buf, dtype=np.int16) 
        # Scale to degree C
        temp = np.where ( temp!=-32767, temp*a + b- 273.15, -32767)
        
    return temp

def calculate_gdd ( temp, tbase=10, tmax=40 ):
    """This function calculates the Growing Degree Days for a given year from
    the ERA Interim daily mean surface temperature data. The user can select a 
    base temperature in degrees Celsius. By default, the value is 10. If no
    year is specified, the whole time series is retrieved. Note that if you 
    don't specify time and location, the operation can be quite slow and will
    return lots of data."""
    
    if temp.ndim == 3:
        b = np.clip ( temp, tbase, tmax )
        c = np.where ( b-tbase<0, 0, b-tbase )
        agdd = c.cumsum (axis=0)
    else:
        if temp.shape[0] <= 367:
            # Only one year of data
            b = np.clip ( temp, tbase, tmax )
            c = np.where ( b-tbase < 0, 0, b-tbase )
            agdd = c.cumsum ( axis=0 )
        else:
            b = np.clip ( temp, tbase, tmax )
            c = np.where ( b-tbase < 0, 0, b-tbase )
            agdd = np.zeros( 4017 )
            for y in xrange ( 11 ):
                a = c[y*365:(y+1)*365]
                o = a.cumsum ( axis=0)
                agdd[y*365:(y+1)*365] = o
    return agdd

def get_ndvi ( longitude, latitude, \
        plot=False,  data_dir="/data/geospatial_20/ucfajlg/MODIS/output" ):
    """This function returns the  NDVI for a given longitude and latitude, 
    for 2001 to 2011. Optionally, It will also plot the data"""
    # Check sanity of longitude an latitude values...
    assert ( longitude >= -180 and longitude <= 180 )
    assert ( latitude >= -90 and latitude <= 90 )
    (ix, iy) = pixel_loc ( longitude, latitude )
    data = []
    t_range = []
    for year in xrange ( 2001, 2012 ):
        gdal_dataset = gdal.Open ( "%s/NDVI_%04d.tif" % ( data_dir, year ) )
        data = np.r_[ data, gdal_dataset.ReadAsArray ()[ :, iy, ix] ] 
        t_range +=  [ matplotlib.dates.datestr2num("%04d-%d-01" % (year, m )) \
            for m in range(1, 13) ]
    if plot:
        plt.plot_date ( t_range, data, '-sr', label="NDVI" )
        plt.grid ( True )
        plt.xlabel("Date")
        plt.ylabel("NDVI [-]")
        plt.show()
    return ( data )
    
def agdd_plots ( nplots, iplot, tbase, tmax, t_range, temp, agdd ):
    """This function does the AGDD plots in a nplots vertical stack of plots.
    iplot is the current plot (from top to bottom, starting at 1), tbase and
    tmax are the values used for AGDD calculations. t_range is a temporal range
    (usually DoY) and temp and AGDD are extracted 2m temperature and AGDD"""
    plt.subplot ( nplots, 1, iplot)
    # Put a grey area for the AGDD calculation bounds
    plt.axhspan ( tbase, tmax, xmin=0, xmax=366, color='0.9' )
    # Plot temperature
    plt.plot ( t_range, temp, '-r', label="Tm" )
    plt.ylabel("Mean Temp [degC]")
    plt.grid ( True )
    plt.twinx()
    plt.plot ( t_range, agdd, '-g', label="AGDD" )
    plt.ylabel ( "AGDD [degC]")
    