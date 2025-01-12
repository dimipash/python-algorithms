"""
Canny Edge Detection Algorithm

Implements the Canny edge detection algorithm using OpenCV.
Process includes Gaussian smoothing, gradient calculation,
non-maximum suppression, and hysteresis thresholding.

Time Complexity: O(width * height) for image dimensions
Space Complexity: O(width * height) for output edge map
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny_edge_detection(
    image: np.ndarray,
    threshold1: int = 100,
    threshold2: int = 200,
    aperture_size: int = 3,
) -> np.ndarray:
    """
    Apply Canny edge detection to an image.

    Args:
        image (np.ndarray): Input grayscale image
        threshold1 (int): Lower threshold for hysteresis
        threshold2 (int): Upper threshold for hysteresis
        aperture_size (int): Aperture size for Sobel operator

    Returns:
        np.ndarray: Binary edge map
    """
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 1.4)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold1, threshold2, apertureSize=aperture_size)

    return edges


def main() -> None:
    """
    Demonstrate Canny edge detection with visualization.
    """
    # Load image in grayscale
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Detect edges
    edges = canny_edge_detection(image)

    # Display results
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(image, cmap="gray")
    plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap="gray")
    plt.title("Canny Edge Detection"), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()
