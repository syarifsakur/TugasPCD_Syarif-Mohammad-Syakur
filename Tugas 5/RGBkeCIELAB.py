import cv2
import numpy as np


# Fungsi transformasi RGB ke CIELAB
def rgb_to_cielab(r, g, b):
    # Konversi ke rentang 0-1
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    # Transformasi gamma
    if r > 0.04045:
        r = ((r + 0.055) / 1.055) ** 2.4
    else:
        r = r / 12.92

    if g > 0.04045:
        g = ((g + 0.055) / 1.055) ** 2.4
    else:
        g = g / 12.92

    if b > 0.04045:
        b = ((b + 0.055) / 1.055) ** 2.4
    else:
        b = b / 12.92

    # RGB ke XYZ
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505

    # White reference
    x = x / 0.95047
    y = y / 1.00000
    z = z / 1.08883

    # XYZ ke CIELAB
    if x > 0.008856:
        fx = x ** (1.0 / 3.0)
    else:
        fx = (7.787 * x) + (16.0 / 116.0)

    if y > 0.008856:
        fy = y ** (1.0 / 3.0)
    else:
        fy = (7.787 * y) + (16.0 / 116.0)

    if z > 0.008856:
        fz = z ** (1.0 / 3.0)
    else:
        fz = (7.787 * z) + (16.0 / 116.0)

    l = (116.0 * fy) - 16.0
    a = 500.0 * (fx - fy)
    b = 200.0 * (fy - fz)

    return l, a, b


# Load gambar
img = cv2.imread('foto1.jpeg')

# Membuat salinan gambar dengan format float
img_float = np.float32(img) / 255.0

# Menghitung nilai CIELAB
cielab_img = cv2.cvtColor(img_float, cv2.COLOR_RGB2LAB)

# Memisahkan nilai L, a, dan b
l, a, b = cv2.split(cielab_img)

# Menampilkan hasil
cv2.imshow('Gambar asli', img)
cv2.imshow('Gambar CIELAB', cv2.merge([l, a, b]))
cv2.waitKey(0)
cv2.destroyAllWindows()