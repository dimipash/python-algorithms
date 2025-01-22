"""
Image Contrast Adjustment

Modifies image contrast using cv2.convertScaleAbs() where:
- alpha controls contrast (1.0-3.0 for higher, <1.0 for lower)
- beta controls brightness (-100 to 100)

Time Complexity: O(n*m) where n,m are image dimensions
Space Complexity: O(n*m) for storing the modified image
"""


def change_contrast(image: np.ndarray, alpha: float, beta: int = 0) -> np.ndarray:
    """
    Adjust image contrast using alpha and beta parameters.

    Args:
        image (np.ndarray): Input image in BGR format
        alpha (float): Contrast control (1.0-3.0 for higher, <1.0 for lower)
        beta (int): Brightness control (-100 to 100)

    Returns:
        np.ndarray: Contrast-adjusted image
    """
    # Input validation
    if alpha < 0:
        raise ValueError("Alpha must be non-negative")

    # Apply contrast adjustment formula: g(x) = alpha*f(x) + beta
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def main() -> None:
    """
    Example usage of contrast adjustment.
    """
    # Load image
    image = cv2.imread("input_image.jpg")

    # Test different contrast levels
    high_contrast = change_contrast(image, alpha=2.0)  # Increase contrast
    low_contrast = change_contrast(image, alpha=0.5)  # Decrease contrast

    # Display results
    cv2.imshow("Original", image)
    cv2.imshow("High Contrast", high_contrast)
    cv2.imshow("Low Contrast", low_contrast)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
