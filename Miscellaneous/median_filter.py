"""
Median Filter Implementation

Applies non-linear filtering to reduce noise while preserving edges.
Particularly effective for removing salt-and-pepper noise by replacing
each pixel with the median of its neighborhood.

Time Complexity: O(width * height * kernel_size^2)
Space Complexity: O(width * height)
"""


def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    """
    Apply median filter to an image.

    Args:
        image (np.ndarray): Input grayscale image
        kernel_size (int): Size of the filter kernel (must be odd)

    Returns:
        np.ndarray: Filtered image

    Raises:
        ValueError: If kernel_size is not odd
    """
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd")

    # Pad image to handle borders
    pad_size = kernel_size // 2
    padded = cv2.copyMakeBorder(
        image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REFLECT
    )

    height, width = image.shape
    filtered = np.zeros_like(image)

    # Process each pixel
    for i in range(height):
        for j in range(width):
            # Extract neighborhood and compute median
            neighborhood = padded[i : i + kernel_size, j : j + kernel_size].flatten()
            filtered[i, j] = np.median(neighborhood)

    return filtered


def main() -> None:
    """
    Demonstrate median filtering with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Apply median filter with different kernel sizes
    filtered3 = median_filter(image, 3)  # 3x3 kernel
    filtered5 = median_filter(image, 5)  # 5x5 kernel

    # Display results
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.imshow(image, cmap="gray")
    plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(132)
    plt.imshow(filtered3, cmap="gray")
    plt.title("3x3 Median Filter")
    plt.xticks([]), plt.yticks([])

    plt.subplot(133)
    plt.imshow(filtered5, cmap="gray")
    plt.title("5x5 Median Filter")
    plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
