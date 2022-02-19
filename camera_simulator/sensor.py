"""Sensor of a camera simulator

Iterator class that simulates the sensor of a camera given a sensor gain, 
an image and the size of the iterator.

    Typical usage example:

    sensor1 = Sensor(gain,image,10)
    processed_img = sensor1.process(image)
"""

from base_processor import Base_processor
import numpy as np
from lens import Lens

class Sensor(Base_processor):
    """The sensor of a camera simulator

    Attributes:
        _gain: An integer indicating the gain of the sensor.
        image:
        _max:
    """
    
    def __init__(self,_gain, image, lens, _max = 10):
        """Inits Sensor with the _gain, image and maximum iterator"""
        if type(_gain) is not int or type(_max) is not int:
            raise TypeError("The gain and the maximum iterator must be Integers")
        if type(image) is not np.ndarray:
            raise TypeError("The image must be a numpy array")
        if type(lens) is not Lens:
            raise TypeError("The lens must be a Lens object")
        self._gain = _gain
        self.image = image
        self.height = lens.height
        self.width = lens.width
        self._max = _max
        

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self._max:
            result = self.i + self.image
            self.i += 1
            return result
        else:
            raise StopIteration

    # Gain Property
    @property
    def gain(self):
        """Getter of the gain property"""
        return self._gain
    
    @gain.setter
    def gain(self,_gain):
        """Setter of the gain property"""
        if type(_gain) is not int:
            raise TypeError("The gain must be an Integer")
        self._gain = _gain
    
    @Lens.decorator
    def process(self,image):
        """Multiplies the gain of the sensor with a given image.
        
        Args:
            image: A 2D numpy data of the image.

        Returns: 
            The 2D numpy data of the image multiplied by the gain of the sensor.
        """
        return self._gain * image

def mymean():
    im_height = 5
    im_width = 5
    gain = np.random.randint(10)
    lens = Lens(im_height,im_width)
    image = np.random.randint(10,size=(im_height,im_width))
    sensors = [i for i in Sensor(gain,image,lens)]
    result = np.mean(sensors,axis=0)
    return result
