
.. raw:: html

   <table border="" width=100% cellpadding=0><tr>
   <td bgcolor="#232323" border="">

.. raw:: html

   </td>
   </tr>
   <td bgcolor="#9ABAE2" border="">
   </td>
   </table>

Read and use some different file formats
========================================

In this session, we will learn to use some geospatial tools using GDAL
in Python. A good set of working notes on how to use GDAL has been
developed that you will find useful for background reading.

`HDF <http://www.hdfgroup.org/HDF-FAQ.html>`__\ (Hierarchical Data
Format) and `HDF-EOS <http://hdfeos.org/>`__ are common formats for EO
data so you need to have some idea how to use and manipulate them.

A hierarchical data format is essentially a format that ‘packs’ together
various aspects of a dataset (metadata, raster data etc.) into a binary
file. There are many tools for manipulating and reading HDF in python,
but we will use one of the more generic tools,
`gdal <http://gdal.org>`__ here.

When using HDF files, we need to have some idea of the stucture of the
contents, although you can clearly explore that yourself in an
interactive session. MODIS products have extensive information available
to help you interpret the datasets, for example the MODIS LAI/fAPAR
product
`MOD15A2 <https://lpdaac.usgs.gov/products/modis_products_table/leaf_area_index_fraction_of_photosynthetically_active_radiation/8_day_l4_global_1km/mod15a2>`__.
We will use this as an example to explore a dataset.

You will need access to the file
```MCD15A2.A2011185.h09v05.005.2011213154534.hdf`` <http://www2.geog.ucl.ac.uk/~plewis/geogg122/_images/MCD15A2.A2011185.h09v05.005.2011213154534.hdf>`__,
which you might access from the `MODIS Land Products
site <https://lpdaac.usgs.gov/>`__

Before going into the Python coding for GDAL, it is worthwhile looking
over some of the tools that are provided with GDAL and that can be run
from the shell. In particular, we can use the ``gdalinfo`` program, that
takes a filename and will output a copious description of the data,
including metadata, but also geogrpahic projection, size, number of
bands, etc.

.. code:: python

    !gdalinfo MCD15A2.A2011185.h09v05.005.2011213154534.hdf 

