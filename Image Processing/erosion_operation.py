import cv2
import numpy as np
import matplotlib.pyplot as plt


def erosion_operation():
    """
    Perform erosion on a binary image using OpenCV.

    Erosion is a morphological operation that removes pixels from the boundaries
    of objects in an image, thereby reducing their size. It is useful for removing
    small-scale noise, separating connected objects, and refining the shape of
    objects by peeling away their outer layers.

    Usage:
        erosion_operation()

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

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display the original and eroded images
    plt.subplot(121), plt.imshow(image, cmap="gray")
    plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(eroded_image, cmap="gray")
    plt.title("Eroded Image"), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    erosion_operation()
