import numpy as np
import numpy.ma as ma
from osgeo import ogr,osr
import gdal
try:
    from PIL import Image,ImageDraw
except:
    import Image,ImageDraw
    
import os
if 'GDAL_DATA' not in os.environ:
    os.environ["GDAL_DATA"] = '/opt/anaconda/share/gdal'


def raster_mask(reference_filename, \
                target_vector_file = "data/world.shp",\
                attribute_filter = "NAME = 'IRELAND'"):

    burn_value = 1

    # First, open the file that we'll be taking as a reference
    # We will need to gleam the size in pixels, as well as projection
    # and geotransform.
    
    g = gdal.Open( reference_filename )
    
    # We now create an in-memory raster, with the appropriate dimensions
    drv = gdal.GetDriverByName('MEM')
    target_ds = drv.Create('', g.RasterXSize, g.RasterXSize, 1,  gdal.GDT_Byte)
    target_ds.SetGeoTransform( g.GetGeoTransform() )
    
    # We set up a transform object as we saw in the previous notebook.
    # This goes from WGS84 to the projection in the reference datasets
    
    wgs84 = osr.SpatialReference( ) # Define a SpatialReference object
    wgs84.ImportFromEPSG( 4326 ) # And set it to WGS84 using the EPSG code
    
    # Now for the target projection, Ordnance Survey's British National Grid
    to_proj = osr.SpatialReference() # define the SpatialReference object
    # In this case, we get the projection from a Proj4 string
    
    # or, if using the proj4 representation
    to_proj.ImportFromWkt( g.GetProjectionRef() )
    target_ds.SetProjection ( to_proj.ExportToWkt() )
    # Now, we define a coordinate transformtion object, *from* wgs84 *to* OSNG
    tx = osr.CoordinateTransformation( wgs84, to_proj )
    
    # We define an output in-memory OGR dataset
    # You could also do select a driver for an eg "ESRI Shapefile" here
    # and give it a sexier name than out!
    
    drv = ogr.GetDriverByName( 'Memory' )  
    dst_ds = drv.CreateDataSource( 'out' )
    # This is a single layer dataset. The layer needs to be of polygons
    # and needs to have the target files' projection
    dst_layer = dst_ds.CreateLayer('', srs = to_proj, geom_type=ogr.wkbPolygon )  
    
    # Open the original shapefile, get the first layer, and filter by attribute
    vector_ds = ogr.Open( target_vector_file )
    lyr = vector_ds.GetLayer ( 0 )
    lyr.SetAttributeFilter( attribute_filter )
    
    
    # Get a field definition from the original vector file. 
    # We don't need much more detail here
    feature = lyr.GetFeature(0)
    field = feature.GetFieldDefnRef( 0 )
    # Apply the field definition from the original to the output
    dst_layer.CreateField( field )
    feature_defn = dst_layer.GetLayerDefn()
    # Reset the original layer so we can read all features
    lyr.ResetReading()
    for feat in lyr:
        # For each feature, get the geometry
        geom = feat.GetGeometryRef()
        # transform it to the reference projection
        geom.Transform ( tx )
        # Create an output feature
        out_geom = ogr.Feature ( feature_defn )
        # Set the geometry to be the reprojected/transformed geometry
        out_geom.SetGeometry ( geom )
        # Add the feature with its geometry to the output yaer
        dst_layer.CreateFeature(out_geom )
        # Clear things up
        out_geom.Destroy
        geom.Destroy
    # Done adding geometries
    # Reset the output layer to the 0th geometry
    dst_layer.ResetReading()
    
    # Now, we rastertize the output vector in-memory file
    # into the in-memory output raster file
    
    err = gdal.RasterizeLayer(target_ds, [1], dst_layer,
                burn_values=[burn_value])
    if err != 0:
        print("error:", err)
    
    # Read the data from the raster, this is your mask
    data = target_ds.ReadAsArray()
    
    # return False for the desired area
    # and True elsewhere
 
    return ~data.astype(bool)


def world2Pixel(geoMatrix, x, y):
  """
  Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
  the pixel location of a geospatial coordinate
  """
  ulX = geoMatrix[0]
  ulY = geoMatrix[3]
  xDist = geoMatrix[1]
  yDist = geoMatrix[5]
  rtnX = geoMatrix[2]
  rtnY = geoMatrix[4]
  pixel = np.round((x - ulX) / xDist).astype(np.int)
  line = np.round((ulY - y) / xDist).astype(np.int)
  return (pixel, line)

def raster_mask2(reference_filename, \
                target_vector_file = "data/world.shp",\
                attribute_filter = 0):

    #burn_value = 1

    # First, open the file that we'll be taking as a reference
    # We will need to gleam the size in pixels, as well as projection
    # and geotransform.

    vector_ds = ogr.Open( target_vector_file )

    source_ds = ogr.GetDriverByName("Memory").CopyDataSource(vector_ds, "")
    source_layer = source_ds.GetLayer(0)
    source_srs = source_layer.GetSpatialRef()
    wkt = source_srs.ExportToWkt()

    lyr = vector_ds.GetLayer ( 0 )
    #lyr.SetAttributeFilter( attribute_filter )
    # Get a field definition from the original vector file. 
    # We don't need much more detail here
    poly = lyr.GetFeature(attribute_filter)

    geom = poly.GetGeometryRef()
    pts = geom.GetGeometryRef(0)

    # extract and plot the transformed data
    pnts = np.array([(pts.GetX(p), pts.GetY(p)) for p in xrange(pts.GetPointCount())]).transpose()

    # MODIS
    g = gdal.Open( reference_filename )
    raster = gdal.Open( reference_filename )
    # get the wicket
    modisWKT = raster.GetProjectionRef()

    oSRS = osr.SpatialReference ()
    oSRSop = osr.SpatialReference ()

    oSRSop.ImportFromWkt(modisWKT)
    # wkt from above, is the wicket from the shapefile
    oSRS.ImportFromWkt(wkt)
    # now make sure we have the shapefile geom

    geom = poly.GetGeometryRef()
    pts = geom.GetGeometryRef(0)

    # pts is the polygon of interest
    pts.AssignSpatialReference(oSRS)
    # so transform it to the MODIS geometry
    pts.TransformTo(oSRSop)

    pnts = np.array([(pts.GetX(p), pts.GetY(p)) for p in xrange(pts.GetPointCount())]).transpose()

    geo_t = raster.GetGeoTransform()

    pixel, line = world2Pixel(geo_t,pnts[0],pnts[1])

    rasterPoly = Image.new("L", (raster.RasterXSize, raster.RasterYSize),1)
    rasterize = ImageDraw.Draw(rasterPoly)
    # must be a tuple now ... doh
    listdata = list(tuple(pixel) for pixel in np.array((pixel,line)).T.tolist())
    rasterize.polygon(listdata,outline=0,fill=0)
    mask = np.array(rasterPoly).astype(bool)
    return mask


def imageToArray(i):
    """
    Converts a Python Imaging Library array to a
    numpy array.
    """
    a=np.fromstring(i.tobytes(),'b')
    a.shape=i.im.size[1], i.im.size[0]
    return a



