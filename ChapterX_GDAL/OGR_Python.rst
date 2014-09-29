
Working with vector data: OGR
=============================

.. code:: python

    import json
    import matplotlib
    import os
    import ogr
    import osr
    import gdal
    
    fp = open("../bmh_matplotlibrc.json", 'r' )
    s = json.load ( fp )
    fp.close()
    matplotlib.rcParams.update(s)
    %pylab inline
    %config InlineBackend.figure_format = 'svg'
    figsize( 7,7 )

.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib


Vector data
-----------

Sometimes, geospatial data is acquired and recorded for particular
geometric objects such as polygons or lines. An example is a road
layout, where each road is represented as a geometric object (a line,
with points given in a geographical projection), with a number of added
*features* associated with it, such as the road name, whether it is a
toll road, or whether it is dual-carriageway, etc. This data is quite
different to a raster, where the entire scene is tessellated into
pixels, and each pixel holds a value (or an array of value in the case
of multiband rasterfiles).

If you are familiar with databases, vector files are effectively a
database, where one of the fields is a geometry object (a line in our
previous road example, or a polygon if you consider a cadastral system).
We can thus select different records by writing queries on the features.
Some of these queries might be spatial (e.g. check whether a point is
inside a particular country polygon).

The most common format for vector data is the **ESRI Shapfile**, which
is a multifile format (i.e., several files are needed in order to access
the data). We'll start by getting hold of a shapefile that contains the
countries of the world as polygons, together with information on country
name, capital name, population, etc. The file is available
`here <http://aprsworld.net/gisdata/world/world.zip>`__.

.. figure:: http://aprsworld.net/gisdata/world/political-world-aprs-small.png
   :alt: World

   World

We will download the file with ``wget`` (or ``curl`` if you want to),
and uncompress it using ``unzip`` in the shell:

.. code:: python

    # Downloads the data using wget
    !wget http://aprsworld.net/gisdata/world/world.zip
    # or if you want to use curl...
    #! curl http://aprsworld.net/gisdata/world/world.zip -o world.zip
    !unzip -o -x world.zip
We need to import ``ogr``, and then open the file. As with GDAL, we get
a handler to the file, (``g`` in this case). OGR files can have
different layers, although Shapefiles only have one. We need to select
the layer using ``GetLayer(0)`` (selecting the first layer).

.. code:: python

    from osgeo import ogr
    
    g = ogr.Open( "world.shp" )
    layer = g.GetLayer( 0 )
In order to see a field (the field ``NAME``) we can loop over the
features in the layer, and use the ``GetField('NAME')`` method. We'll
only do ten features here:

.. code:: python

    
    n_feat = 0
    for feat in layer:
        
        print feat.GetField('NAME')
        
        n_feat += 1
        if n_feat == 10:
            break

::


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-2-f4731880d34d> in <module>()
          1 
          2 n_feat = 0
    ----> 3 for feat in layer:
          4 
          5     print feat.GetField('NAME')


    NameError: name 'layer' is not defined


If you wanted to see the different layers, we could do this using:

.. code:: python

    layerDefinition = layer.GetLayerDefn()
    
    
    for i in range(layerDefinition.GetFieldCount()):
        print "Field %d: %s" % ( i+1, layerDefinition.GetFieldDefn(i).GetName() )
Each feature, in addition to the fields shown agove, will have a
``Geometry`` field. We get a handle to this using the
``GetGeometryRef()`` method. Geometries have many methods, such as
``ExportToKML()`` to export to KML (Google Maps/Earth format):

.. code:: python

    the_geometry = feat.GetGeometryRef()
    the_geometry.ExportToKML()
Many of the methods that don't start with ``__`` are interesting. Let's
see what these are. typically, the interesting methods start with an
upper case letter, so we'll only show those:

.. code:: python

    for m in dir ( the_geometry ):
        if m[0].isupper():
            print m
You'll notice that many of these mechanisms e.g. ``Overlaps`` or
``Touches`` are effectively geoprocessing operations (they operate on
geometries and return ``True`` if one geometry overlaps or touches,
respectively, the other). Other operations, such as ``Buffer`` return a
buffered version of the same geometry. This allows you to actually do
fairly complicated geoprocessing operations with OGR. However, if you
want to do geoprocessing in earnest, you should really be using
`Shapely <http://toblerity.org/shapely/manual.html>`__.

A particularly useful webpage for this section is `available in the OGR
cookbook <http://pcjericks.github.io/py-gdalogr-cookbook/>`__. Have a
look through that if you want more in depth information.

Selecting attributes and/or data extents
----------------------------------------

