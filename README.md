# JPK_AFM_Analysis
Module to analysis AFM data from a JPK Nanowizard 4 (mainly QI) 

Christian T. Kreis, Ruby May A. Sullan -- Department of Physical and Environmental Sciences, University of Toronto Scarborough, 1065 Military Trail, Toronto, ON M1C 1A4, Canada

Special thanks to all the members of the Sullan lab for your input on useful functionalities to add, as well as testing the functions with your data


0. At the moment there is no proper documentation available. That might change, but I would not be too optimistic.

1. The module was designed to read raw QI data files (.jpk-qi-data) from a JPK Nanowizard AFM (Software: v6.1.121). For other AFM suppliers the data import functions need to be modified, other JPK software versions should be mostly compatible.

2. All the necessary modules to run the codes are included within the WinPython or anaconda Python distribution. For reference, I used WinPython 3.6.7.0

3. The module was designed on a Windows machine. There might be some issues when using Mac, Linux, or others. I tried to make sure that things are designed sucht that they are independent of the OS (e.g. path structures), but I am sure I overlooked some things.

4. The parameters in the functions are optimized for our imaging settings and biofilm system -- adapting might be necessary.

5. Not all functions, options of functions, and output parameters were tested thoroughly. There might be some bugs, issues, and errors in the code. Test the results against other analysis software (and always question whether the results make sense).

6. There is a grapical user interface included. At the moment, not all functions are implemented in the GUI. Use a high resolution screen, as the GUI has a minimal size around 1600X700 pixel.

7. To speed analysis up, multithreading and multiprocessing can be implemented for the QI data analysis. I did some tests on that matter, but there are some compatibility issues with the corresponding modules and Spyder and matplotlib.

8. Most of the biofilm QI maps had dimensions of 64x64 pixels. For such a map the three-layer algorithm takes a few minutes to process on a standard desktop computer (i5-8400 @2.80 Ghz, 16GB Ram). Other functions, such as topography, are much faster. For larger maps, processing times will be significantly longer. I am sure that can be improved by implementing multiprocessing, etc.





