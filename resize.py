import cv2
import matplotlib.pyplot as plt


def resize_image():
    """
    Resize an image to new dimensions using OpenCV.

    This function loads an image from a specified path, resizes it to new dimensions,
    and displays both the original and resized images.

    Usage:
        resize_image()

    Time Complexity:
        O(N*M), where N and M are the dimensions of the image.

    Space Complexity:
        O(N*M), where N and M are the dimensions of the image.
    """

    # Load an image (replace 'path_to_your_image.jpg' with the actual image path)
    image = cv2.imread("path_to_your_image.jpg")

    # Get original dimensions
    original_height, original_width = image.shape[:2]
    print(f"Original Dimensions: {original_width} x {original_height}")

    # Define new dimensions
    new_width = 300
    new_height = 200
    print(f"New Dimensions: {new_width} x {new_height}")

    # Resize the image
    resized_image = cv2.resize(
        image, (new_width, new_height), interpolation=cv2.INTER_LINEAR
    )

    # Display the original and resized images
    plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.title("Resized Image"), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    resize_image()
