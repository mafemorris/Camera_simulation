# Camera Simulator
Basic camera simulation with a lens and a sensor. 

## Base Work
The library has a principal folder called camera_simulator with the files base_processor, lens and sensor. Each class is on its own file to be clear with each part of the camera simulator. 
The base processor has the property enable that is initialized as True and the library abc is used to create the abstract method that will later be used in the sensor and lens classes. 
The lens class is initialized with the given values of height and width. If the height or width values are not integers it raises a TypeError. The process method raises a ValueError if the dimensions of the image and the lens are different, otherwise returns the image. 
The sensor class is initialized with the given gain property (other values are added later in the advanced python section). The processor method multiplies the value of the image by the gain of the sensor. 
All files, classes and methods docstrings are made following the Google standard format and formatted using black code formatter. 

## Specific skills

### Documentation
All the documentation and html documentation are done using sphinx. 
The notebook Tutorial.ipynb has the tutorial to use the camera_simulator package. 

### Packaging
A __init__.py, a README.md and a setup.py files are added and a test folder to complete the minimum needs of the package. 
The setup.py file has the basic information to create the python wheels and the dependencies needed to function properly. 

### Testing 
All the tests for the files sensor.py and lens.py are in the tests folder.
It tests:
 - The creation of the objects and the possible raised errors.
 - The setters and getters with the possible raised errors
 - The process methods and the possible errors.
 - The decorator from the Lens class in the Sensor process method.
 - The mymean function uses a given seed for the gain and the image, data and dimensions, that are created randomly. 

## Advanced Python

### Decorator
The method decorator is created to call the Lens' method process before a given function f. The idea of this method is to call the lens process before the sensor process, however, when the lens process is called in the sensor class it needs the lens height and width. To solve this, I initiate the sensor with a lens object. Also, there is a lens_update in case the value of the Lens height or width is changed.

### Sensor Iterator
To change the sensor class into an iterator, the methods __iter__ and __next__ are added in the Sensor class. In the __next__ method the returned image is the original plus the index of the iteration. 

### mymean function
The mymean function is in the sensor file at the end. The image height, width and data are random, as well as the sensor gain. Then, the sensor is iterated, and as each iteration there is a new matrix, they are saved in a list. Then, I used the numpy mean function to find the mean of the matrixes. 
In the setup.py file, an entry point is added to use the command pysensor to call the mymean function in the sensor file.  

### Concurrent package
As I have never used the concurrent package before, I searched for some information and saw a couple of videos about it. Then, I implement the solution as needed. For this case, I add the possibility to set a seed, image height and width in the mymean method. Thus, it is easier to see the differences between the result matrixes. 
