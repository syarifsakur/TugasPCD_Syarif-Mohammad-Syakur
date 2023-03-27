import cv2
import numpy as np
from skimage import io, color

# Load image
img = io.imread('foto1.jpeg')

# Convert image to LAB color space
lab_img = color.rgb2lab(img)

# Extract L, A, B channels
L_channel = lab_img[:, :, 0]
A_channel = lab_img[:, :, 1]
B_channel = lab_img[:, :, 2]

# Normalize channels
L_channel = L_channel / 100
A_channel = (A_channel + 128) / 255
B_channel = (B_channel + 128) / 255

# Convert normalized LAB values to linear RGB values
R = np.clip((3.2406 * L_channel - 1.5372 * A_channel - 0.4986 * B_channel) * 255, 0, 255)
G = np.clip((-0.9689 * L_channel + 1.8758 * A_channel + 0.0415 * B_channel) * 255, 0, 255)
B = np.clip((0.0557 * L_channel - 0.2040 * A_channel + 1.0570 * B_channel) * 255, 0, 255)

# Merge channels and convert back to uint8
rgb_img = np.dstack((R, G, B)).astype(np.uint8)

# Display original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Transformed Image', rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()