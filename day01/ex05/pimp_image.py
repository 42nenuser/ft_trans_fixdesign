import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of an image.
    """
    return 255 - array

def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Highlight the red channel by setting green and blue to zero.
    """
    result = np.zeros_like(array)
    result[..., 0] = array[..., 0]  # Copy the red channel
    return result

def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Highlight the green channel by setting red and blue to zero.
    """
    result = np.zeros_like(array)
    result[..., 1] = array[..., 1]  # Copy the green channel
    return result

def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Highlight the blue channel by setting red and green to zero.
    """
    result = np.zeros_like(array)
    result[..., 2] = array[..., 2]  # Copy the blue channel
    return result

def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert an image to grayscale using the average method.
    """
    gray = np.mean(array, axis=-1).astype('uint8')
    return np.stack((gray, gray, gray), axis=-1)  # Retain 3 channels