OGR provides an easy way to select attributes on a given layer. This is
done using a SQL-like syntax (you can read more on `OGR's SQL subset
here <http://www.gdal.org/ogr/ogr_sql.html>`__. The main point is that
the *attribute filter* is applied to a complete layer. For example,
let's say that we want to select only countries with a population (field
APPROX) larger than 90 000 000 inhabitants:

.. code:: python

    g = ogr.Open ( "world.shp" )
    lyr = g.GetLayer( 0 )
    lyr.SetAttributeFilter ( "APPROX > 90000000" )
    for feat in lyr:
        print feat.GetFieldAsString ( "NAME") + " has %d inhabitants" % \
            feat.GetFieldAsInteger("APPROX")

.. parsed-literal::

    PAKISTAN has 123490000 inhabitants
    JAPAN has 124710000 inhabitants
    RUSSIAN FEDERATION has 150500000 inhabitants
    INDIA has 873850000 inhabitants
    BANGLADESH has 120850000 inhabitants
    BRAZIL has 159630000 inhabitants
    NIGERIA has 91700000 inhabitants
    CHINA has 1179030000 inhabitants
    INDONESIA has 186180000 inhabitants
    JOHNSTON ATOLL has 256420000 inhabitants
    KINGMAN REEF - PALMYRA ATOLL has 256420000 inhabitants
    UNITED STATES has 256420000 inhabitants


So we get a list of popoulous countries (note that Johnston Atoll and
Palmyra are part of the US, and report the sample popuation as the US!)

An additional way to filter the data is by geographical extent. Let's
say we wanted a list of all the countries in (broadly speaking) Europe,
*i.e.* a geographical extent in longitude from 14W to 37E, and in
latitude from 72N to 38N. We can use ``SetSpatialFilterRect`` to do
this:

.. code:: python

    g = ogr.Open ( "world.shp" )
    lyr = g.GetLayer( 0 )
    lyr.SetSpatialFilterRect ( -14, 37, 38, 72)
    for feat in lyr:
        print feat.GetFieldAsString ( "NAME") + " ---- " + feat.GetFieldAsString ( "CAPITAL") 

.. parsed-literal::

    ALGERIA ---- ALGIERS
    BELGIUM ---- BRUSSELS
    LUXEMBOURG ---- LUXEMBOURG
    SAN MARINO ---- SAN MARINO
    AUSTRIA ---- VIENNA
    CZECH REPUBLIC ---- PRAGUE
    SLOVENIA ---- LJUBLJANA
    HUNGARY ---- BUDAPEST
    SLOVAKIA ---- BRATISLAVA
    YUGOSLAVIA ---- BELGRADE [BEOGRADE]
    BOSNIA AND HERZEGOVINA ---- SARAJEVO
    ALBANIA ---- TIRANE
    MACEDONIA, THE FORMER YUGOSLAV REPUBLIC ---- SKOPJE
    LITHUANIA ---- VILNIUS
    LATVIA ---- RIGA
    BULGARIA ---- SOFIA
    BELARUS ---- MINSK
    MOLDOVA, REPUBLIC OF ---- KISHINEV
    IRELAND ---- DUBLIN
    ICELAND ---- REYKJAVIK
    SPAIN ---- MADRID
    SWEDEN ---- STOCKHOLM
    FINLAND ---- HELSINKI
    TURKEY ---- ANKARA
    RUSSIAN FEDERATION ---- MOSCOW
    GREECE ---- ATHENS
    PORTUGAL ---- LISBON
    POLAND ---- WARSAW
    NORWAY ---- OSLO
    GERMANY ---- BERLIN
    ESTONIA ---- TALLINN
    TUNISIA ---- TUNIS
    CROATIA ---- ZAGREB
    ROMANIA ---- BUCURESTI
    UKRAINE ---- KIEV
    NETHERLANDS ---- AMSTERDAM
    JERSEY ---- SAINT HELIER
    GUERNSEY ---- SAINT PETER PORT
    FAROE ISLANDS ---- TORSHAVN
    DENMARK ---- COPENHAGEN
    MONACO ---- MONACO
    ANDORRA ---- ANDORRA LA VELLA
    LIECHTENSTEIN ---- VADUZ
    SWITZERLAND ---- BERN
    ISLE OF MAN ---- DOUGLAS
    UNITED KINGDOM ---- LONDON
    FRANCE ---- PARIS
    VATICAN CITY (HOLY SEE) ---- VATICAN CITY
    ITALY ---- ROME


Saving a vector file
--------------------

Saving a vector file using OGR requires a number of steps:

1. Definition of the format
2. Definition of the layer projection and geometry type (e.g. lines,
   polygons...)
3. Definition of the data type of the different fields
4. Creation of a feature, population of the different fields, and
   setting a geometry
5. Addition of the feature to the layer
6. Destruction of the feature

