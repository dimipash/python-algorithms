"""
Image Convolution Implementation

Applies a kernel to an image using the convolution operation. The kernel
slides over the image, performing element-wise multiplication and summation
to create transformed features.

Time Complexity: O(M*N*k*k) where M,N are image dimensions, k is kernel size
Space Complexity: O(M*N) for output image
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def convolve_image(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Apply convolution operation to an image using a specified kernel.

    Args:
        image (np.ndarray): Input image (grayscale)
        kernel (np.ndarray): Convolution kernel

    Returns:
        np.ndarray: Convolved image

    Raises:
        ValueError: If kernel dimensions are not odd
    """
    if kernel.shape[0] % 2 == 0 or kernel.shape[1] % 2 == 0:
        raise ValueError("Kernel dimensions must be odd")

    # Apply convolution using OpenCV's filter2D
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)


def main() -> None:
    """
    Demonstrate image convolution with different kernels.
    """
    # Load image in grayscale
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Define different kernels
    kernels = {
        "Edge Detection": np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]),
        "Blur": np.array(
            [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
        ),
        "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
    }

    # Apply each kernel and display results
    plt.figure(figsize=(12, 4))
    plt.subplot(141), plt.imshow(image, cmap="gray")
    plt.title("Original"), plt.xticks([]), plt.yticks([])

    for i, (name, kernel) in enumerate(kernels.items(), 2):
        convolved = convolve_image(image, kernel)
        plt.subplot(141 + i - 1), plt.imshow(convolved, cmap="gray")
        plt.title(name), plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
