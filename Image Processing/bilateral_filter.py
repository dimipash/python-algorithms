"""
Bilateral Filter Implementation

Applies edge-preserving smoothing using both spatial and intensity differences.
Combines a Gaussian filter with a range filter to preserve edges while
reducing noise.

Time Complexity: O(n*m*r^2) where n,m are image dimensions, r is filter radius
Space Complexity: O(n*m) for output filtered image
"""


def bilateral_filter(
    image: np.ndarray, d: int = 15, sigma_color: float = 75, sigma_space: float = 75
) -> np.ndarray:
    """
    Apply bilateral filtering to an image.

    Args:
        image (np.ndarray): Input image in BGR format
        d (int): Diameter of pixel neighborhood
        sigma_color (float): Filter sigma in color space
        sigma_space (float): Filter sigma in coordinate space

    Returns:
        np.ndarray: Filtered image
    """
    # Apply bilateral filter using OpenCV
    return cv2.bilateralFilter(image, d, sigma_color, sigma_space)


def main() -> None:
    """
    Demonstrate bilateral filtering with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg")

    # Apply bilateral filter
    filtered = bilateral_filter(image)

    # Display results
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB))
    plt.title("Bilateral Filtered")
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()
