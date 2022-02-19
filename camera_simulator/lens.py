"""Lens of a camera simulator

Iterator class that simulates the lens of a camera given the dimension height and width of the lens.

    Typical usage example:

    lens1 = Lens(height,width)
    processed_img = sensor1.process(image)
"""

from base_processor import Base_processor

class Lens(Base_processor):
    """The lens of a camera simulator

    Attributes:
        _height: An integer indicating the height of the lens.
        _width: An integer indicating the width of the lens.
    """

    def __init__(self,_height,_width):
        """Inits Lens with the _height and the _width."""
        if type(_height) is not int or type(_width) is not int:
            raise TypeError("The height and the width must be Integers")
        self._height = _height
        self._width = _width

    # Height Property
    @property
    def height(self):
        """Getter of the height property"""
        return self._height

    @height.setter 
    def height(self, _height):
        """Setter of the height property"""
        if type(_height) is not int:
            raise TypeError("The height must be an Integer")
        self._height = _height
    
    # Width Property
    @property
    def width(self):
        """Getter of the width property"""
        return self._width

    @width.setter 
    def width(self, _width):
        """Setter of the width property"""
        if type(_width) is not int:
            raise TypeError("The width must be an Integer")
        self._width = _width

    def process(self, image):
        """Compares lens dimensions and an image dimensions.
        
        Process method that compares the dimensions of an image with the Lens height and width.
        
        Args:
            image: A 2D numpy data of the image.

        Returns: 
            The 2D numpy data of the image.

        Raises:
            ValueError: The size of the image is different to the lens height and width.
        """
        size = image.shape
        if self.height != size[0] or self.width != size[1]:
            raise ValueError("The size of the image is different to the lens height and width.")
        return image

    def decorator(f):
        def simultaneous(*args,**kargs):
            Lens.process(*args,**kargs)
            return f(*args,**kargs)
        return simultaneous
