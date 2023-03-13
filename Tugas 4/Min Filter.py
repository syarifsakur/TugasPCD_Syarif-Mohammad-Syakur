import numpy as np
import cv2

def min_filter(img, kernel_size):
    # Mendefinisikan kernel untuk filter min
    kernel = np.ones((kernel_size, kernel_size, 3), np.uint8)

    # Melakukan padding pada gambar
    pad_size = kernel_size // 2
    padded_img = cv2.copyMakeBorder(img, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REPLICATE)

    # Membuat citra hasil filter min
    filtered_img = np.zeros_like(img)

    # Memproses setiap piksel pada gambar
    for i in range(pad_size, img.shape[0] + pad_size):
        for j in range(pad_size, img.shape[1] + pad_size):
            # Mengambil kernel di sekitar piksel
            kernel_pixels = padded_img[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1, :]
            # Menghitung nilai minimum dari kernel untuk setiap channel
            min_val = np.min(kernel_pixels, axis=(0, 1))
            # Menetapkan nilai minimum ke piksel pada citra hasil filter
            filtered_img[i - pad_size, j - pad_size, :] = min_val

    return filtered_img

img = cv2.imread("pemandangan.jpg")  # membaca gambar warna
img = cv2.resize(img, (500, 500))
filtered_img = min_filter(img, 3)  # filter min dengan kernel 3x3
cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()