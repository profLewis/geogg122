
Welcome to GeogG122: Scientific Computing
=========================================

Course information
------------------

Course Convenor
~~~~~~~~~~~~~~~

`Prof P. Lewis <http://www.geog.ucl.ac.uk/~plewis>`__

Course Staff
~~~~~~~~~~~~

`Prof P. Lewis <http://www.geog.ucl.ac.uk/~plewis>`__ `Dr. J.
Gomez-Dans <http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/jose-gomez-dans>`__

Purpose of this course
----------------------

This course, GeogG122 Scientific Computing, is a term 1 MSc module worth
15 credits (25% of the term 1 credits) that aims to:

-  impart an understanding of scientific computing
-  give students a grounding in the basic principles of algorithm
   development and program construction
-  to introduce principles of computer-based image analysis and model
   development

It is open to students from a number of `MSc
courses <http://www.geog.ucl.ac.uk/admissions-and-teaching/postgraduates>`__
run by the `Department of Geography <http://www.geog.ucl.ac.uk>`__
`UCL <www.ucl.ac.uk>`__, but the material should be of wider value to
others wishing to make use of scientific computing.

The module will cover:

-  Introduction to programming
-  Computing for image analysis
-  Computing in Python
-  Computing for environmental modelling
-  Data visualisation for scientific applications

Learning Outcomes
-----------------

At the end of the module, students should:

-  have an understanding of algorithm development and be able to use
   widely used scientific computing software to manipulate datasets and
   accomplish analytical tasks
-  have an understanding of the technical issues specific to image-based
   analysis, model implementation and scientific visualisation

Additional Outcomes
-------------------

If you follow the various 'advanced' sections of the course, you will
gain a deeper understanding of the concepts and codes, and in addition:

• have a working knowledge of linux / unix operating systems and have
the knowledge and confidence to obtain, compile and install commonly
available scientific software packages

Timetable
---------

The course takes place over 10 weeks in term 1, on Wednesdays usually
from 10:00 to 13:00 (09:00-13:00 in the first two sessions) in the
Geography Department Unix Computing Lab (PB110) in the `Pearson
Building,
UCL <http://www.ucl.ac.uk/efd/roombooking/building-location/?id=003>`__.

Classes take place from the second week of term to the final week of
term, other than Reading week. See `UCL term dates for further
information <http://www.ucl.ac.uk/staff/term-dates>`__.

Structure of the Course
-----------------------

::

    #1  1  Oct 09:00-13:00 4 hrs Python 101
    #2  8  Oct 09:00-13:00 4 hrs Plotting and Numerical Python
    #3  15 Oct 10:00-13:00 4 hrs Geospatial Data
    #4  22 Oct 10:00-13:00 3 hrs Interpolation
    #5  29 Oct 10:00-13:00 3 hrs Practical
    #5a READING WEEK (ENVI)
    #6  12 Nov 10:00-13:00 3 hrs TBD 
    #7  19 Nov 10:00-13:00 3 hrs TBD
    #8  26 Nov 10:00-13:00 3 hrs TBD 
    #9  3  Dec 10:00-13:00 3 hrs Group practical 
    #10 10 Dec 10:00-13:00 3 hrs Group practical

Total scheduled hours: 32 hours

Prof Philip Lewis

Rooms: Pearson Building Unix Lab, Room 110, 1st floor

In addition to the 10:300 session, I will be available 09:00-10:00 for
help and questions (other than the first few weeks when we start at
09:00 anyway).

Assessment
----------

Assessment is through one piece of coursework that is submitted in both
paper form and electronically via Moodle. See the `Moodle
page <http://moodle.ucl.ac.uk/course/view.php?id=13891>`__ for more
details.

Information on the assessment is directly available `in a later section
of the
notes <..//Chapter6a_Practical/Practical.html>`__.

Useful links
------------

`Course Moodle
page <http://moodle.ucl.ac.uk/course/view.php?id=13891>`__

`A useful reading list for basic and advanced
Unix. <http://www.ee.surrey.ac.uk/Teaching/Unix/books-uk.html>`__

Detailed Struucture of the Course
---------------------------------

**0.0 Introduction**

A brief overview of the course (these notes):

`[Introductory
notes] <../Chapter0_Introduction/f1_index.html>`__

