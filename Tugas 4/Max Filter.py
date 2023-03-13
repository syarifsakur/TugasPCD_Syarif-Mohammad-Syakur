import numpy as np
import cv2

def max_filter(img, kernel_size):
    # Mendefinisikan kernel untuk filter max
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Melakukan padding pada gambar
    pad_size = kernel_size // 2
    padded_img = cv2.copyMakeBorder(img, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REPLICATE)

    # Membuat citra hasil filter max
    filtered_img = np.zeros_like(img)

    # Memproses setiap piksel pada gambar
    for i in range(pad_size, img.shape[0] + pad_size):
        for j in range(pad_size, img.shape[1] + pad_size):
            # Mengambil kernel di sekitar piksel
            kernel_pixels = padded_img[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]
            # Menghitung nilai maksimum dari kernel
            max_val = np.max(kernel_pixels)
            # Menetapkan nilai maksimum ke piksel pada citra hasil filter
            filtered_img[i - pad_size, j - pad_size] = max_val

    return filtered_img

img = cv2.imread("foto1.jpeg",0)  # membaca gambar warna
img = cv2.resize(img, (500, 500))
filtered_img = max_filter(img, 3)  # filter max dengan kernel 3x3
cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()