.. parsed-literal::

    Driver: HDF4/Hierarchical Data Format Release 4
    Files: MCD15A2.A2011185.h09v05.005.2011213154534.hdf
    Size is 512, 512
    Coordinate System is `'
    Metadata:
      HDFEOSVersion=HDFEOS_V2.9
      LOCALGRANULEID=MCD15A2.A2011185.h09v05.005.2011213154534.hdf
      PRODUCTIONDATETIME=2011-08-01T15:45:34.000Z
      DAYNIGHTFLAG=Day
      REPROCESSINGACTUAL=reprocessed
      LOCALVERSIONID=5.0.4
      REPROCESSINGPLANNED=further update is anticipated
      SCIENCEQUALITYFLAG=Not Investigated
      AUTOMATICQUALITYFLAGEXPLANATION=No automatic quality assessment is performed in the PGE
      AUTOMATICQUALITYFLAG=Passed
      SCIENCEQUALITYFLAGEXPLANATION=See http://landweb.nascom/nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aqua the product Science Quality status.
      QAPERCENTMISSINGDATA=3
      QAPERCENTOUTOFBOUNDSDATA=3
      QAPERCENTCLOUDCOVER=23
      QAPERCENTINTERPOLATEDDATA=0
      PARAMETERNAME=MCD15A2
      VERSIONID=5
      SHORTNAME=MCD15A2
      INPUTPOINTER=MYD15A1.A2011192.h09v05.005.2011194222549.hdf, MYD15A1.A2011191.h09v05.005.2011194224921.hdf, MYD15A1.A2011190.h09v05.005.2011192044353.hdf, MYD15A1.A2011189.h09v05.005.2011191043320.hdf, MYD15A1.A2011188.h09v05.005.2011190043751.hdf, MYD15A1.A2011187.h09v05.005.2011189125127.hdf, MYD15A1.A2011186.h09v05.005.2011188044024.hdf, MYD15A1.A2011185.h09v05.005.2011187152544.hdf, MOD15A1.A2011192.h09v05.005.2011194044548.hdf, MOD15A1.A2011191.h09v05.005.2011193042953.hdf, MOD15A1.A2011190.h09v05.005.2011192045720.hdf, MOD15A1.A2011189.h09v05.005.2011191045425.hdf, MOD15A1.A2011188.h09v05.005.2011190045726.hdf, MOD15A1.A2011187.h09v05.005.2011189045204.hdf, MOD15A1.A2011186.h09v05.005.2011188195439.hdf, MOD15A1.A2011185.h09v05.005.2011210211523.hdf, MCD15A2_ANC_RI4.hdf
      GRINGPOINTLONGITUDE=-103.835851753394, -117.486656023174, -104.256722414513, -92.131858571552
      GRINGPOINTLATITUDE=29.8360532722546, 39.9999999964079, 40.0742066197196, 29.9009502428382
      GRINGPOINTSEQUENCENO=1, 2, 3, 4
      EXCLUSIONGRINGFLAG=N
      RANGEENDINGDATE=2011-07-11
      RANGEENDINGTIME=23:59:59
      RANGEBEGINNINGDATE=2011-07-04
      RANGEBEGINNINGTIME=00:00:00
      PGEVERSION=5.0.9
      ASSOCIATEDSENSORSHORTNAME=MODIS
      ASSOCIATEDPLATFORMSHORTNAME=Terra
      ASSOCIATEDINSTRUMENTSHORTNAME=MODIS
      ASSOCIATEDSENSORSHORTNAME=MODIS
      ASSOCIATEDPLATFORMSHORTNAME=Aqua
      ASSOCIATEDINSTRUMENTSHORTNAME=MODIS
      QAPERCENTGOODQUALITY=100
      QAPERCENTOTHERQUALITY=100
      HORIZONTALTILENUMBER=09
      VERTICALTILENUMBER=05
      TileID=51009005
      NDAYS_COMPOSITED=16
      QAPERCENTGOODFPAR=100
      QAPERCENTGOODLAI=100
      QAPERCENTMAINMETHOD=100
      QAPERCENTEMPIRICALMODEL=0
      NORTHBOUNDINGCOORDINATE=39.9999999964079
      SOUTHBOUNDINGCOORDINATE=29.9999999973059
      EASTBOUNDINGCOORDINATE=-92.3664205550513
      WESTBOUNDINGCOORDINATE=-117.486656023174
      ALGORITHMPACKAGEACCEPTANCEDATE=10-01-2004
      ALGORITHMPACKAGEMATURITYCODE=Normal
      ALGORITHMPACKAGENAME=MCDPR_15A2
      ALGORITHMPACKAGEVERSION=5
      GEOANYABNORMAL=False
      GEOESTMAXRMSERROR=50.0
      LONGNAME=MODIS/Terra+Aqua Leaf Area Index/FPAR 8-Day L4 Global 1km SIN Grid
      PROCESSINGCENTER=MODAPS
      SYSTEMFILENAME=MYD15A1.A2011192.h09v05.005.2011194222549.hdf, MYD15A1.A2011191.h09v05.005.2011194224921.hdf, MYD15A1.A2011190.h09v05.005.2011192044353.hdf, MYD15A1.A2011189.h09v05.005.2011191043320.hdf, MYD15A1.A2011188.h09v05.005.2011190043751.hdf, MYD15A1.A2011187.h09v05.005.2011189125127.hdf, MYD15A1.A2011186.h09v05.005.2011188044024.hdf, MYD15A1.A2011185.h09v05.005.2011187152544.hdf, MOD15A1.A2011192.h09v05.005.2011194044548.hdf, MOD15A1.A2011191.h09v05.005.2011193042953.hdf, MOD15A1.A2011190.h09v05.005.2011192045720.hdf, MOD15A1.A2011189.h09v05.005.2011191045425.hdf, MOD15A1.A2011188.h09v05.005.2011190045726.hdf, MOD15A1.A2011187.h09v05.005.2011189045204.hdf, MOD15A1.A2011186.h09v05.005.2011188195439.hdf, MOD15A1.A2011185.h09v05.005.2011210211523.hdf
      NUMBEROFGRANULES=1
      GRANULEDAYNIGHTFLAG=Day
      GRANULEBEGINNINGDATETIME=2011-07-29T21:15:23.000Z
      GRANULEENDINGDATETIME=2011-07-29T21:15:23.000Z
      CHARACTERISTICBINANGULARSIZE=30.0
      CHARACTERISTICBINSIZE=926.625433055556
      DATACOLUMNS=1200
      DATAROWS=1200
      GLOBALGRIDCOLUMNS=43200
      GLOBALGRIDROWS=21600
      NADIRDATARESOLUTION=1km
      MAXIMUMOBSERVATIONS=1
      SPSOPARAMETERS=5367, 2680
      PROCESSINGENVIRONMENT=Linux minion5559 2.6.18-238.12.1.el5PAE #1 SMP Tue May 31 14:02:45 EDT 2011 i686 i686 i386 GNU/Linux
      DESCRREVISION=5.0
      ENGINEERING_DATA=
    # MOD_PR15A2 (Vers 5.0.4 Rele 10.18.2006 23:59)
    # MUM API Vers 2.5.8 Rev 104 Rel. 11.15.2000 10:49 (pgs)
    # (c) 2000 J.M. Glassy, NTSG,LLSD
    # portions of MUM API by Petr Votava,NTSG Lab,U.Montana
    # HOST ECS_PGS_VirtualHost PROCESS 19540618
    # PLATFORM Sys genericunix Vers unknown Release unknown Node (no nodename available)
    # INIT-TIME Mon Aug  1 11:45:14 2011
    
    YEARDAY 185 COMPOSITE_PERIOD  24 FIRSTDAY_IN_PERIOD 185
    SDS[PGE34_ISG_MBRLUT] %ID 268697600 Rank   2 (664 120)
    SDS[PGE34_OUTFIELD_PROP] %ID 268697601 Rank   2 (78 179)
    SDS[PGE34_BROWSEFIELD_PROP] %ID 268697602 Rank   2 (77 164)
    READANC SDS[PGE34_ISG_MBRLUT] RANK 2 (664 120)
    READANC SDS[PGE34_OUTFIELD_PROP] RANK 2 (78 179)
    READANC SDS[PGE34_BROWSEFIELD_PROP] RANK 2 (77 164)
    READANC SDS[PGE34_ECSMETA_DICT] RANK 2 (73 110)
    READANC SDS[PGE34_RELEASE_NOTES] RANK 2 (84 98)
    FLDPROP SDSnam(PGE34_OUTFIELD_PROP)MoleName(PGE34_OUTFIELD_PROP)Status 3 Nelem 13962
    BROWSE cvlBrwMol 0 Nelem 57600 Type 21 Status 3
    BROWSE cvlBrwMol 1 Nelem 57600 Type 21 Status 3
    BROWSE cvlBrwMol 2 Nelem 57600 Type 21 Status 3
    BROWSE cvlBrwMol 3 Nelem 57600 Type 21 Status 3
    BROWSE: NEW GRID ID 4194320
    BROWSEFIELD  0 Sum 1725178 Average 29.951
    BROWSEFIELD  1 Sum 581056 Average 10.0878
    BROWSEFIELD  2 Sum 358279 Average 6.22012
    BROWSEFIELD  3 Sum 8016362 Average 139.173
    BROWSE-DONE: N-Pixels 57600 Invalid offsets: 0 OutOfRange 0
    
    COMPOSITING FPAR FREQUENCIES
    FPAR   0       34
    FPAR   1       71
    FPAR   2       21
    FPAR   3       50
    FPAR   4      221
    FPAR   5      592
    FPAR   6     4712
    FPAR   7     1445
    FPAR   8      522
    FPAR   9     1210
    FPAR  10    12969
    FPAR  11    17195
    FPAR  12    83945
    FPAR  13   197436
    FPAR  14    79525
    FPAR  15    55842
    FPAR  16    68815
    FPAR  17    40112
    FPAR  18    62851
    FPAR  19    42180
    FPAR  20    43324
    FPAR  21    34354
    FPAR  22    20947
    FPAR  23    29184
    FPAR  24    35510
    FPAR  25    32078
    FPAR  26    34318
    FPAR  27    24998
    FPAR  28    28379
    FPAR  29    18195
    FPAR  30    17813
    FPAR  31    15146
    FPAR  32    10109
    FPAR  33    14734
    FPAR  34    17210
    FPAR  35    23089
    FPAR  36    14491
    FPAR  37    15924
    FPAR  38    15249
    FPAR  39    15657
    FPAR  40     9683
    FPAR  41     9847
    FPAR  42     7833
    FPAR  43    11433
    FPAR  44    12093
    FPAR  45    10148
    FPAR  46     9235
    FPAR  47    11742
    FPAR  48    10464
    FPAR  49     8277
    FPAR  50     5914
    FPAR  51     8763
    FPAR  52     6712
    FPAR  53     6807
    FPAR  54     9616
    FPAR  55     7249
    FPAR  56     5771
    FPAR  57     6052
    FPAR  58     5514
    FPAR  59     6665
    FPAR  60     5731
    FPAR  61     5195
    FPAR  62     5484
    FPAR  63     4754
    FPAR  64     4820
    FPAR  65     4963
    FPAR  66     3775
    FPAR  67     4243
    FPAR  68     4047
    FPAR  69     3461
    FPAR  70     2613
    FPAR  71     3143
    FPAR  72     2812
    FPAR  73     2463
    FPAR  74     1918
    FPAR  75     1894
    FPAR  76     1938
    FPAR  77     1574
    FPAR  78     1329
    FPAR  79     1287
    FPAR  80     1165
    FPAR  81     1210
    FPAR  82     1268
    FPAR  83     1501
    FPAR  84     1562
    FPAR  85     1466
    FPAR  86     1875
    FPAR  87     1865
    FPAR  88     2695
    FPAR  89     8083
    FPAR  90     4573
    FPAR  91      800
    FPAR  92      830
    FPAR  93      723
    FPAR  94      446
    FPAR  95      146
    FPAR  96       59
    FPAR  97       52
    FPAR  98       26
    FPAR  99        6
    FPAR 100        1
    
    COMPOSITING LAI FREQUENCIES
    LAI    0      135
    LAI    1     7017
    LAI    2   333047
    LAI    3   320752
    LAI    4   116468
    LAI    5   116636
    LAI    6    95497
    LAI    7    74899
    LAI    8    46317
    LAI    9    30182
    LAI   10    38262
    LAI   11    28509
    LAI   12    20955
    LAI   13    16270
    LAI   14    18420
    LAI   15    13305
    LAI   16    13099
    LAI   17    10446
    LAI   18     6287
    LAI   19     8236
    LAI   20     6428
    LAI   21     5986
    LAI   22     5851
    LAI   23     4651
    LAI   24     3958
    LAI   25     4149
    LAI   26     3228
    LAI   27     2795
    LAI   28     2712
    LAI   29     2032
    LAI   30     1961
    LAI   31     1927
    LAI   32     1557
    LAI   33     1448
    LAI   34     1445
    LAI   35     1123
    LAI   36     1135
    LAI   37      991
    LAI   38      849
    LAI   39      748
    LAI   40      771
    LAI   41      712
    LAI   42      641
    LAI   43      655
    LAI   44      816
    LAI   45      947
    LAI   46      965
    LAI   47      947
    LAI   48      934
    LAI   49      948
    LAI   50      758
    LAI   51      677
    LAI   52      662
    LAI   53      727
    LAI   54      651
    LAI   55      643
    LAI   56      789
    LAI   57      790
    LAI   58      613
    LAI   59      868
    LAI   60      676
    LAI   61      776
    LAI   62     3217
    LAI   63      796
    LAI   64      608
    LAI   65     2298
    LAI   66     4179
    LAI   67      166
    LAI   68      123
    LAI   69        5
    
    COMPOSITING DAY INDEX FREQUENCIES
    TILE-INDEX    0 Selection Frequency:   177256
    TILE-INDEX    1 Selection Frequency:   143267
    TILE-INDEX    2 Selection Frequency:   164215
    TILE-INDEX    3 Selection Frequency:   128123
    TILE-INDEX    4 Selection Frequency:   168637
    TILE-INDEX    5 Selection Frequency:    99292
    TILE-INDEX    6 Selection Frequency:   110562
    TILE-INDEX    7 Selection Frequency:    61898
    TILE-INDEX    8 Selection Frequency:    27366
    TILE-INDEX    9 Selection Frequency:    89455
    TILE-INDEX   10 Selection Frequency:    32747
    TILE-INDEX   11 Selection Frequency:    73910
    TILE-INDEX   12 Selection Frequency:    43557
    TILE-INDEX   13 Selection Frequency:    26380
    TILE-INDEX   14 Selection Frequency:    36942
    TILE-INDEX   15 Selection Frequency:    14464
    
    LOCALGRANULEID [MCD15A2.A2011185.h09v05.005.2011213154534.hdf]
    ECS QC PERCENT N valid (demominator) : 1398071.000000
    ECS Total Pixels       (denominator) : 1440000
    
    QAPERCENTxx PSA BEFORE CALC
    QAPERCENTINTERPOLATEDDATA: 0
    QAPERCENTMISSINGDATA     : 41929
    QAPERCENTOUTOFBOUNDSDATA : 41929
    QAPERCENTCLOUDCOVER      : 334183
    QAPERCENTNOTPRODUCEDCLOUD: 0
    QAPERCENTNOTPRODUCEDOTHER: 0
    QAPERCENTGOODQUALITY     : 1391137
    QAPERCENTOTHERQUALITY    : 48863
    QAPERCENTGOODFPAR        : 1391137
    QAPERCENTGOODLAI         : 1391137
    QAPERCENTMAINMETHOD      : 1391137
    QAPERCENTEMPIRICALMODEL  : 6934
    QAPERCENTNDAYSCOMPOSITED : 16
    QAPERCENTTERRA           : 1052272
    
    
    QAPERCENTxx PSA AFTER CALC
    QAPERCENTINTERPOLATEDDATA: 0
    QAPERCENTMISSINGDATA     : 3
    QAPERCENTOUTOFBOUNDSDATA : 3
    QAPERCENTCLOUDCOVER      : 23
    QAPERCENTNOTPRODUCEDCLOUD: 0
    QAPERCENTNOTPRODUCEDOTHER: 0
    QAPERCENTGOODQUALITY     : 100
    QAPERCENTOTHERQUALITY    : 100
    QAPERCENTGOODFPAR        : 100
    QAPERCENTGOODLAI         : 100
    QAPERCENTMAINMETHOD      : 100
    QAPERCENTEMPIRICALMODEL  : 0
    QAPERCENTNDAYSCOMPOSITED : 16
    
    
    SESSION ENGINEERING SUMMARY FOR PGE34 8-day FPAR,LAI
    UM_VERSION U.MONTANA MODIS PGE34 Vers 5.0.4 Rev 4 Release 10.18.2006 23:59
    Candidate Days: 16
    
    N. invalid loads      : 0
    Pixels failing best day : 41929
    Pixels set to fill      : 0
    Pixels skipped (disqual): 1118070
    Unclassified Pixels     : 41929
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011185.h09v05.005.2011210211523.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011186.h09v05.005.2011188195439.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011187.h09v05.005.2011189045204.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011188.h09v05.005.2011190045726.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011189.h09v05.005.2011191045425.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011190.h09v05.005.2011192045720.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011191.h09v05.005.2011193042953.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MOD15A1.A2011192.h09v05.005.2011194044548.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011185.h09v05.005.2011187152544.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011186.h09v05.005.2011188044024.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011187.h09v05.005.2011189125127.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011188.h09v05.005.2011190043751.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011189.h09v05.005.2011191043320.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011190.h09v05.005.2011192044353.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011191.h09v05.005.2011194224921.hdf
    MOD15A1 DAILY Input: /MODAPSops8/archive/f5559/running/AMPM_L10m/6913096/MYD15A1.A2011192.h09v05.005.2011194222549.hdf
    
    PGE34 Output       : /MODAPSx/archive/f5559/ops8/running/AMPM_L10m/6913096/MCD15A2.1.2011-185T00:00:00.000000Z.51009005.8618434.215230_1.hdf
    MOD15A2 ANCILLARY    : /MODAPSops8/PGE/AMPM/coeff/PGE34/MCD15A2_ANC_RI4.hdf
    
    QAPERCENTxx PSA AFTER CALC
    QAPERCENTINTERPOLATEDDATA: 0
    QAPERCENTMISSINGDATA     : 3
    QAPERCENTOUTOFBOUNDSDATA : 3
    QAPERCENTCLOUDCOVER      : 23
    QAPERCENTTERRA          : 75
    QAPERCENTGOODQUALITY     : 100
    QAPERCENTOTHERQUALITY    : 100
    QAPERCENTGOODFPAR        : 100
    QAPERCENTGOODLAI         : 100
    QAPERCENTMAINMETHOD      : 100
    QAPERCENTEMPIRICALMODEL  : 0
    QAPERCENTNDAYSCOMPOSITED : 16
    
    
    Started Mon Aug  1 11:45:14 2011  Ended Mon Aug  1 11:45:34 2011
    Elapsed Time          20 Sec (       0.33 Min)
      MOD15A2_FILLVALUE_DOC=MOD15A2 FILL VALUE LEGEND
    255 = _Fillvalue, assigned when:
        * the MODAGAGG suf. reflectance for channel VIS, NIR was assigned its _Fillvalue, or
        * land cover pixel itself was assigned _Fillvalus 255 or 254.
    254 = land cover assigned as perennial salt or inland fresh water.
    253 = land cover assigned as barren, sparse vegetation (rock, tundra, desert.)
    252 = land cover assigned as perennial snow, ice.
    251 = land cover assigned as "permanent" wetlands/inundated marshlands.
    250 = land cover assigned as urban/built-up.
    249 = land cover assigned as "unclassified" or not able to determine.
    
      MOD15A2_FparLai_QC_DOC=
    FparLai_QC 5 BITFIELDS IN 8 BITWORD
    MODLAND_QC START 0 END 0 VALIDS 2
    MODLAND_QC   0 = Good Quality (main algorithm with or without saturation)
    MODLAND_QC   1 = Other Quality (back-up algorithm or fill value)
    SENSOR START 1 END 1 VALIDS 2
    SENSOR       0  = Terra
    SENSOR       1  = Aqua
    DEADDETECTOR START 2 END 2 VALIDS 2
    DEADDETECTOR 0 = Detectors apparently fine for up to 50% of channels 1,2
    DEADDETECTOR 1 = Dead detectors caused >50% adjacent detector retrieval
    CLOUDSTATE START 3 END 4 VALIDS 4 (this inherited from Aggregate_QC bits {0,1} cloud state)
    CLOUDSTATE   00 = 0 Significant clouds NOT present (clear)
    CLOUDSTATE   01 = 1 Significant clouds WERE present
    CLOUDSTATE   10 = 2 Mixed cloud present on pixel
    CLOUDSTATE   11 = 3 Cloud state not defined,assumed clear
    SCF_QC START 5 END 7 VALIDS 5
    SCF_QC       000=0 Main (RT) algorithm used, best result possible (no saturation)
    SCF_QC       001=1 Main (RT) algorithm used, saturation occured. Good, very usable.
    SCF_QC       010=2 Main algorithm failed due to bad geometry, empirical algorithm used
    SCF_QC       011=3 Main algorithm faild due to problems other than geometry, empirical algorithm used
    SCF_QC       100=4 Pixel not produced at all, value coudn't be retrieved (possible reasons: bad L1B data, unusable MODAGAGG data)
    
      MOD15A2_FparExtra_QC_DOC=
    FparExtra_QC 6 BITFIELDS IN 8 BITWORD
    LANDSEA PASS-THROUGH START 0 END 1 VALIDS 4
    LANDSEA   00 = 0 LAND       AggrQC(3,5)values{001}
    LANDSEA   01 = 1 SHORE      AggrQC(3,5)values{000,010,100}
    LANDSEA   10 = 2 FRESHWATER AggrQC(3,5)values{011,101}
    LANDSEA   11 = 3 OCEAN      AggrQC(3,5)values{110,111}
    SNOW_ICE (from Aggregate_QC bits) START 2 END 2 VALIDS 2
    SNOW_ICE  0 = No snow/ice detected
    SNOW_ICE  1 = Snow/ice were detected
    AEROSOL START 3 END 3 VALIDS 2
    AEROSOL   0 = No or low atmospheric aerosol levels detected
    AEROSOL   1 = Average or high aerosol levels detected
    CIRRUS (from Aggregate_QC bits {8,9} ) START 4 END 4 VALIDS 2
    CIRRUS    0 = No cirrus detected
    CIRRUS    1 = Cirrus was detected
    INTERNAL_CLOUD_MASK START 5 END 5 VALIDS 2
    INTERNAL_CLOUD_MASK 0 = No clouds
    INTERNAL_CLOUD_MASK 1 = Clouds were detected
    CLOUD_SHADOW START 6 END 6 VALIDS 2
    CLOUD_SHADOW        0 = No cloud shadow detected
    CLOUD_SHADOW        1 = Cloud shadow detected
    SCF_BIOME_MASK START 7 END 7 VALIDS 2
    SCF_BIOME_MASK  0 = Biome outside interval <1,4>
    SCF_BIOME_MASK  1 = Biome in interval <1,4>
    
      MOD15A2_StdDev_QC_DOC=MOD15A2 STANDARD DEVIATION FILL VALUE LEGEND
    255 = _Fillvalue, assigned when:
        * the MODAGAGG suf. reflectance for channel VIS, NIR was assigned its _Fillvalue, or
        * land cover pixel itself was assigned _Fillvalus 255 or 254.
    254 = land cover assigned as perennial salt or inland fresh water.
    253 = land cover assigned as barren, sparse vegetation (rock, tundra, desert.)
    252 = land cover assigned as perennial snow, ice.
    251 = land cover assigned as "permanent" wetlands/inundated marshlands.
    250 = land cover assigned as urban/built-up.
    249 = land cover assigned as "unclassified" or not able to determine.
    248 = no standard deviation available, pixel produced using backup method.
    
      MOD15A1_ANC_BUILD_CERT=mtAncUtil v. 1.8 Rel. 09.11.2000 17:36 API v. 2.5.6 release 09.14.2000 16:33 Rev.Index 102 (J.Glassy)
    
      UM_VERSION=U.MONTANA MODIS PGE34 Vers 5.0.4 Rev 4 Release 10.18.2006 23:59
    Subdatasets:
      SUBDATASET_1_NAME=HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:Fpar_1km
      SUBDATASET_1_DESC=[1200x1200] Fpar_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
      SUBDATASET_2_NAME=HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:Lai_1km
      SUBDATASET_2_DESC=[1200x1200] Lai_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
      SUBDATASET_3_NAME=HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparLai_QC
      SUBDATASET_3_DESC=[1200x1200] FparLai_QC MOD_Grid_MOD15A2 (8-bit unsigned integer)
      SUBDATASET_4_NAME=HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparExtra_QC
      SUBDATASET_4_DESC=[1200x1200] FparExtra_QC MOD_Grid_MOD15A2 (8-bit unsigned integer)
      SUBDATASET_5_NAME=HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparStdDev_1km
      SUBDATASET_5_DESC=[1200x1200] FparStdDev_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
      SUBDATASET_6_NAME=HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:LaiStdDev_1km
      SUBDATASET_6_DESC=[1200x1200] LaiStdDev_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
    Corner Coordinates:
    Upper Left  (    0.0,    0.0)
    Lower Left  (    0.0,  512.0)
    Upper Right (  512.0,    0.0)
    Lower Right (  512.0,  512.0)
    Center      (  256.0,  256.0)


.. code:: python

    # Filter lines that do not have BOUNDINGCOORDINATE in them
    !gdalinfo MCD15A2.A2011185.h09v05.005.2011213154534.hdf | grep BOUNDINGCOORDINATE

.. parsed-literal::

      NORTHBOUNDINGCOORDINATE=39.9999999964079
      SOUTHBOUNDINGCOORDINATE=29.9999999973059
      EASTBOUNDINGCOORDINATE=-92.3664205550513
      WESTBOUNDINGCOORDINATE=-117.486656023174


We can check this against e.g. the `UNH MODIS tile
calculator <http://remotesensing.unh.edu/modis/modis.shtml>`__, just to
confirm that we have interpreted the coordinates correctly.