This appears quite involved, but let's see how this works. Note that
when you generate a new vector file, OGR will fail if the file already
exists. You might want to use ``os.remove()`` to get rid of the file if
it exists.

Let's see how this is done with an example which is a snippet that
creates a GeoJSON file with the location of the different national
parks. GeoJSON is a nice geographic format, and `github allows you to
display it easily as a
map <https://github.com/blog/1528-there-s-a-map-for-that>`__.

.. code:: python

    # National park information, separated by TABs
    
    parks = """Dartmoor national park\t-3.904\t50.58
    New forest national park\t-1.595\t50.86
    Exmoor national park\t-3.651\t51.14
    Pembrokeshire coast national park\t-4.694\t51.64
    Brecon beacons national park\t-3.432\t51.88
    Pembrokeshire coast national park\t-4.79\t51.99
    Norfolk and suffolk broads\t1.569\t52.62
    Snowdonia national park\t-3.898\t52.9
    Peak district national park\t-1.802\t53.3
    Yorkshire dales national park\t-2.157\t54.23
    North yorkshire moors national park\t-0.8855\t54.37
    Lake district national park\t-3.084\t54.47
    Galloway forest park\t-4.171\t54.87
    Northumberland national park\t-2.228\t55.28
    Loch lomond and the trossachs national park\t-4.593\t56.24
    Tay forest park\t-4.025\t56.59
    Cairngorms national park\t-3.545\t57.08"""
    
    # See if the file exists from a previous run of this snippet
    if os.path.exists ( "parks.json"):
        # It does exist, so remove it
        os.remove ( "parks.json" )
    
    # We need the output projection to bet set to Lat/Long
    latlong = osr.SpatialReference()
    latlong.ImportFromEPSG( 4326 )
    
    # Invoke the GeoJSON driver
    drv = ogr.GetDriverByName( 'GeoJSON' )  
    # This is the output filename
    dst_ds = drv.CreateDataSource( 'parks.json' )
    # This is a single layer dataset. The layer needs to be of points
    # and needs to have the WGS84 projection, which we defined above
    dst_layer = dst_ds.CreateLayer('', srs =latlong , \
                                   geom_type=ogr.wkbPoint )  
    
    # We just need a field with the Park's name, and its type is a String
    field_defn=ogr.FieldDefn( 'name', ogr.OFTString )
    dst_layer.CreateField( field_defn )
    
    
    # Algorithm is as follows:
    # 1. Loop over lines
    # 2. Split line into park name, longitude, latitude
    # 3. Create WKT of the point
    # 4. Set the attribute name to name of park
    # 5. Clean up
    
    for park_id, line in enumerate( parks.split( "\n" ) ):
        # Get the relevant information
        park_name, lon, lat = line.split("\t")
        # Create a geogrpahical representation of the current park
        wkt = "POINT ( %f %f )" % ( float(lon), float(lat) )
        # Create a feature, using the attributes/fields that are
        # required for this layer
        feat = ogr.Feature(feature_def=dst_layer.GetLayerDefn())
        # Feed the WKT into a geometry
        p = ogr.CreateGeometryFromWkt( wkt )
        # Feed the geometry into a WKT
        feat.SetGeometryDirectly( p )
        # Set the name field to its value
        feat.SetField ( "name", park_name )
        # Attach the feature to the layer
        dst_layer.CreateFeature( feat )
        # Clean up
        feat.Destroy()
    
    # Close file    
    dst_ds = None

You can see the result of this on
`github <https://gist.github.com/jgomezdans/6811102>`__.

Additionally, note that if we had defined a coordinate transformation as
in the raster session, we could apply this transformation to an OGR
geometry entity (in the snippet above, ``p`` would be such), and it
would be reprojected.

**Exercise** Modify the above snippet to output a GeoJSON file for the
Peak District National Park, whose UTM30N (`EPSG code:
32630 <http://spatialreference.org/ref/epsg/32630/>`__) co-ordinates are
:math:`577659, 5911841`.

.. raw:: html

   <script src="https://gist.github.com/jgomezdans/6811102.js"></script>

.. raw:: html

   <script src="https://gist.github.com/jgomezdans/6811102.js"></script>

Rasterising
-----------

A very frequent problem one finds is how to mask out an area in a raster
file that is defined as polygon in a shapefile. For example, if you have
a raster of the worlds population density, and you want to extract all
the pixels that belong to one particular country, how do you go about
that? One way around this is to *rasterise* the polygon(s), which
translates into "burning" pixels that fall within the polygon with a
number, resulting in a mask.

