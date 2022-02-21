"""
Unit tests for the sensor methods
"""
import pytest
import numpy as np
from sensor import Sensor, mymean
from lens import Lens


def test_creation():
    """Test if Sensor is created with the correct values."""
    gain = 3
    im_height, im_width = 3, 3
    image = np.random.randint(10, size=(im_height, im_width))
    lens = Lens(im_height, im_width)
    _max = 5
    Sensor(gain, image, lens, _max)


@pytest.mark.parametrize(
    "gain,image,lens,_max,expected_error_message",
    [
        (
            3.1,
            np.random.randint(10, size=(10, 10)),
            Lens(10, 10),
            5,
            "The gain and the maximum iterator must be Integers",
        ),
        (
            3,
            np.random.randint(10, size=(10, 10)),
            Lens(10, 10),
            5.1,
            "The gain and the maximum iterator must be Integers",
        ),
        (
            3.1,
            np.random.randint(10, size=(10, 10)),
            Lens(10, 10),
            5.1,
            "The gain and the maximum iterator must be Integers",
        ),
        (3, [[1, 2, 3], [4, 5, 6]], Lens(2, 3), 5, "The image must be a numpy array"),
        (3, np.random.randint(10, size=(10, 10)), "lens", 5, "The lens must be a Lens object"),
    ],
)
def test_creation_invalid(gain, image, lens, _max, expected_error_message):
    """Test if Sensor properly handles invalid creation values."""
    with pytest.raises(TypeError, match=expected_error_message):
        Sensor(gain, image, lens, _max)


def test_gain_getter():
    """Test if the gain getter works properly."""
    gain = 3
    im_height, im_width = 3, 3
    image = np.random.randint(10, size=(im_height, im_width))
    lens = Lens(im_height, im_width)
    sensor1 = Sensor(gain, image, lens)
    assert gain == sensor1.gain


def test_gain_setter():
    """Test if the gain setter works properly."""
    old_gain = 3
    new_gain = 4
    im_height, im_width = 3, 3
    image = np.random.randint(10, size=(im_height, im_width))
    lens = Lens(im_height, im_width)
    sensor1 = Sensor(old_gain, image, lens)
    sensor1.gain = new_gain
    assert sensor1.gain == new_gain


@pytest.mark.parametrize(
    "new_gain,expected_error_message",
    [
        (2.1, "The gain must be an Integer"),
        ("2", "The gain must be an Integer"),
    ],
)
def test_gain_setter_invalid(new_gain, expected_error_message):
    """Test if the gain setter handles invalid gain values."""
    old_gain = 3
    im_height, im_width = 3, 3
    image = np.random.randint(10, size=(im_height, im_width))
    lens = Lens(im_height, im_width)
    sensor1 = Sensor(old_gain, image, lens)
    with pytest.raises(TypeError, match=expected_error_message):
        sensor1.gain = new_gain


def test_process():
    """Test if process works properly"""
    gain = 3
    im_height, im_width = 3, 3
    image = np.random.randint(10, size=(im_height, im_width))
    lens = Lens(im_height, im_width)
    sensor1 = Sensor(gain, image, lens)
    assert (sensor1.process(image) == gain * image).all()


@pytest.mark.parametrize(
    "height,width,expected_error_message",
    [
        (10, 5, "The size of the image is different to the lens height and width."),
        (5, 10, "The size of the image is different to the lens height and width."),
        (5, 5, "The size of the image is different to the lens height and width."),
    ],
)
def test_process_decorator(height, width, expected_error_message):
    """Test if the decorator calls the Lens process when process is called and handles invalid dimension values."""
    gain = 3
    im_height, im_width = 10, 10
    image = np.random.randint(10, size=(im_height, im_width))
    lens = Lens(height, width)
    sensor1 = Sensor(gain, image, lens)
    with pytest.raises(ValueError, match=expected_error_message):
        sensor1.process(image)


def test_mymean():
    """Test if mymean method works properly."""
    np.random.seed(10)
    im_height = np.random.randint(5, 10)
    im_width = np.random.randint(5, 10)
    gain = np.random.randint(10)
    image = np.random.randint(10, size=(im_height, im_width))
    result = (sum(range(10)) + 10 * image) / 10
    assert (result == mymean(seed=10)).all()
