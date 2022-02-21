"""
Unit tests for the lens methods
"""
import pytest
import numpy as np
from lens import Lens


def test_creation():
    """Test if Lens is created with the correct values."""
    height, width = 5, 10
    Lens(height, width)


@pytest.mark.parametrize(
    "height,width,expected_error_message",
    [
        (2.3, 10, "The height and the width must be Integers"),
        (2, 10.5, "The height and the width must be Integers"),
        (2.3, 10.5, "The height and the width must be Integers"),
        ("2", 10, "The height and the width must be Integers"),
        (2, "10", "The height and the width must be Integers"),
        ("2", "10", "The height and the width must be Integers"),
    ],
)
def test_creation_invalid(height, width, expected_error_message):
    """Test if Lens properly handles invalid creation values."""
    with pytest.raises(TypeError, match=expected_error_message):
        Lens(height, width)


def test_dimensions_getter():
    """Test if the dimensions getters work properly."""
    height, width = 3, 4
    lens1 = Lens(height, width)
    assert height == lens1.height
    assert width == lens1.width


def test_dimensions_setter():
    """Test if the dimensions setters work properly."""
    old_height, old_width = 3, 4
    new_height, new_width = 1, 2
    lens1 = Lens(old_height, old_width)
    lens1.height = new_height
    lens1.width = new_width
    assert lens1.height == new_height
    assert lens1.width == new_width


@pytest.mark.parametrize(
    "new_height,new_width,expected_error_message",
    [
        (2.1, 3, "The height must be an Integer"),
        (2, 3.1, "The width must be an Integer"),
        ("2", 3, "The height must be an Integer"),
        (2, "3", "The width must be an Integer"),
    ],
)
def test_dimensions_setter_invalid(new_height, new_width, expected_error_message):
    """Test if the dimensions setters handle invalid dimension values."""
    old_height, old_width = 3, 4
    lens1 = Lens(old_height, old_width)
    with pytest.raises(TypeError, match=expected_error_message):
        lens1.height = new_height
        lens1.width = new_width


def test_process():
    """Test if process works properly"""
    im_height = 10
    im_width = 10
    image = np.random.randint(10, size=(im_height, im_width))
    lens1 = Lens(im_height, im_width)
    assert (lens1.process(image) == image).all()


@pytest.mark.parametrize(
    "height,width,expected_error_message",
    [
        (10, 5, "The size of the image is different to the lens height and width."),
        (5, 10, "The size of the image is different to the lens height and width."),
        (5, 5, "The size of the image is different to the lens height and width."),
    ],
)
def test_process_invalid(height, width, expected_error_message):
    """Test if process handles properly invalid dimension values."""
    im_height = 10
    im_width = 10
    image = np.random.randint(10, size=(im_height, im_width))
    lens1 = Lens(height, width)
    with pytest.raises(ValueError, match=expected_error_message):
        lens1.process(image)
