import numpy as np
import numpy.ma as ma
import gdal


def masked(months=range(1, 13), years=[2009], folder="data/", layer="BHR_VIS"):
    """Read globalbedo data when given month and year.
    Parameters
    ------------
    months: iter
         An iterator with the month numbers to read
    years: iter
        An iterator with the years to read
    folder: str
        The folder where the GA data are stored.
    layer: str
        The data layer

    Returns
    ---------
    A 2D array"""
    data = []
    file_template = 'NETCDF:"{:s}":{:s}'  # Template for the Netcdf path
    # the actual filename
    fname_template = '{:s}/GlobAlbedo.merge.albedo.05.{:d}{:02d}.nc'
    for year in years:
        for month in months:
            fname = fname_template.format(folder, year, month)
            netcdf_fname = file_template.format(fname, layer)
            g = gdal.Open(netcdf_fname)
            if g is None:
                raise IOError("Problem with reading file {}".format(fname))
            the_data = g.ReadAsArray()
            masked_data = np.ma.array(the_data,mask=np.isnan(the_data))
            data.append(masked_data)
    output_data = np.ma.array(data)
    return output_data

