# Camera Simulator
Basic simulation of a lens and a sensor of a camera. 

## Base Work
The library has a principal folder called camera_simulator with the classes base_processor, lens and sensor. Each class is on its own file in order to be clear of each part of the camera simulator. 
The base processor has the property enable that is initialized as True and the library abc is used to create the abstract method that will later be used in the sensor and lens classes. 
The lens class is initialized with the values height and width properties given. If the height or width values are not integers it raises a TypeError. The process method raises a value error if the dimensions of the image and the lens are different, otherwise returns the image. 
The sensor class is initialized with the gain property given (other values are added later in the advance python section). The processor multiplies the value of the image by the gain of the lens. 
All files, classes and methods doctrings are made following the Google standard format and formated using black code formatter. 

## Specific skills

### Documentation
All the documentation and html documentaton are made. 
The notebook Tutorial.ipynb has the tutorial to use the camera_simulator package. 

### Packaging
A __init__.py, a README.md and a setup.py files are added and a test folder in order to complete the minimum needs of the package. 
The setup.py file has the basic information to create the python wheels and the dependencies needed for it to work. 

### Testing 
All the tests for the files sensor.py and lens.py are in the tests folder.
It is test:
 - The creation of the objects and the possible raised errors.
 - The setters and getters with the possible reaised errors
 - The process methods and the possible errors.
 - The decorator from the Lens class in the Sensor process method.
 - The mymean function using a seed given that the gain and the image (data and dimensions) are made randomly. 

## Advanced Python

### Decorator
The method decorator is created to call the method process in Lens before a given function f. The idea of this method is to call the lens process before the sensor process, however, when the lens process is called in the sensor class it needs the lens height and width. To solve this I initiate the sensor with a lens object also I create a update lens in case the value of the height or width is change in the lens.

### Sensor Iterator
To do this I add the methods __iter__ and __next__ in the Sensor class. In the next method the returned image is the original plus the index of the iteration. 

### mymean function
The mymean funcion is in the sensor file at the end. The image height, width and data are random, as well as the sensor gain. Then, the sensor is iterated, and as each iteration there is a new matrix, they are saved in a list. Then, I used the numpy mean function to find the mean of the matrixes. 
In the setup.py file an entry point is added to use the command pysensor to call the mymean function in sensor file.  

### Concurrent package

