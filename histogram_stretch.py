"""
Histogram Stretching Implementation

Enhances image contrast by stretching the intensity values to cover
the full dynamic range [0,255]. Uses the formula:
output = (input - min) * 255 / (max - min)

Time Complexity: O(width * height) for pixel operations
Space Complexity: O(width * height) for output image
"""


def histogram_stretch(image: np.ndarray) -> np.ndarray:
    """
    Apply histogram stretching to enhance image contrast.

    Args:
        image (np.ndarray): Input grayscale image

    Returns:
        np.ndarray: Contrast-enhanced image

    Raises:
        ValueError: If image is None or has zero range
    """
    if image is None:
        raise ValueError("Input image cannot be None")

    # Get min and max intensity values
    I_min = np.min(image)
    I_max = np.max(image)

    # Check for zero range to avoid division by zero
    if I_max == I_min:
        return image

    # Apply stretching formula
    return ((image - I_min) * 255 / (I_max - I_min)).astype(np.uint8)


def main() -> None:
    """
    Demonstrate histogram stretching with visualization.
    """
    # Load image
    image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

    # Apply stretching
    stretched = histogram_stretch(image)

    # Display results
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.imshow(image, cmap="gray")
    plt.title("Original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(stretched, cmap="gray")
    plt.title("Stretched")
    plt.xticks([]), plt.yticks([])

    plt.show()
