"""
Local Binary Pattern Implementation

Computes texture descriptors by comparing each pixel with its neighbors
in a circular pattern. Creates a binary string based on intensity comparisons,
which is then converted to a decimal value.

Time Complexity: O(width * height * P) where P is number of neighbors
Space Complexity: O(width * height) for output image
"""


def local_binary_pattern(image: np.ndarray, P: int = 8, R: int = 1) -> np.ndarray:
    """
    Calculate Local Binary Pattern for an image.

    Args:
        image (np.ndarray): Input grayscale image
        P (int): Number of sampling points
        R (int): Radius of circular pattern

    Returns:
        np.ndarray: LBP image

    Raises:
        ValueError: If image is None or invalid parameters
    """
    if image is None:
        raise ValueError("Input image cannot be None")

    h, w = image.shape
    lbp_image = np.zeros((h, w), dtype=np.uint8)

    # Process each pixel
    for i in range(R, h - R):
        for j in range(R, w - R):
            center = image[i, j]
            binary_string = ""

            # Sample P points on circle of radius R
            for p in range(P):
                theta = 2 * np.pi * p / P
                x = int(i + R * np.sin(theta))
                y = int(j + R * np.cos(theta))

                # Compare with center pixel
                binary_string += "1" if image[x, y] >= center else "0"

            # Convert binary pattern to decimal
            lbp_image[i, j] = int(binary_string, 2)

    return lbp_image


def main() -> None:
    """
    Demonstrate LBP with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Could not load image")

    # Apply LBP with different parameters
    lbp8_1 = local_binary_pattern(image, P=8, R=1)  # Standard LBP
    lbp16_2 = local_binary_pattern(image, P=16, R=2)  # More sampling points

    # Display results
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.imshow(image, cmap="gray")
    plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(132)
    plt.imshow(lbp8_1, cmap="gray")
    plt.title("LBP (P=8, R=1)")
    plt.xticks([]), plt.yticks([])

    plt.subplot(133)
    plt.imshow(lbp16_2, cmap="gray")
    plt.title("LBP (P=16, R=2)")
    plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
