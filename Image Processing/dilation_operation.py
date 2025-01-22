import cv2
import numpy as np
import matplotlib.pyplot as plt


def dilation_operation():
    """
    Perform dilation on a binary image using OpenCV.

    Dilation is a morphological operation that adds pixels to the boundaries
    of objects in an image, thereby increasing their size. It is useful for
    filling gaps, connecting nearby objects, and expanding object boundaries.

    Usage:
        dilation_operation()

    Time Complexity:
        O(N*M), where N and M are the dimensions of the image.

    Space Complexity:
        O(N*M), where N and M are the dimensions of the image.
    """

    # Create a binary image
    image = np.array(
        [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],
        dtype=np.uint8,
    )

    # Define the structuring element (3x3 square)
    kernel = np.ones((3, 3), np.uint8)

    # Apply dilation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display the original and dilated images
    plt.subplot(121), plt.imshow(image, cmap="gray")
    plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dilated_image, cmap="gray")
    plt.title("Dilated Image"), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    dilation_operation()