We can apply other shell GDAL tools, e.g. to perform a reprojection from
the native `MODIS
sinusoidal <http://modis-land.gsfc.nasa.gov/MODLAND_grid.html>`__
projection, to the `Contiguous United States NAD27 Albers Equal
Area <http://spatialreference.org/ref/sr-org/7271/>`__:

.. code:: python

    !gdalwarp -of GTiff \
        -t_srs '+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=23 +lon_0=-96 +x_0=0 +y_0=0 +ellps=clrk66 +units=m +no_defs'  \
        -tr 1000 1000 \
        'HDF4_EOS:EOS_GRID:MCD15A2.A2011185.h09v05.005.2011213154534.hdf:MOD_Grid_MOD15A2:Lai_1km' output_file.tif

.. parsed-literal::

    Creating output file that is 2152P x 1323L.
    Processing input file HDF4_EOS:EOS_GRID:MCD15A2.A2011185.h09v05.005.2011213154534.hdf:MOD_Grid_MOD15A2:Lai_1km.
    Using internal nodata values (eg. 255) for image HDF4_EOS:EOS_GRID:MCD15A2.A2011185.h09v05.005.2011213154534.hdf:MOD_Grid_MOD15A2:Lai_1km.
    0...10...20...30...40...50...60...70...80...90...100 - done.


