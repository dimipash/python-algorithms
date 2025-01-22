import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_sepia(image):
    """
    Apply a sepia tone to the input image.

    Parameters:
        image (numpy.ndarray): Input image in BGR format.

    Returns:
        numpy.ndarray: Sepia-toned image in BGR format.
    """
    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Define the sepia filter matrix
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )
    # Apply the sepia filter
    sepia_image = cv2.transform(image_rgb, sepia_filter)
    # Clip the values to be within [0, 255]
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)
    # Convert back to BGR for OpenCV
    sepia_image_bgr = cv2.cvtColor(sepia_image, cv2.COLOR_RGB2BGR)
    return sepia_image_bgr


# Load the image
image_path = "path_to_your_image.jpg"  # Replace with your image path
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found.")
else:
    # Apply sepia filter
    sepia_image = apply_sepia(image)
    # Display the original and sepia images
    plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(cv2.cvtColor(sepia_image, cv2.COLOR_BGR2RGB))
    plt.title("Sepia Image"), plt.xticks([]), plt.yticks([])
    plt.show()
