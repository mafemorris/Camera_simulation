# Camera Simulator
Basic simulation of a lens and a sensor of a camera. 

## Base Work
The library has a principal folder called camera_simulator with the classes base_processor, lens and sensor. Each class is on its own file in order to be clear of each part of the camera simulator. 
The base processor has the property enable that is initialized as True and I used the library abc to create the abstract method that will later be used in the sensor and lens classes. 
The lens class is initialized with the properties height and width given. The processor raises a value error if the dimensions of the image and the lens are different, otherwise returns the image. 
The sensor class is initialized with the property gain given. The processor multiplies the value of the image by the gain of the lens. 

## Specific skills

### Documentation

### Packaging
A __init__.py, a README.md and a setup.py files are added and a test folder in order to complete the minimum needs of the package. 
The setup.py file has the basic information to create the python wheels and the dependencies needed for it to work. 


## Advanced Python
