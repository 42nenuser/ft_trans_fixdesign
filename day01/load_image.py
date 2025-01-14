import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path and convert it to a numpy array.
    
    Args:
        path (str): Path to the image file.
        
    Returns:
        np.ndarray: Numpy array of the image data.
    """
    try:
        image = Image.open(path)
        print(f"The shape of image is: {np.array(image).shape}")
        return np.array(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        raise
