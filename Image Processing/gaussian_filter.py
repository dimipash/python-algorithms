"""
Gaussian Filter Implementation

Applies Gaussian smoothing to reduce noise and blur images using a 2D
Gaussian function. The filter performs weighted averaging where central
pixels have more influence than peripheral ones.

Time Complexity: O(kernel_width * kernel_height * image_width * image_height)
Space Complexity: O(width * height) for output image
"""


def gaussian_blur(
    image: np.ndarray, kernel_size: tuple = (5, 5), sigma: float = 0
) -> np.ndarray:
    """
    Apply Gaussian blur to an image.

    Args:
        image (np.ndarray): Input image in BGR format
        kernel_size (tuple): Size of Gaussian kernel (must be odd)
        sigma (float): Standard deviation (0 means auto-compute)

    Returns:
        np.ndarray: Blurred image

    Raises:
        ValueError: If kernel dimensions are not odd
    """
    if kernel_size[0] % 2 == 0 or kernel_size[1] % 2 == 0:
        raise ValueError("Kernel dimensions must be odd")

    return cv2.GaussianBlur(image, kernel_size, sigma)


def main() -> None:
    """
    Demonstrate Gaussian blurring with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg")

    # Apply different levels of blurring
    blur_params = [
        ((3, 3), 0),  # Light blur
        ((5, 5), 0),  # Medium blur
        ((9, 9), 0),  # Heavy blur
    ]

    plt.figure(figsize=(12, 4))
    plt.subplot(141)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.xticks([]), plt.yticks([])

    for i, (ksize, sigma) in enumerate(blur_params, 1):
        blurred = gaussian_blur(image, ksize, sigma)
        plt.subplot(141 + i)
        plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
        plt.title(f"Kernel: {ksize[0]}x{ksize[0]}")
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