where ``MCD15A2.A2011185.h09v05.005.2011213154534.hdf`` is the name of
the input HDF file, ``MOD_Grid_MOD15A2:Lai_1km`` is the data product we
want, and the rather menacing string
``+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=23 +lon_0=-96 +x_0=0 +y_0=0 +ellps=clrk66 +units=m +no_defs``
specifies the projection in Proj4 format. You can typically find the
projection you want on
`spatialreference.org <http://spatialreference.org>`__, and just copy
and paste the contents of `Proj4
definition <http://spatialreference.org/ref/sr-org/7271/proj4/>`__
(remember to surround it by quotes). The option ``-tr xres yres``
specifies the desired resolution of the output dataset (1000 by 1000 m
in the case above). ``-of GTiff`` specifies the GeoTiff format to be
used as as output.

Having some idea what information is in the hdf file then, we can
proceed to read the data in inside Python using the GDAL library:

.. code:: python

    import gdal # Import GDAL library bindings
    
    # The file that we shall be using
    # Needs to be on current directory
    filename = 'MCD15A2.A2011185.h09v05.005.2011213154534.hdf'
    
    g = gdal.Open(filename)
    # g should now be a GDAL dataset, but if the file isn't found
    # g will be none. Let's test this:
    if g is None:
        print "Problem opening file %s!" % filename
    else:
        print "File %s opened fine" % filename
        
        
    subdatasets = g.GetSubDatasets()
    for fname, name in subdatasets:
        print name
        print "\t", fname
    


