"""Sensor of a camera simulator

Iterator class that simulates the sensor of a camera given a sensor gain, 
an image, a lens and the size of the iterator.

    Typical usage example:

    sensor1 = Sensor(gain,image,lens,10)
    processed_img = sensor1.process(image)
    for i in sensor1:
        print(i)
"""

from base_processor import Base_processor
import numpy as np
from lens import Lens
from abc import ABCMeta
from concurrent import futures


class Sensor(Base_processor):
    """The sensor of a camera simulator that can be used as an iterator.

    Attributes:
        _gain: An integer indicating the gain of the sensor.
        image: 2D numpy data of the image.
        lens: Object of type Lens.
        _max: An integer of the maximum value of the iterator.

    Raises:
        The gain and the maximum iterator must be Integers
        The image must be a numpy array
        The lens must be a Lens object
    """

    def __init__(self, _gain, image, lens, _max=10):
        """Inits Sensor with the _gain, image, lens height and width, and the value of the maximum iterator"""
        if not isinstance(_gain, int) or not isinstance(_max, int):
            raise TypeError("The gain and the maximum iterator must be Integers")
        if not isinstance(image, np.ndarray):
            raise TypeError("The image must be a numpy array")
        if (
            not hasattr(lens, "height")
            and not hasattr(lens, "width")
            and not isinstance(type(lens), ABCMeta)
        ):
            raise TypeError("The lens must be a Lens object")
        self._gain = _gain
        self.image = image
        self.height = lens.height
        self.width = lens.width
        self._max = _max

    # Iterator
    def __iter__(self):
        """Makes the class an iterator"""
        self.i = 0
        return self

    def __next__(self):
        """Returns the next item of the sequence and adds the current index of iteration plus the image."""
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
    def gain(self, _gain):
        """Setter of the gain property
        Args:
            _gain: An integer indicating the new gain of the sensor.

        Returns:
            The new gain value of the sensor.

        Raises:
            TypeError: The gain must be an Integer."""

        if not isinstance(_gain, int):
            raise TypeError("The gain must be an Integer")
        self._gain = _gain

    def lens_update(self, lens):
        """Updates the value of the height and the width in case it was changed."""
        self.height = lens.height
        self.width = lens.width

    @Lens.decorator
    def process(self, image):
        """Multiplies the gain of the sensor with a given image.

        Args:
            image: A 2D numpy data of the image.

        Returns:
            The 2D numpy data of the image multiplied by the gain of the sensor.
        """
        return self._gain * image


def mymean(im_height=None, im_width=None, seed=None):
    """The mean of an image through a Sensor object.

    Args:
            seed: The random seed if it is needed.
            im_heiht: An integer indicating the image height.
            im_width: An integer indicating the image height.
    """
    # Random image and gain
    if seed is not None:
        np.random.seed(seed)
    if im_height is None:
        im_height = np.random.randint(5, 10)
    if im_width is None:
        im_width = np.random.randint(5, 10)
    gain = np.random.randint(10)
    lens = Lens(im_height, im_width)
    image = np.random.randint(10, size=(im_height, im_width))

    sensors = [i for i in Sensor(gain, image, lens)]

    result = np.mean(sensors, axis=0)
    return result


def concurrent():
    """Uses the concurrent package with max 5 workers to call mymean function 100 times, with a 10x10 image."""
    with futures.ProcessPoolExecutor(max_workers=5) as pool:
        fs = [pool.submit(mymean, 10, 10) for i in range(100)]
        for f in futures.as_completed(fs):
            try:
                matrixes = f.result()
            except ValueError:
                continue
            print(matrixes)


if __name__ == "__main__":
    concurrent()
