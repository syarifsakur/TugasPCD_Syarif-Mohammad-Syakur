import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar grayscale
img = cv2.imread('pemandangan.jpg', 0)

# Lakukan DFT pada gambar
dft = np.fft.fft2(img)

# Geser nol frekuensi ke pusat citra
dft_shift = np.fft.fftshift(dft)

# Hitung magnitudo spektrum frekuensi
magnitude_spectrum = 20 * np.log(np.abs(dft_shift))

# Tampilkan gambar asli dan magnitudo spektrum frekuensi
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()