.. parsed-literal::

    File MCD15A2.A2011185.h09v05.005.2011213154534.hdf opened fine
    [1200x1200] Fpar_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
    	HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:Fpar_1km
    [1200x1200] Lai_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
    	HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:Lai_1km
    [1200x1200] FparLai_QC MOD_Grid_MOD15A2 (8-bit unsigned integer)
    	HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparLai_QC
    [1200x1200] FparExtra_QC MOD_Grid_MOD15A2 (8-bit unsigned integer)
    	HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparExtra_QC
    [1200x1200] FparStdDev_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
    	HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparStdDev_1km
    [1200x1200] LaiStdDev_1km MOD_Grid_MOD15A2 (8-bit unsigned integer)
    	HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:LaiStdDev_1km


In the previous code snippet we have done a number of different things:

1. Import the GDAL library
2. Open a file with GDAL, storing a handler to the file in ``g``
3. Test that ``g`` is not ``None`` (as this indicates failure opening
   the file. Try changing ``filename`` above to something else)
4. We then use the ``GetSubDatasets()`` method to read out information
   on the different subdatasets available from this file (compare to the
   output of ``gdalinfo`` on the shelf earlier)
5. Loop over the retrieved subdatasets to print the name (human-readable
   information) and the GDAL filename. This last item is the filename
   that you need to use to tell GDAL to open a particular data layer of
   the 6 layers present in this example