An introduction to some of the basics of the Unix operating system. The
aim is to enable students to understand the directory structure and
basic unix operations (e.g. copying and moving files) as well simple
operations such as text editing.

**Students should read and follow these notes in their own time**\ \* as
we will not be going through them in class (unless requested).

`[Unix
notes] <../Chapter1_Unix/f3_1_unix_intro.html>`__
`[Unix
exercises] <../Chapter1_Unix/f3_1a_unix_intro_answers.html>`__

**1.0 Python 101**

The aim of this section is to introduce you to some of the fundamental
concepts in Python. Mainly, this is based around fundamental data types
in Python (``int``, ``float``, ``str``, ``bool`` etc.) and ways to group
them (``tuple``, ``list`` and ``dict``). We then learn about how to loop
over groups of things, which gives us control to iterate some process.
We need to spend a little time on strings, as you will likely to quite a
bit of string processing in Scientific Computing (e.g. reading/writing
data to/from ASCII text files). Although some of the examples we use are
very simple to explain a concept, the more developed ones should be
directly applicable to the sort of programming you are likely to need to
do. A set of exercises is developed throughout the chapter, with worked
answers available to you once you have had a go yourself. In addition, a
more advanced section of the chapter is available, that goes into some
more detail and complications. This too has a set of exercises with
worked examples.

`[Course
Notes] <../Chapter2_Python_intro/python101.html>`__
`[Answers] <../Chapter2_Python_intro/main_answers.html>`__
`[Advanced] <../Chapter2_Python_intro/advanced.html>`__
`[Advanced
Answers] <../Chapter2_Python_intro/advanced_answers.html>`__

**2.0 Plotting and Numerical Python**

In this session, we will introduce and use some packages that you will
commonly use in scientific programming.

These are:

`numpy <http://www.numpy.org/>`__: NumPy is the fundamental package for
scientific computing with Python

`matplotlib <http://matplotlib.org/>`__: Python 2D plotting library

We will also introduce some additional programming concepts, and set an
exercise that you can do and get feedback on.

`[Course
Notes] <../Chapter3_Scientific_Numerical_Python/Scientific_Numerical_Python.html>`__
`[Answers] <../Chapter3_Scientific_Numerical_Python/answers.html>`__
`[Advanced] <../Chapter3_Scientific_Numerical_Python/advanced.html>`__

**3.0 Geospatial Data**

In this session, we will introduced the gdal geospatial module which can
read a wide range of scientific data formats. You will find that using
it to read data is quite similar to the work we did last week on netCDF
datasets.

