from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

def display_images(original, modified, title):
    """
    Display the original and modified images side by side.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(modified)
    axes[1].set_title(title)
    axes[1].axis("off")

    plt.show()

def main():
    try:
        # Load the image
        image = ft_load("landscape.jpg")

        # Apply transformations
        inverted = ft_invert(image)
        red_only = ft_red(image)
        green_only = ft_green(image)
        blue_only = ft_blue(image)
        gray = ft_grey(image)

        # Display results
        display_images(image, inverted, "Inverted Colors")
        display_images(image, red_only, "Red Channel")
        display_images(image, green_only, "Green Channel")
        display_images(image, blue_only, "Blue Channel")
        display_images(image, gray, "Grayscale")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
