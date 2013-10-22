![](https://raw.github.com/profLewis/geogg122/master/ucl_logo.png)

# Welcome to GeogG122: Scientific Computing

## Course information

### Course Convenor

[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)

### Course and Contributing Staff
[Prof Philip Lewis] (http://www.geog.ucl.ac.uk/~plewis)  
[Dr. Qingling Wu] (http://www.geog.ucl.ac.uk/about-the-department/people/academic-staff/qingling-wu)  
[Dr. Jose Gomez-Dans](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/jose-gomez-dans/)


### Useful links

[Course Moodle page] (http://moodle.ucl.ac.uk/course/view.php?id=13891)  

[A useful reading list for basic and advanced Unix.] (http://www.ee.surrey.ac.uk/Teaching/Unix/books-uk.html)  

-  Introduction  
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
