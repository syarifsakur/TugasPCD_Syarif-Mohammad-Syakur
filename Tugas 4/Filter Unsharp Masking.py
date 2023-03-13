import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar grayscale
img = cv2.imread('pemandangan.jpg', 0)

# Lakukan filter Gaussian untuk menghaluskan gambar
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Lakukan operasi unsharp masking
unsharp = cv2.addWeighted(img, 2, gaussian, -1, 0)

# Tampilkan gambar asli dan hasil filter
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(unsharp, cmap='gray')
plt.title('Unsharp Masking Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()