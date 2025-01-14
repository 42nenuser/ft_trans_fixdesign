import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load image
image = np.array(Image.open("landscape.jpg"))

# Apply transformations
inverted = 255 - image
grayscale = np.mean(image, axis=-1)

# Display results
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image.astype('uint8'))
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(inverted.astype('uint8'))
axes[1].set_title("Inverted Colors")
axes[1].axis("off")

axes[2].imshow(grayscale, cmap='gray')
axes[2].set_title("Grayscale")
axes[2].axis("off")

plt.show()
