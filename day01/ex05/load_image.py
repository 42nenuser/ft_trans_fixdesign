from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Load an image and convert it to a NumPy array.
    """
    try:
        image = Image.open(path)
        print(f"The shape of image is: {np.array(image).shape}")
        return np.array(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        raise
