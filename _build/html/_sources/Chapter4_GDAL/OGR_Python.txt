
Working with vector data: OGR
=============================

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

.. parsed-literal::

    --2013-10-22 15:47:43--  http://aprsworld.net/gisdata/world/world.zip
    Resolving aprsworld.net... 72.251.203.219
    Connecting to aprsworld.net|72.251.203.219|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 3436277 (3.3M) [application/zip]
    Saving to: `world.zip.1'
    
    100%[======================================>] 3,436,277   3.28M/s   in 1.0s    
    
    2013-10-22 15:47:45 (3.28 MB/s) - `world.zip.1' saved [3436277/3436277]
    
    Archive:  world.zip
      inflating: world.dbf               
      inflating: world.shp               
      inflating: world.shx               


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

.. parsed-literal::

    GUATEMALA
    BOLIVIA
    PARAGUAY
    URUGUAY
    SURINAME
    FRENCH GUIANA
    WESTERN SAHARA
    GAMBIA
    MOROCCO
    MALI


If you wanted to see the different layers, we could do this using:

.. code:: python

    layerDefinition = layer.GetLayerDefn()
    
    
    for i in range(layerDefinition.GetFieldCount()):
        print "Field %d: %s" % ( i+1, layerDefinition.GetFieldDefn(i).GetName() )

.. parsed-literal::

    Field 1: NAME
    Field 2: CAPITAL
    Field 3: APPROX
    Field 4: AREA
    Field 5: SOURCETHM


Each feature, in addition to the fields shown agove, will have a
``Geometry`` field. We get a handle to this using the
``GetGeometryRef()`` method. Geometries have many methods, such as
``ExportToKML()`` to export to KML (Google Maps/Earth format):

.. code:: python

    the_geometry = feat.GetGeometryRef()
    the_geometry.ExportToKML()



.. parsed-literal::

    '<Polygon><outerBoundaryIs><LinearRing><coordinates>-12.0443,14.669667 -11.87845,14.8252 -11.76455,15.039033 -11.63345,15.335633 -11.58515,15.634533 -11.52995,15.6713 -11.34705,15.6736 -11.26425,15.6529 -11.2125,15.549433 -11.1849,15.3092 -11.0503,15.097667 -10.9675,15.086167 -10.53275,15.365533 -9.70465,15.364367 -9.52175,15.373567 -9.4631,15.440233 -9.43205,15.619567 -9.37685,15.658667 -9.13185,15.656367 -9.1385,15.489433 -8.1165,15.487567 -6.83415,15.504167 -5.513,15.483867 -5.25265,16.2627 -5.2693,16.3033 -5.58505,16.439867 -5.63765,16.5635 -5.7623,17.728033 -5.8814,18.589933 -6.02265,19.525633 -6.1362,20.697567 -6.3107,21.8621 -6.4575,22.952833 -6.4686,23.543433 -6.52675,23.8627 -6.7123,24.997733 -5.05065,24.9834 -5.00065,24.982967 -4.51805,24.628633 -2.77295,23.4557 -2.17905,23.0869 -1.6281,22.7265 -0.5692,22.030967 0.6009,21.241133 1.0281,21.001933 1.10095,20.985233 1.21475,20.9807 1.21475,20.807767 1.24435,20.7486 1.40825,20.609033 1.5517,20.5514 1.6678,20.3724 1.9421,20.185067 2.0514,20.172933 2.2221,20.168367 2.27785,20.157 2.3348,20.1312 2.4031,20.028033 2.4486,20.009833 2.6307,19.971933 2.8208,19.887733 3.12355,19.778533 3.21345,19.6458 3.19755,19.4501 3.15885,19.3242 3.10535,19.174767 3.13495,19.065567 3.2738,18.875933 3.3091,18.853933 3.3774,18.852433 3.52535,18.9131 3.82355,18.996533 4.34825,19.149 4.34725,19.115667 4.3451,19.045533 4.29825,18.466367 4.23895,17.8664 4.1984,17.276833 4.1766,16.666467 4.1423,16.331633 3.97065,16.208933 3.8864,16.099767 3.85205,15.8315 3.8146,15.700467 3.6305,15.5809 3.4245,15.5081 3.07805,15.428033 2.75035,15.396833 2.3197,15.323 2.10435,15.2731 1.8297,15.216967 1.62995,15.213833 1.41145,15.120267 1.05565,15.0402 0.8809,15.046433 0.6905,15.0402 0.61245,14.965333 0.52195,14.890467 0.419,14.856167 0.238,14.858267 0.1196,14.8782 -0.2863,15.048533 -0.614,15.108833 -0.75445,15.1109 -0.82935,15.094267 -0.94485,15.018367 -1.285,14.7418 -1.4754,14.625333 -1.6439,14.5723 -1.94035,14.462067 -2.16195,14.312333 -2.24625,14.2094 -2.3118,14.0472 -2.42415,13.939067 -2.69255,13.824667 -2.77995,13.596967 -3.1014,13.524167 -3.3573,13.452433 -3.53205,13.248633 -3.6725,13.2341 -3.84105,13.232 -4.0564,13.2653 -4.1001,13.256967 -4.22805,13.0386 -4.24135,12.8486 -4.5398,12.277633 -4.72495,12.088433 -4.7833,12.04 -4.8209,12.017533 -4.8687,12.0 -5.03205,11.943633 -5.40485,11.807433 -5.4576,11.7805 -5.46435,11.758033 -5.39025,11.609867 -5.38015,11.431733 -5.43175,11.337433 -5.443,11.246133 -5.39135,11.051533 -5.40035,10.9767 -5.5171,10.836 -5.52835,10.806067 -5.5073,10.733367 -5.5285,10.681033 -5.5168,10.6259 -5.46805,10.575 -5.4553,10.5029 -5.46805,10.409567 -5.50265,10.376233 -5.5873,10.2946 -5.72715,10.208567 -5.8078,10.1817 -5.96645,10.1602 -6.0444,10.1602 -6.13045,10.187067 -6.1466,10.212167 -6.1466,10.260567 -6.0928,10.3466 -6.13855,10.4595 -6.17615,10.486367 -6.20305,10.486367 -6.238,10.477433 -6.2837,10.429033 -6.3469,10.4165 -6.40875,10.421867 -6.5405,10.4595 -6.5835,10.450533 -6.6319,10.423667 -6.6561,10.3878 -6.66415,10.307167 -6.7018,10.267733 -6.74755,10.256967 -6.8228,10.256967 -6.87255,10.239033 -6.9801,10.151233 -7.06885,10.1315 -7.20595,10.1315 -7.30005,10.1602 -7.33095,10.194267 -7.35785,10.310767 -7.41165,10.341233 -7.45735,10.353767 -7.7101,10.351967 -7.7531,10.4882 -7.8284,10.525833 -7.9427,10.529433 -8.19545,10.5366 -8.26805,10.545533 -8.33525,10.5814 -8.3339,10.619033 -8.28015,10.7176 -8.17795,10.921933 -8.20755,10.9524 -8.3124,10.982867 -8.385,10.9739 -8.42265,10.947033 -8.51945,10.807233 -8.627,10.771367 -8.67,10.7696 -8.68615,10.783933 -8.68615,10.8162 -8.6458,10.889667 -8.6458,10.904 -8.68885,10.9273 -8.6915,10.9775 -8.68615,11.038433 -8.666,11.102967 -8.6176,11.149567 -8.28955,11.3449 -8.4401,11.4435 -8.77625,11.5761 -8.86635,11.6263 -8.8986,11.674667 -8.88245,11.7123 -8.76415,11.8969 -8.748,11.998 -8.75615,12.0537 -8.9702,12.136333 -8.90365,12.335867 -9.1426,12.388267 -9.36645,12.279433 -9.7355,12.1323 -9.80655,12.0866 -9.96635,12.0 -10.0388,11.958267 -10.1407,11.925833 -10.31445,11.925867 -10.3944,11.966 -10.4546,11.986067 -10.4917,11.987633 -10.5241,11.975267 -10.5465,11.9559 -10.5583,11.948633 -10.56825,11.944533 -10.5777,11.943933 -10.58715,11.9458 -10.6018,11.9581 -10.6155,11.973867 -10.6342,12.0 -10.6706,12.034 -10.6969,12.058533 -10.72995,12.058533 -10.8209,12.019967 -10.8457,12.019967 -10.8953,12.053 -10.92835,12.149433 -10.91185,12.3257 -10.9201,12.3615 -10.97385,12.358733 -11.12265,12.237567 -11.17225,12.033733 -11.4244,12.141167 -11.56495,12.254067 -11.60215,12.303667 -11.3913,12.429 -11.4946,12.489567 -11.4326,12.610767 -11.5401,12.6824 -11.5649,12.7237 -11.57315,12.756767 -11.4905,12.988133 -11.5194,13.096933 -11.7385,13.336567 -11.8625,13.325567 -11.9989,13.344833 -12.08155,13.416433 -12.08985,13.4798 -12.0774,13.866767 -12.0443,14.669667</coordinates></LinearRing></outerBoundaryIs></Polygon>'



