from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def transpose(array: np.ndarray) -> np.ndarray:
    """
    Transpose a 2D or 3D numpy array manually.
    
    Args:
        array (np.ndarray): Input array to transpose.
        
    Returns:
        np.ndarray: Transposed array with the correct shape.
    """
    if len(array.shape) == 3:  # For images with channels (H, W, C)
        return np.transpose(array, (1, 0, 2))  # Swap the first two axes
    elif len(array.shape) == 2:  # For grayscale images (H, W)
        return np.transpose(array)  # Simple transpose for 2D arrays
    else:
        raise ValueError("Unsupported array dimensions for transpose.")


def main():
    try:
        # Load the image
        image = ft_load("animal.jpeg")
        
        # Cut a square part (example: center 400x400 square)
        x_center, y_center = image.shape[0] // 2, image.shape[1] // 2
        square_part = image[x_center-200:x_center+200, y_center-200:y_center+200]

        print(f"Square part shape: {square_part.shape}")
        print(square_part)

        # Perform manual transpose
        transposed = transpose(square_part)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Display the transposed image
        plt.imshow(transposed.astype('uint8'))
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
