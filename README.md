![](https://raw.github.com/profLewis/geogg122/master/images/ucl_logo.png)

# Welcome to GeogG122: Scientific Computing

## Course information

### Course Convenor

[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)

### Course and Contributing Staff
[Prof Philip Lewis] (http://www.geog.ucl.ac.uk/~plewis)  
[Dr. Jose Gomez-Dans](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/jose-gomez-dans/)

### Purpose of this course

This course, GeogG122 Scientific Computing, is a term 1 MSc module worth 15 credits (25% of the term 1 credits) that aims to:

* impart an understanding of scientific computing
* give students a grounding in the basic principles of algorithm development and program construction
* to introduce principles of computer-based image analysis and model development

It is open to students from a number of MSc courses run by the Department of Geography UCL, but the material should be of wider value to others wishing to make use of scientific computing. 

The module will cover:

* Introduction to linux environment 
* Computing in Python
* Computing for image analysis
* Computing for environmental modelling
* Data visualisation for scientific applications

### Learning Outcomes

At the end of the module, students should:

* have a working knowledge of linux / unix operating systems and have the knowledge and confidence to obtain, compile and install commonly available scientific software packages
* have an understanding of algorithm development and be able to use widely used scientific computing software to manipulate datasets and accomplish analytical tasks
* have an understanding of the technical issues specific to image-based analysis, model implementation and scientific visualisation

### Timetable

The course takes place over 10 weeks in term 1, on Wednesdays usually from 10:00 to 13:00 (09:00-13:00 in the first two sessions) in the Geography Department Unix Computing Lab (PB110) in the [Pearson Building](http://www.ucl.ac.uk/estates/roombooking/building-location/?id=003), UCL. Classes take place from the second week of term to the final week of term, other than Reading week. See UCL [term dates](http://www.ucl.ac.uk/staff/term-dates) for further information.

### Assessment

Assessment is through one piece of coursework that is submitted in both paper form and electronically via Moodle. See the [Moodle page](https://moodle.ucl.ac.uk/course/view.php?id=13891) for more details.

### Useful links

[Course Moodle page] (http://moodle.ucl.ac.uk/course/view.php?id=13891)  

[A useful reading list for basic and advanced Unix.] (http://www.ee.surrey.ac.uk/Teaching/Unix/books-uk.html)  

### Structure of the Course

    #1 1 Oct 09:00-13:00 4 hrs Introduction to Unix 110 
    #2 8 Oct 09:00-13:00 4 hrs Python 101 110 
    #3 15 Oct 10:00-13:00 4 hrs Plotting and Numerical Python 110 
    #4 22 Oct 10:00-13:00 3 hrs Raster and vector data 110 
    #5 29 Oct 10:00-13:00 3 hrs Raster and vector data 110 
    #5a READING WEEK (ENVI)
    #6 12 Nov 10:00-13:00 3 hrs Raster and vector data 110 
    #7 19 Nov 10:00-13:00 3 hrs Building and calibrating a model 110 
    #8 26 Nov 10:00-13:00 3 hrs Building and calibrating a model 110 
    #9 3 Dec 10:00-13:00 3 hrs Group practical 110 
    #10 10 Dec 10:00-13:00 3 hrs Group practical 110 



-  0.0 Introduction  
In this session, we will outline the purpose and structure of the course.

  [Introductory notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter0_Introduction/f1_index.ipynb)  


-  1.0 Unix  
  [Unix Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter1_Unix/f3_1_unix_intro.ipynb)  
  [Unix exercises](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter1_Unix/f3_1a_unix_intro_answers.ipynb)  

-  2.0 Python 101  
 The aim of this Chapter is to introduce you to some of the fundamental concepts in Python. Mainly, this is based around fundamental data types in Python (`int`, `float`, `str`, `bool` etc.) and ways to group them (`tuple`, `list` and `dict`).  We then learn about how to loop over groups of things, which gives us control to iterate some process. We need to spend a little time on strings, as you will likely to quite a bit of string processing in Scientific Computing (e.g. reading/writing data to/from ASCII text files). Although some of the examples we use are very simple to explain a concept, the more developed ones should be directly applicable to the sort of programming you are likely to need to do. A set of exercises is developed throughout the chapter, with worked answers available to you once you have had a go yourself. In addition, a more advanced section of the chapter is available, that goes into some more detail and complkications. This too has a set of exercises with worked examples.  

  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter2_Python_intro/python101.ipynb)  
  [Answers](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter2_Python_intro/main_answers.ipynb)  
  [Advanced](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter2_Python_intro/advanced.ipynb)  
  [Advanced Answers](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter2_Python_intro/advanced_answers.ipynb)  
 
- 3.0 Plotting and Numerical Python
      
  In this session, we will introduce and use some packages that you will commonly use in scientific programming.
      
  These are: 
      
  [numpy](http://www.numpy.org/): NumPy is the fundamental package for scientific computing with Python   
  [matplotlib](http://matplotlib.org/): Python 2D plotting library   
    
  We will also introduce some additional programming concepts, and set an exercise that you can do and get feedback on.   
      
  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter3_Scientific_Numerical_Python/Scientific_Numerical_Python.ipynb)  
  [Answers](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter3_Scientific_Numerical_Python/answers.ipynb)  
  [Advanced](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter3_Scientific_Numerical_Python/advanced.ipynb)  

      
- 4.0 Geospatial data

  In this session, we will introduced the gdal geospatial module which can read a wide range of scientific data formats. You will find that using it to read data is quite similar to the work we did last week on netCDF datasets.

  The main challenges are also much the same: very often, you need to be able to read data from a 'stack' of image files and generate a useful 3D (space and time) dataset from these. Once you have the data in such a form, there are many things we can do with it, and very many of these are convenient to do using array-based expressions such as in numpy (consider the simplicity of the expression absorbed = rad * (1 - albedo) from last week's exercise).

  That said, it can sometimes be quite an effort to prepare datasets in this form. Last week, we developed a 'valid data' mask from the GlobAlbedo dataset, as invalid data were stored as nan. Very often though, scientific datasets have more complex 'Quality Control' (QC) information, that gives per-pixel information describing the quality of the product at that location (e.g. it was very cloudy so the results are not so good).

  To explore this, we will first consider the MODIS Leaf Area Index (LAI) product taht is mapped at 1 km resolution, every 8 days from the year 2000.

  We will learn how to read in these data (in hdf format) using gdal, and how to interpret the QC information in such products to produce valid data masks. As an exercise, you will wrap some code around that to form a 3D masked array of the dataset.

  Next, we will consider how to download such data. This should be a reinforcement of material from last week, but it is useful to know how to conveniently access NASA data products. A challenge in the exercise then is to download a different dataset (MODIS snow cover) for the UK, and form a masked 3D dataset from this.

  Finally, we will introduce vector datasets and show you python tools that allow you (among many other things) to build a mask in the projection and sampling of your spatial dataset (MODIS LAI in this case).

  There are many features and as many complexities to the Python tools we will deal with today, but in this material, we cover some very typical tasks you will want to do. They all revolve around generating masked 3D datasets from NASA MODIS datasets, which is a very useful form of global biophysical information over the last decade+. We also provide much material for further reading and use when you are more confident in your programming.

  A final point here is that the material we cover today is very closely related to what you will need to do in the first section of your assessed practical that we will introduce next week, so you really need to get to grips with this now.

  There is not as much 'new' material as in previous weeks now, but we assume that you have understood, and can make use of, material from those lectures.
    
  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter4_GDAL/GDAL_HDF.ipynb)  
  [Answers](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter4_GDAL/answers.ipynb)  
  [Advanced](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter4_GDAL/advanced.ipynb)  


- 5.0 Function fitting and Interpolation

  In today's session, we will be using some of the LAI datasets we examined last week (masked by national boundaries) and doing some analysis on them.

  First, we will examine how to improve our data reading function by extracting only the area we are interested in. This involves querying the 'country' mask to find its limits and passing this information through to the reader.
    Then we will look at methods to interpolate and smooth over gaps in datasets using various methods.
    Finally, we will look at fitting models to datasets, in this case a model describing LAI phenology.
    
  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter5_Interpolation/Interpolation.ipynb)  
  
- 6.0 ENVI

  In today's practical, you will gain experience of using the ENVI software package.

  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter6_ENVI/envi.ipynb)
  

- 6.A Coursework

  These notes explain about the coursework to be submitted.

  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter6_Practical/Practical.ipynb)
  

- 7.0 ENSO

  Using monthly fire count data from MODIS Terra, develop and test a predictive model for the number of fires per unit area per year driven by Sea Surface Temperature anomaly data.
  
  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter7_ENSO/ENSO.ipynb)
  
- 8.0 P Theory

  Using hyperspectral image data over an agricultural area, use photon recollision theory to produce a map of Leaf Area Index.
    
  [Course Notes](http://nbviewer.ipython.org/urls/raw.github.com/profLewis/geogg122/master/Chapter8_ptheory/Ptheory.ipynb)