The main challenges are also much the same: very often, you need to be
able to read data from a 'stack' of image files and generate a useful 3D
(space and time) dataset from these. Once you have the data in such a
form, there are many things we can do with it, and very many of these
are convenient to do using array-based expressions such as in numpy
(consider the simplicity of the expression absorbed = rad \* (1 -
albedo) from last week's exercise).

That said, it can sometimes be quite an effort to prepare datasets in
this form. Last week, we developed a 'valid data' mask from the
GlobAlbedo dataset, as invalid data were stored as nan. Very often
though, scientific datasets have more complex 'Quality Control' (QC)
information, that gives per-pixel information describing the quality of
the product at that location (e.g. it was very cloudy so the results are
not so good).

To explore this, we will first consider the MODIS Leaf Area Index (LAI)
product taht is mapped at 1 km resolution, every 8 days from the year
2000.

We will learn how to read in these data (in hdf format) using gdal, and
how to interpret the QC information in such products to produce valid
data masks. As an exercise, you will wrap some code around that to form
a 3D masked array of the dataset.

Next, we will consider how to download such data. This should be a
reinforcement of material from last week, but it is useful to know how
to conveniently access NASA data products. A challenge in the exercise
then is to download a different dataset (MODIS snow cover) for the UK,
and form a masked 3D dataset from this.

Finally, we will introduce vector datasets and show you python tools
that allow you (among many other things) to build a mask in the
projection and sampling of your spatial dataset (MODIS LAI in this
case).

There are many features and as many complexities to the Python tools we
will deal with today, but in this material, we cover some very typical
tasks you will want to do. They all revolve around generating masked 3D
datasets from NASA MODIS datasets, which is a very useful form of global
biophysical information over the last decade+. We also provide much
material for further reading and use when you are more confident in your
programming.

A final point here is that the material we cover today is very closely
related to what you will need to do in the first section of your
assessed practical that we will introduce next week, so you really need
to get to grips with this now.

There is not as much 'new' material as in previous weeks now, but we
assume that you have understood, and can make use of, material from
those lectures.

`[Course
Notes] <../Chapter4_GDAL/GDAL_HDF.html>`__
`[Answers] <../Chapter4_GDAL/answers.html>`__
`[Advanced] <../Chapter4_GDAL/advanced.html>`__

**4.0 Interpolation**

In today's session, we will be using some of the LAI datasets we
examined last week (masked by national boundaries) and doing some
analysis on them. First, we will examine how to improve our data reading
function by extracting only the area we are interested in. This involves
querying the 'country' mask to find its limits and passing this
information through to the reader. Then we will look at methods to
interpolate and smooth over gaps in datasets using various methods.
Finally, we will look at fitting models to datasets, in this case a
model describing LAI phenology.

`[Course
Notes] <../Chapter5_Interpolation/Interpolation.html>`__

**4a ENVI**

This session is rather apart from the rest and is included to allow
students to familarise themselves with a package image processing
environment (ENVI). This is an *unsupervised* session, that takes place
during UCL Reading Week in Term 1.

`[Course
Notes] <..//Chapter6_ENVI/envi.html>`__

**5.0 Practical**

This section describes the coursework you are to submit for assessment
for this course.

`[Practical for
assessment] <..//Chapter6a_Practical/Practical.html>`__

**6.0 ENSO**

To finish the course, some practical applications. The first of these
looks at predicting fire activity from from climatic data.

Using monthly fire count data from MODIS Terra, develop and test a
predictive model for the number of fires per unit area per year driven
by Sea Surface Temperature anomaly data.

`[Course
Notes] <../Chapter7_ENSO/ENSO.html>`__

**7.0 P Theory**

Another practical application involves a simple radiative transfer model
applied to help interpret hyperspectral remote sensing data over an
agricultural site.

Using hyperspectral image data over an agricultural area, use photon
recollision theory to produce a map of Leaf Area Index.

`[Course
Notes] <../Chapter8_ptheory/Ptheory.html>`__

Using these notes
-----------------

There are several ways you can access this course material.

These notes are created in `ipython
notebooks <http://ipython.org/ipython-doc/dev/interactive/notebook.html>`__.

The course is all stored online in
`github <https://github.com/profLewis/geogg122>`__, so you can just
navigate to that site and download the files as you like.

Probably the easiest option is to access the html version of the notes
from notebook links in the README on
`github <https://github.com/profLewis/geogg122/blob/master/README.md>`__
or above on this page. You can access *notebook* links, which are
guaranteed to be up to date, or *html* links, which should be (but not
guaranteed).

Another option is to access individual notebooks online through the
`IPython Notebook Viewer <http://nbviewer.ipython.org/>`__.

For example, to view the notebook
``Chapter0_Introduction/f2_intro.html``, you use a `link to the github
file <../Chapter0_Introduction/f2_intro.html>`__.

From these viewers, you can download the notebook if you like, using the
*Download Notebook* button (top right of the page).

Provided you have a relatively up to date version of
`ipython <http://ipython.org/ipython-doc/dev/interactive/nbconvert.html#nbconvert>`__
and a few other tools such as
`pandoc <http://johnmacfarlane.net/pandoc/installing.html>`__ you can
convert your own notebooks to other formats using ``ipython``, e.g.:

``berlin% ipython nbconvert --to html f2_intro.html``

You can also convert the notebooks to other
`formats <http://ipython.org/ipython-doc/rel-1.0.0/interactive/nbconvert.html>`__
though you might need some other tools as well for this. If you have a
working copy of ``LaTeX`` on your system (e.g.
`MacTeX <http://tug.org/mactex/downloading.html>`__ on OS X), you can
convert the notebooks to pdf format:

``berlin% ipython nbconvert --to latex --post PDF f2_intro.html``

Obtaining the course material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can obtain the whole course from
`github <https://github.com/profLewis/geogg122>`__.

To download the whole course, you can:

1. **using git**

| use the command
`git <http://en.wikipedia.org/wiki/Git_%28software%29>`__, if available:
|  Create a place on the system that you want to work in (N.B., don't
type ``berlin%``: that represents the command line prompt), e.g.:

| ``berlin% mkdir -p ~/Data/msc``
|  ``berlin% cd ~/Data/msc``
|  ``berlin% git clone https://github.com/profLewis/geogg122.git``
|  ``berlin% cd ~/Data/msc/geogg122``

This will create a directory ``~/Data/msc/geogg122`` which has the
current versions of the notebooks for the course and associated files.

If the course notes change at all (e.g. are updated), you can update
your copy with:

``berlin% git pull``

To find out more about using ``git``, type ``git --help``, get `help
online <http://www.siteground.com/tutorials/git/commands.htm>`__ or
download and use a `gui tool <http://git-scm.com/downloads>`__.

If you set up an account on `github <https://github.com/edu>`__, you can
fork the `course repository <https://github.com/profLewis/geogg122>`__
to make your own version of the course notes, and add in your own
comments and examples, if that helps you learn or remember things.

.. raw:: html

   <p>

2. **using a zip file**

Download the course as a zip file:

| ``berlin% mkdir -p ~/Data/msc``
|  ``berlin% cd ~/Data/msc``
| 
``berlin% wget -O geogg122.zip https://github.com/profLewis/geogg122/archive/master.zip``
|  ``berlin% unzip geogg122.zip``
|  ``berlin% cd ~/Data/msc/geogg122-master``

You can directly use the notebooks, or you can open the ``html`` files,
e.g. opening

`file:///home/plewis/Data/geogg122/Chapter1\_Unix/f3\_1\_unix\_intro.html </home/plewis/Data/geogg122/Chapter1_Unix/f3_1_unix_intro.html>`__
in a browser (obviously changing the username and path as appropriate).

Using the course material
~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have copied the course material as described above (and have
changed directory to where you have put the course (e.g.
``~/Data/msc/geogg122-master`` or ``~/Data/msc/geogg122``) then ``cd``
to the chapter you want, e.g.:

``berlin% cd ~/Data/msc/geogg122/Chapter0_Introduction``

and you can start the notebooks with:

``berlin% ipython notebook``

This should launch a web browser with the address
``http://127.0.0.1:8888/`` or similar with links to the notebooks you
have available.

To load a *specific* notebook, you can type e.g.:

``berlin% ipython notebook f1_index.html``

Python
~~~~~~

For most users wanting to install a working python environment, Anaconda
appears to be far easier and overall quite nice to use:
https://store.continuum.io/cshop/anaconda/. Comes with Python notebooks,
spyder and a wealth of other things not in some other releases.

System access
~~~~~~~~~~~~~

You should be able to install python on a windows operating system and
so could run most of the class material from any windows computer that
you have. As we have noted above, you can download all of the class
notes as python notebooks or other formats (such as html).

For windows users, it's probably best if you just use
http://mobaxterm.mobatek.net/ to connect to the UCL system (you don't
need exceed, it's free, got SFTP, etc).

For linux and OS X machines, it's very straightforward as you already
have a unix system. For OS X, you can find the terminal in the
``Utilities`` folder under ``Applications``. For ``X windows`` on OS X,
you may need to `install this <http://support.apple.com/kb/HT5293>`__ if
you have a recent version of the operating system.

Another approach is to use the `UCL
WTS <http://www.ucl.ac.uk/isd/students/windows/wts/access/remote>`__
system, where you have access to some software called ``exceed`` to
allow you to log on to the system.

Using any of these (or other!) approaches, you want to be able to use
the command ``ssh`` (or similar) to log on to the gateway machine
``shankly.geog.ucl.ac.uk``:

This will normally be:

``ssh -X username@shankly.geog.ucl.ac.uk``

From there, you should log in (with ``ssh``) to another computer in the
lab (or else everyone will be on the same computer).

From OS X, you use:

``ssh -Y username@shankly.geog.ucl.ac.uk``

but then the usual ``-X`` option once you get on to shankly. An
alternative gateway, if ``shankly`` is down or busy is
``lyon.geog.ucl.ac.uk``.
