import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar grayscale
img = cv2.imread('pemandangan.jpg', 0)

# Lakukan transformasi Fourier pada gambar
f = np.fft.fft2(img)

# Geser nol frekuensi ke pusat
fshift = np.fft.fftshift(f)

# Hitung magnitudo spektrum frekuensi
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Buat filter kernel
rows, cols = img.shape
crow, ccol = rows//2, cols//2
D = 30  # jari-jari lingkaran pada filter kernel
kernel = np.zeros((rows, cols), np.uint8)
cv2.circle(kernel, (crow, ccol), D, 1, -1)

# Terapkan filter kernel pada domain frekuensi
fshift = fshift * kernel

# Geser kembali nol frekuensi ke sudut kiri atas
f_ishift = np.fft.ifftshift(fshift)

# Lakukan inverse Fourier transform
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Tampilkan gambar asli, spektrum frekuensi, dan hasil filter
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back, cmap='gray')
plt.title('Laplacian Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()