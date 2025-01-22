"""
Laplacian Filter Implementation

Detects edges in images using second-order derivatives. The Laplacian
highlights regions of rapid intensity change by calculating the sum of
second derivatives in x and y directions.

Time Complexity: O(width * height) for image dimensions
Space Complexity: O(width * height) for output image
"""

def apply_laplacian(image: np.ndarray, ksize: int = 3) -> np.ndarray:
    """
    Apply Laplacian edge detection to an image.

    Args:
        image (np.ndarray): Input grayscale image
        ksize (int): Kernel size (3, 5, or 7)

    Returns:
        np.ndarray: Edge-detected image

    Raises:
        ValueError: If kernel size is not odd
    """
    if ksize % 2 == 0:
        raise ValueError("Kernel size must be odd")
        
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    
    # Apply Laplacian operator
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F, ksize=ksize)
    
    # Convert to absolute values and 8-bit
    return np.uint8(np.absolute(laplacia
