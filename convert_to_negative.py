"""
Image Negative Converter

Converts an image to its negative by inverting pixel values using the formula:
negative = 255 - original_value
Works with both grayscale and color images (BGR format).

Time Complexity: O(n*m) where n,m are image dimensions
Space Complexity: O(n*m) for storing the negative image
"""

import cv2
import numpy as np


def convert_to_negative(image: np.ndarray) -> np.ndarray:
    """
    Convert image to its negative by inverting pixel values.

    Args:
        image (np.ndarray): Input image in BGR or grayscale format

    Returns:
        np.ndarray: Negative version of input image

    Examples:
        >>> img = cv2.imread('image.jpg')
        >>> negative = convert_to_negative(img)
    """
    # Invert pixel values using numpy's broadcasting
    return 255 - image


def main() -> None:
    """
    Demonstrate image negative conversion with examples.
    """
    # Load color and grayscale images
    color_img = cv2.imread("input_image.jpg")
    gray_img = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Convert to negatives
    color_negative = convert_to_negative(color_img)
    gray_negative = convert_to_negative(gray_img)

    # Display results
    cv2.imshow("Original Color", color_img)
    cv2.imshow("Color Negative", color_negative)
    cv2.imshow("Original Grayscale", gray_img)
    cv2.imshow("Grayscale Negative", gray_negative)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
