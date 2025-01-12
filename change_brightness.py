"""
Image Brightness Adjustment

Modifies image brightness by converting to HSV color space and adjusting 
the V (Value) channel. Works with 8-bit images where pixel values range 
from 0 (black) to 255 (white).

Time Complexity: O(n*m) where n,m are image dimensions
Space Complexity: O(n*m) for storing the modified image
"""


def change_brightness(image: np.ndarray, value: int) -> np.ndarray:
    """
    Adjust image brightness using HSV color space.

    Args:
        image (np.ndarray): Input image in BGR format
        value (int): Brightness adjustment (-255 to 255)

    Returns:
        np.ndarray: Brightness-adjusted image in BGR format
    """
    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split into H, S, V channels
    h, s, v = cv2.split(hsv)

    # Adjust V channel and clip to valid range
    v = np.clip(v + value, 0, 255)

    # Merge channels and convert back to BGR
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


def main() -> None:
    """
    Example usage of brightness adjustment.
    """
    # Load image
    image = cv2.imread("input_image.jpg")

    # Adjust brightness
    bright = change_brightness(image, 50)  # Brighter
    dark = change_brightness(image, -50)  # Darker

    # Display results
    cv2.imshow("Original", image)
    cv2.imshow("Brighter", bright)
    cv2.imshow("Darker", dark)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