Let's say that we want to access the LAI information. By contrasting the
output of the above code (or ``gdalinfo``) to the contents of the
`LAI/fAPAR product information
page <https://lpdaac.usgs.gov/products/modis_products_table/leaf_area_index_fraction_of_photosynthetically_active_radiation/8_day_l4_global_1km/mod15a2>`__,
we find out that we want the layers for ``Lai_1km``, ``FparLai_Qc``,
``FparExtra_QC`` and ``LaiStdDev_1km``.

To read these individual datasets, we need to open each of them
individually using GDAL, and the GDAL filenames used above:

.. code:: python

    # Let's create a list with the selected layer names
    selected_layers = [  "Lai_1km", "FparLai_QC", "FparExtra_QC",  "LaiStdDev_1km" ]
    # We will store the data in a dictionary
    # Initialise an empty dictionary
    data = {}
    # for convenience, we will use string substitution to create a 
    # template for GDAL filenames, which we'll substitute on the fly:
    file_template = 'HDF4_EOS:EOS_GRID:"%s":MOD_Grid_MOD15A2:%s'
    for i, layer in enumerate ( selected_layers ):
        this_file = file_template % ( filename, layer )
        print "Opening Layer %d: %s" % (i+1, this_file )
        g = gdal.Open ( this_file )
        
        if g is None:
            raise IOError
        data[layer] = g.ReadAsArray() 
        print "\t>>> Read %s!" % layer
        

.. parsed-literal::

    Opening Layer 1: HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:Lai_1km
    	>>> Read Lai_1km!
    Opening Layer 2: HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparLai_QC
    	>>> Read FparLai_QC!
    Opening Layer 3: HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:FparExtra_QC
    	>>> Read FparExtra_QC!
    Opening Layer 4: HDF4_EOS:EOS_GRID:"MCD15A2.A2011185.h09v05.005.2011213154534.hdf":MOD_Grid_MOD15A2:LaiStdDev_1km
    	>>> Read LaiStdDev_1km!


In the previous code, we have seen a way of neatly creating the
filenames required by GDAL to access the independent datasets: a
template string that gets substituted with the ``filename`` and the
``layer`` name. Note that the presence of double quotes in the template
requires us to use single quotes around it. The data is now stored in a
dictionary, and can be accessed as e.g. ``data['Lai_1km']``:

.. code:: python

    print read_data['Lai_1km']

.. parsed-literal::

    [[ 3  3  2 ...,  6  8 21]
     [ 4  3  6 ...,  8 18 14]
     [ 3 12 11 ..., 12  8  8]
     ..., 
     [ 2  3  2 ..., 18 11 17]
     [ 2  3  3 ..., 16 19 15]
     [ 3  2  2 ..., 15 16 15]]


