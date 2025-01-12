"""
Burkes Dithering Algorithm

Converts grayscale images to binary using error diffusion with Burkes pattern:
    * 8/32 4/32
2/32 4/32 8/32 4/32 2/32

Time Complexity: O(width * height) for image dimensions
Space Complexity: O(width * height) for pixel array
"""

import numpy as np
from PIL import Image


def burkes_dithering(image: Image) -> Image:
    """
    Apply Burkes dithering to convert image to binary.

    Args:
        image: Input PIL Image

    Returns:
        PIL Image: Dithered binary image

    Raises:
        ValueError: If image is invalid
    """
    # Convert to grayscale
    gray_image = image.convert("L")
    pixels = np.array(gray_image, dtype=np.float32)
    height, width = pixels.shape

    # Process each pixel
    for y in range(height):
        for x in range(width):
            # Get old pixel value and threshold it
            old_pixel = pixels[y, x]
            new_pixel = 255 if old_pixel > 127 else 0
            pixels[y, x] = new_pixel

            # Calculate quantization error
            quant_error = old_pixel - new_pixel

            # Distribute error to neighbors using Burkes pattern
            if x + 1 < width:
                pixels[y, x + 1] += quant_error * 8 / 32
            if x + 2 < width:
                pixels[y, x + 2] += quant_error * 4 / 32

            if y + 1 < height:
                for i in range(-2, 3):
                    if 0 <= x + i < width:
                        weight = (
                            2 / 32 if abs(i) == 2 else 4 / 32 if abs(i) == 1 else 8 / 32
                        )
                        pixels[y + 1, x + i] += quant_error * weight

    # Convert back to 8-bit image
    return Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8))


def main() -> None:
    """
    Example usage of Burkes dithering.
    """
    # Load and process image
    image = Image.open("input.jpg")
    dithered = burkes_dithering(image)
    dithered.save("output.jpg")
