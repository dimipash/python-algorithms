"""
Gabor Filter Implementation

Combines Gaussian function with sinusoidal wave to analyze textures and 
patterns in images. Particularly useful for texture analysis, edge detection,
and feature extraction.

Time Complexity: O(ksize^2 * width * height) for filter application
Space Complexity: O(width * height) for output image
"""


def create_gabor_filter(
    ksize: int = 21,
    sigma: float = 5.0,
    theta: float = np.pi / 4,
    lambd: float = 10.0,
    gamma: float = 0.5,
    psi: float = 0,
) -> np.ndarray:
    """
    Create a Gabor filter kernel with specified parameters.

    Args:
        ksize (int): Size of the filter kernel
        sigma (float): Standard deviation of Gaussian envelope
        theta (float): Orientation of filter in radians
        lambd (float): Wavelength of sinusoidal factor
        gamma (float): Spatial aspect ratio
        psi (float): Phase offset

    Returns:
        np.ndarray: Gabor filter kernel
    """
    return cv2.getGaborKernel(
        (ksize, ksize), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F
    )


def apply_gabor_filter(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Apply Gabor filter to an image.

    Args:
        image (np.ndarray): Input grayscale image
        kernel (np.ndarray): Gabor filter kernel

    Returns:
        np.ndarray: Filtered image
    """
    return cv2.filter2D(image, cv2.CV_8UC3, kernel)


def main() -> None:
    """
    Demonstrate Gabor filtering with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Create filters with different orientations
    thetas = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

    # Apply filters and display results
    plt.figure(figsize=(12, 4))
    plt.subplot(151), plt.imshow(image, cmap="gray")
    plt.title("Original"), plt.xticks([]), plt.yticks([])

    for i, theta in enumerate(thetas, 1):
        kernel = create_gabor_filter(theta=theta)
        filtered = apply_gabor_filter(image, kernel)
        plt.subplot(151 + i)
        plt.imshow(filtered, cmap="gray")
        plt.title(f"θ={theta:.2f}")
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