Now we have to translate the LAI values into meaningful quantities.
According to the
`LAI <https://lpdaac.usgs.gov/products/modis_products_table/leaf_area_index_fraction_of_photosynthetically_active_radiation/8_day_l4_global_1km/mod15a2>`__
webpage, there is a scale factor of 0.1 involved for LAI and SD LAI:

.. code:: python

    lai = data['Lai_1km'] * 0.1
    lai_sd = data['LaiStdDev_1km'] * 0.1
.. code:: python

    print "LAI"
    print lai
    print "SD"
    print lai_sd

.. parsed-literal::

    LAI
    [[ 0.3  0.3  0.2 ...,  0.6  0.8  2.1]
     [ 0.4  0.3  0.6 ...,  0.8  1.8  1.4]
     [ 0.3  1.2  1.1 ...,  1.2  0.8  0.8]
     ..., 
     [ 0.2  0.3  0.2 ...,  1.8  1.1  1.7]
     [ 0.2  0.3  0.3 ...,  1.6  1.9  1.5]
     [ 0.3  0.2  0.2 ...,  1.5  1.6  1.5]]
    SD
    [[ 0.2  0.2  0.1 ...,  0.2  0.1  0.3]
     [ 0.2  0.2  0.2 ...,  0.2  0.3  0.2]
     [ 0.   0.1  0.2 ...,  0.1  0.2  0.2]
     ..., 
     [ 0.1  0.1  0.1 ...,  0.3  0.   0.1]
     [ 0.1  0.1  0.1 ...,  0.2  0.2  0.1]
     [ 0.1  0.1  0.1 ...,  0.1  0.2  0.1]]


Some SD values are clearly given as 0.0, which is unlikely to be true.
We should then examine the QC (Quality Control) information. The codes
for this are also given on the LAI product page. They are described as
bit combinations:

.. raw:: html

   <table>
   <tr>
   <th>

Bit No.

.. raw:: html

   </th>    <th>

Parameter Name

.. raw:: html

   </th><th> 

Bit Combination

.. raw:: html

   </th><th>

Explanation

.. raw:: html

   </th>
   <tr>
   <td>

0

.. raw:: html

   </td><td>

MODLAND\_QC bits

.. raw:: html

   </td><td>   

0

.. raw:: html

   </td><td>  

Good quality (main algorithm with or without saturation)

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Other Quality (back-up algorithm or fill values)

.. raw:: html

   </td>
   </tr>

   <tr>
   <td>

1

.. raw:: html

   </td><td>

Sensor

.. raw:: html

   </td><td>    

0

.. raw:: html

   </td><td>  

TERRA

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

AQUA

.. raw:: html

   </td>
   </tr>

   <tr>
   <td>

2

.. raw:: html

   </td><td>

DeadDetector

.. raw:: html

   </td><td>  

0

.. raw:: html

   </td><td>  

Detectors apparently fine for up to 50% of channels 1 2

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Dead detectors caused >50% adjacent detector retrieval

.. raw:: html

   </td>
   </tr>

   <tr>
   <td>

3-4

.. raw:: html

   </td><td>

CloudState

.. raw:: html

   </td><td> 

00

.. raw:: html

   </td><td> 

Significant clouds NOT present (clear)

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

01

.. raw:: html

   </td><td>

Significant clouds WERE present

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

10

.. raw:: html

   </td><td>

Mixed clouds present on pixel

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

11

.. raw:: html

   </td><td>

Cloud state not defined assumed clear

.. raw:: html

   </td>
   </tr>

   <tr>
   <td>

5-7

.. raw:: html

   </td><td>

CF\_QC

.. raw:: html

   </td><td>  

000

.. raw:: html

   </td><td>    

Main (RT) method used best result possible (no saturation)

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

001

.. raw:: html

   </td><td>

Main (RT) method used with saturation. Good very usable

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

010

.. raw:: html

   </td><td>

Main (RT) method failed due to bad geometry empirical algorithm used

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

011

.. raw:: html

   </td><td> 

Main (RT) method failed due to problems other than geometry empirical
algorithm used

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

100

.. raw:: html

   </td><td> 

Pixel not produced at all value coudn’t be retrieved (possible reasons:
bad L1B data unusable MODAGAGG data)

.. raw:: html

   </td>
   </tr>
   </table>

In using this information, it is up to the use which data he/she wants
to pass through for any further processing. There are clearly
trade-offs: if you look for only the highest quality data, then the
number of samples is likely to be lower than if you were more tolerant.
But if you are too tolerant, you will get spurious results. You may find
useful information on how to convert from actual QA flags to diagnostics
in `this page <http://gis.cri.fmach.it/modis-ndvi-evi/>`__ (they focus
on NDVI/EVI, but the theory is the same).

But let's just say that we want to use only the highest quality data.
From the table above, these data are given by the ``CF_QC`` flag being
set to ``000`` or ``001``, or in other words ``00000000`` and
``00000001``, or 0 and 1 in decimal:

.. code:: python

    import numpy as np
    import pylab as plt
    
    qc = data['FparLai_QC'] # Get the QC data
    # Create a mask like the LAI product
    mask = np.zeros_like(lai).astype(bool)
    # Fill the mask where the conditions are met
    mask = np.where ( qc == 0, True, False )
    mask = np.where ( qc == 1, True, mask )
    
    # Select a black/white colormap
    cmap = plt.cm.gray
    # plot the data
    plt.imshow(mask, interpolation='nearest', cmap=cmap)
    # add a colorbar
    plt.colorbar(ticks=[0,1])



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0xbb01b00>




.. image:: GDAL_HDF_files/GDAL_HDF_19_1.png


To plot LAI only for the valid pixels (``mask == True``). We can used
masked arrays for this. Masked arrays are like normal arrays, but they
have an associated mask, which in this case is ``mask`` define above. We
shall also choose another colormap (there are `lots to choose
from <http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps>`__), and
set values outside the 0.1 and 4 to be shown as black pixels.