The way to do this is to use GDAL's ``RasterizeLayer`` method. The
method takes a handle to a GDAL dataset (one that you create yourself,
with the right projection and geotransform, as you've seen above), and a
OGR layer. The syntax for ``RasterizeLayer`` is

::

    err = gdal.RasterizeLayer ( raster_ds, [raster_band_no], ogr_layer, burn_values=[burn_val] )

where ``raster_ds`` is the GDAL raster datasource (note that it needs to
be georreferenced, *i.e.* it requires projection and geotransform),
``raster_band_no`` is the band of the GDAL dataset where we want to burn
pixels, ``ogr_layer`` is the vector layer object, and ``burn_val`` is
the value that we want to burn.

Let's use ``gdal.RasterizeLayer`` in conjunction with all that we have
covered above. Say we want to create a mask that only selects the UK or
Ireland in ``world.shp``, and we want to apply this mask to the MODIS
landcover product that we used in the GDAL session (h17v03 tile ), file
``lc_h17v03.tif``. We find that in this case, ``world.shp`` is in
longitude latitude, and the MODIS data is in the MODIS projection, so we
will reproject the vector data to match the MODIS data (so the latter is
not interpolated and artifacts introduced). To make this efficient and
avoid saving to disk, we shall use *in-memory vector and rasters*, and
we will output a numpy array as our mask. Note then the steps:

1. Crate the projection conversion object (as for GDAL before)
2. Create an in memory **raster** dataset to store the mask, using
   ``lc_h17v03.tif`` as a reference for geotransforms, array size and
   projection.
3. Create an in memory **vector** dataset to hold the features that will
   be reprojected
4. Open ``world.shp`` and apply an ``AttributeFilter`` to select a
   country
5. Select a geometry from ``world.shp``, project it and store it in the
   destination in memory vector layer
6. Once this is done, use ``gdal.RasterizeLayer`` with both in-memory
   raster and vector datasets
7. Read the in memory raster into an array

This is a particularly good exercise that will stress all that we have
learned so far.

.. code:: python

    
    
    reference_filename = "lc_h17v03.tif"
    target_vector_file = "world.shp"
    attribute_filter = "NAME = 'IRELAND'" 
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
    
    
    
    # Plotting to see whether this makes sense.
    
    ndata = g.ReadAsArray()
    plt.imshow ( ndata, interpolation='nearest', cmap=plt.cm.gray, vmin=0, vmax=1, alpha=0.3 )
    plt.hold ( True )
    
    plt.imshow ( data, interpolation='nearest', cmap=plt.cm.gray, alpha=0.7 )
    plt.grid ( False )
    plt.show()


.. image:: OGR_Python_files/OGR_Python_31_0.svg


Using matplotlib to plot geometries
-----------------------------------

Using matplotlib to plot geometries from OGR can be quite tedious.
Here's an example of plotting a map of Angola from the ``world.shp``. In
the same vein of recommending Shapely and Fiona above for serious
geoprocessing of vector data, you are encouraged to use
`descartes <https://bitbucket.org/sgillies/descartes/>`__ for plotting
vector data!

.. code:: python

    import matplotlib.path as mpath
    import matplotlib.patches as mpatches
    
    
    # Extract first layer of features from shapefile using OGR
    ds = ogr.Open('world.shp')
    lyr = ds.GetLayer(0)
    
    
    # Prepare figure
    plt.ioff()
    plt.subplot(1,1,1)
    ax = plt.gca()
    
    
    paths = []
    lyr.ResetReading()
    
    lyr.SetAttributeFilter ( " NAME = 'ANGOLA' ")
    ax.set_xlim(11, 24.5 )
    ax.set_ylim(-20, -2)
    # Read all features in layer and store as paths
    
    for feat in lyr:
    
        for geom in feat.GetGeometryRef():
            envelope = np.array( geom.GetEnvelope() )
            # check if geom is polygon
            if geom.GetGeometryType() == ogr.wkbPolygon:
                codes = []
                all_x = []
                all_y = []
                for i in range(geom.GetGeometryCount()):
                    # Read ring geometry and create path
                    r = geom.GetGeometryRef(i)
                    x = [r.GetX(j) for j in range(r.GetPointCount())]
                    y = [r.GetY(j) for j in range(r.GetPointCount())]
                    # skip boundary between individual rings
                    codes += [mpath.Path.MOVETO] + \
                                 (len(x)-1)*[mpath.Path.LINETO]
                    all_x += x
                    all_y += y
                path = mpath.Path(np.column_stack((all_x,all_y)), codes)
                paths.append(path)
        # Add paths as patches to axes
        for path in paths:
            patch = mpatches.PathPatch(path, \
                    facecolor='0.8', edgecolor='black')
            ax.add_patch(patch)
    
    
    
    ax.set_aspect(1.0)
    plt.show()


.. image:: OGR_Python_files/OGR_Python_34_0.svg

