import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('foto1.jpeg', 0)

# Hitung DFT dari gambar
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Buat filter bandpass untuk detail
M, N = img.shape
H = np.ones((M, N))
x, y = np.meshgrid(np.linspace(-N/2, N/2-1, N), np.linspace(-M/2, M/2-1, M))
D = np.sqrt(x**2 + y**2)
D0 = 50  # Frekuensi cutoff
W = 30  # Lebar bandpass
H[np.where((D < D0 - W/2) | (D > D0 + W/2))] = 0

# Terapkan filter pada DFT dari gambar
dft_detail = dft_shift * H

# Buat filter lowpass untuk rata-rata
H = np.zeros((M, N))
cutoff_freq = 40  # Frekuensi cutoff
H = 1 - np.exp(-(D**2)/(2*(cutoff_freq**2)))

# Terapkan filter pada DFT dari gambar
dft_mean = dft_shift * H

# Gabungkan hasil filter detail dan rata-rata
dft_selective = dft_detail + dft_mean

# Hitung inverse DFT dari DFT yang sudah difilter
img_selective = np.fft.ifft2(np.fft.ifftshift(dft_selective))
img_selective = np.real(img_selective)

# Tampilkan gambar asli dan hasil filter
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_selective, cmap='gray')
plt.title('Selective Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()