.. code:: python

    cmap = plt.cm.Greens
    cmap.set_bad ( 'k' )
    laim = np.ma.array ( lai, mask=mask )
    plt.imshow ( laim, cmap=cmap, interpolation='nearest', vmin=0.1, vmax=4)
    plt.colorbar()



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0xd429e18>




.. image:: GDAL_HDF_files/GDAL_HDF_21_1.png


Similarly, we can do a similar thing for Standard Deviation

.. code:: python

    cmap = plt.cm.spectral
    cmap.set_bad ( 'k' )
    stdm = np.ma.array ( lai_sd, mask=mask )
    plt.imshow ( stdm, cmap=cmap, interpolation='nearest', vmin=0.001, vmax=0.5)
    plt.colorbar()



.. parsed-literal::

    <matplotlib.colorbar.Colorbar instance at 0x2b8ee20374d0>




.. image:: GDAL_HDF_files/GDAL_HDF_23_1.png


Exercise 1
----------

For the moment, we will suppose this data masking to be sufficient.
However, closer inspection of the `product
data <https://lpdaac.usgs.gov/products/modis_products_table/leaf_area_index_fraction_of_photosynthetically_active_radiation/8_day_l4_global_1km/mod15a2>`__
page would show us that the data can take on various Fill Values which
any data user should check for.

Modify the code we have developed above to also check that the data are
not unwanted ‘fill values’ and use this to modify the data mask.

*Hint* Note that these fill values are applied to Lai\_1km, not the QC
information, so you have to check values in that dataset and modify the
mask accordingly.

Exercise 2
----------

We also have access to ``FparExtra_QC``

::

    qc1  = data['FparExtra_QC']

The data values in FparExtra\_QC are:

.. raw:: html

   <table>
   <tr>
   <th>

Bit No.

.. raw:: html

   </th>    <th>

Parameter Name

.. raw:: html

   </th><th> 

Bit Combination

.. raw:: html

   </th><th>

Explanation

.. raw:: html

   </th>
   <tr>
   <td>

0-1

.. raw:: html

   </td><td>

LandSea

.. raw:: html

   </td><td>   

00

.. raw:: html

   </td><td> 

Land

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

01

.. raw:: html

   </td><td>

Shore

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

10

.. raw:: html

   </td><td>

Freshwater

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

11

.. raw:: html

   </td><td>

Ocean

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

2

.. raw:: html

   </td><td>

Snow/Ice

.. raw:: html

   </td><td>  

0

.. raw:: html

   </td><td>

No snow/ice detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Snow/ice detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

3

.. raw:: html

   </td><td>

Aerosol

.. raw:: html

   </td><td>   

0

.. raw:: html

   </td><td>

No or low atmospheric aerosol levels detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Average or high atmospheric aerosol levels detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

4

.. raw:: html

   </td><td>

Cirrus

.. raw:: html

   </td><td>    

0

.. raw:: html

   </td><td>

No cirrus detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Cirrus detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

5

.. raw:: html

   </td><td>

Cloud

.. raw:: html

   </td><td> 

0

.. raw:: html

   </td><td>

No cloud detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Cloud detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

6

.. raw:: html

   </td><td>

Cloud shadow

.. raw:: html

   </td><td>  

0

.. raw:: html

   </td><td>

No cloud shadow detected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Cloud shadowdetected

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

7

.. raw:: html

   </td><td>

Biome\_mask

.. raw:: html

   </td><td>    

0

.. raw:: html

   </td><td>

Biome outside interval 1-4

.. raw:: html

   </td>
   </tr>
   <tr>
   <td>

 

.. raw:: html

   </td><td>

 

.. raw:: html

   </td><td>  

1

.. raw:: html

   </td><td>

Biome in interval 1-4

.. raw:: html

   </td>
   </tr>
   </table>

Use this QC dataset to make sure that **only** Land pixels are passed in
the mask, and apply other data quality measures as appropriate.

*Hint* this is much the same as the exercise above, but looking at a
different QC dataset. The key to doing this is to identify the bit codes
for combinations that you want to set or unset.

You can find an example of how to do this **here**\ [**DEADLINK**\ ].
This filtering shouldn’t make much difference in this case, as the tile
is mostly land pixels. However, consider tile h17v03 (part of the UK)
for the month of June (e.g.
``MCD15A2.A2011185.h17v03.005.2011213154608.hdf``)

**TODO** as NASA website is down!!!!!

.. figure:: https://raw.github.com/jgomezdans/geogg122-1/master/uk_lai.png
   :alt: UK LAI map

   UK LAI map

.. code:: python

    !pwd

.. parsed-literal::

    shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory
    pwd: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory
    pwd: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory


.. code:: python

    def css_styling():
        from IPython.display import display, HTML
        styles = "https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/raw/master/styles/custom.css"
        return HTML(styles)
    css_styling()



.. raw:: html

    <style>
        @font-face {
            font-family: "Computer Modern";
            src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunss.otf');
        }
        div.cell{
            width:800px;
            margin-left:16% !important;
            margin-right:auto;
        }
        h1 {
            font-family: Helvetica, serif;
        }
        h4{
            margin-top:12px;
            margin-bottom: 3px;
           }
        div.text_cell_render{
            font-family: Computer Modern, "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
            line-height: 145%;
            font-size: 130%;
            width:800px;
            margin-left:auto;
            margin-right:auto;
        }
        .CodeMirror{
                font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
        }
        .prompt{
            display: None;
        }
        .text_cell_render h5 {
            font-weight: 300;
            font-size: 22pt;
            color: #4057A1;
            font-style: italic;
            margin-bottom: .5em;
            margin-top: 0.5em;
            display: block;
        }
        
        .warning{
            color: rgb( 240, 20, 20 )
            }  
    </style>
    <script>
        MathJax.Hub.Config({
                            TeX: {
                               extensions: ["AMSmath.js"]
                               },
                    tex2jax: {
                        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                        displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                    },
                    displayAlign: 'center', // Change this to 'center' to center equations.
                    "HTML-CSS": {
                        styles: {'.MathJax_Display': {"margin": 4}}
                    }
            });
    </script>