Many of the methods that don't start with ``__`` are interesting. Let's
see what these are. typically, the interesting methods start with an
upper case letter, so we'll only show those:

.. code:: python

    for m in dir ( the_geometry ):
        if m[0].isupper():
            print m

.. parsed-literal::

    AddGeometry
    AddGeometryDirectly
    AddPoint
    AddPoint_2D
    Area
    AssignSpatialReference
    Boundary
    Buffer
    Centroid
    Clone
    CloseRings
    Contains
    ConvexHull
    Crosses
    Destroy
    Difference
    Disjoint
    Distance
    Empty
    Equal
    Equals
    ExportToGML
    ExportToJson
    ExportToKML
    ExportToWkb
    ExportToWkt
    FlattenTo2D
    GetArea
    GetBoundary
    GetCoordinateDimension
    GetDimension
    GetEnvelope
    GetEnvelope3D
    GetGeometryCount
    GetGeometryName
    GetGeometryRef
    GetGeometryType
    GetPoint
    GetPointCount
    GetPoint_2D
    GetPoints
    GetSpatialReference
    GetX
    GetY
    GetZ
    Intersect
    Intersection
    Intersects
    IsEmpty
    IsRing
    IsSimple
    IsValid
    Length
    Overlaps
    PointOnSurface
    Segmentize
    SetCoordinateDimension
    SetPoint
    SetPoint_2D
    Simplify
    SimplifyPreserveTopology
    SymDifference
    SymmetricDifference
    Touches
    Transform
    TransformTo
    Union
    UnionCascaded
    Within
    WkbSize


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
    import os
    from osgeo import ogr,osr
    
    
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

    from osgeo import ogr,osr
    import gdal
    
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


.. image:: OGR_Python_files/OGR_Python_28_0.png


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


.. image:: OGR_Python_files/OGR_Python_31_0.png

