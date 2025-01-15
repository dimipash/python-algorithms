import cv2
import matplotlib.pyplot as plt


def resize_image(image_path, new_width, new_height):
    """
    Resize an image to new dimensions using OpenCV.

    This function loads an image from the specified path, resizes it to the new dimensions,
    and displays both the original and resized images.

    Parameters:
        image_path (str): Path to the input image.
        new_width (int): Desired width of the resized image.
        new_height (int): Desired height of the resized image.

    Time Complexity:
        O(N*M), where N and M are the dimensions of the image.

    Space Complexity:
        O(N*M), where N and M are the dimensions of the image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("Image not found at the specified path.")

        # Get original dimensions
        original_height, original_width = image.shape[:2]
        print(f"Original Dimensions: {original_width} x {original_height}")

        # Maintain aspect ratio if not specified
        if new_width is None:
            ratio = new_height / original_height
            new_width = int(original_width * ratio)
        elif new_height is None:
            ratio = new_width / original_width
            new_height = int(original_height * ratio)
        else:
            # Override aspect ratio
            pass

        print(f"New Dimensions: {new_width} x {new_height}")

        # Choose interpolation method
        if original_width > new_width or original_height > new_height:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC

        # Resize the image
        resized_image = cv2.resize(
            image, (new_width, new_height), interpolation=interpolation
        )

        # Display the original and resized images
        plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Original Image"), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
        plt.title("Resized Image"), plt.xticks([]), plt.yticks([])
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    new_width = 300
    new_height = 200
    resize_image(image_path, new_width, new_height)
