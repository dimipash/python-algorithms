"""
Sobel Edge Detection Filter

Detects edges using two 3x3 kernels for horizontal and vertical gradients.
Combines Gaussian smoothing with differentiation to balance noise reduction
and edge detection.

Time Complexity: O(width * height) for convolution operations
Space Complexity: O(width * height) for gradient images
"""


def sobel_filter(image: np.ndarray) -> np.ndarray:
    """
    Apply Sobel edge detection to an image.

    Args:
        image (np.ndarray): Input grayscale image

    Returns:
        np.ndarray: Edge-detected image showing gradient magnitudes
    """
    # Define Sobel kernels for x and y directions
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Calculate gradients using convolution
    gradient_x = cv2.filter2D(image, cv2.CV_64F, sobel_x)
    gradient_y = cv2.filter2D(image, cv2.CV_64F, sobel_y)

    # Compute gradient magnitude
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalize to 8-bit range
    return np.uint8(np.clip(gradient_magnitude, 0, 255))


def main() -> None:
    """
    Demonstrate Sobel edge detection with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Apply Sobel filter
    edges = sobel_filter(image)

    # Display results
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.imshow(image, cmap="gray")
    plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(edges, cmap="gray")
    plt.title("Sobel Edges")
    plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
