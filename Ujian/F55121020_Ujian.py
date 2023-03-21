import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def brightness_correction(img):
    brightness = 100
    bright_img = cv2.add(img, brightness)
    return bright_img

def grayscale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

# fungsi untuk menampilkan gambar dalam kotak
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# fungsi untuk memproses citra dan menampilkan hasilnya
def process_image(method):
    global original_img
    if method == 'brightness_correction':
        corrected_img = brightness_correction(original_img)
        show_image(corrected_img, 560, 80, 'Perbaikan Metode 1')
    elif method == 'grayscale':
        corrected_img = grayscale(original_img)
        show_image(corrected_img, 830, 80, 'Perbaikan Metode 2')

# fungsi untuk menampilkan informasi pembuat program
def show_creator():
    creator_label = tk.Label(root, text='Nama : Syarif Mohammad Syakur | NIM : F55121020 |  Kelas : A')
    creator_label.place(x=500, y=625)

# fungsi untuk membuka gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        show_image(original_img, 275, 80, 'Gambar Original')
        size_label.config(text='Dimensi : {} x {}'.format(original_img.shape[1], original_img.shape[0]))

# membuat jendela utama
root = tk.Tk()
root.geometry('1400x1000')
root.title('GUI Aplikasi Penerapan Perbaikan Citra')

# menambahkan tombol untuk membuka gambar
open_button = tk.Button(root, text='Buka Gambar', command=open_image)
open_button.place(x=320, y=515)

# menambahkan label untuk menampilkan dimensi gambar
size_label = tk.Label(root, text='Dimensi : -')
size_label.place(x=320, y=545)

# menambahkan kotak untuk hasil perbaikan citra
correction_box = tk.LabelFrame(root, text='hasil Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=250, y=10, width=800, height=500)

#menambahkan kotak perbaikan citra
correction_box = tk.LabelFrame(root, text='Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=500, y=510, width=350, height=60)

# tombol untuk perbaikan metode 1 (grayscale)
brightness_button = tk.Button(correction_box, text='Kecerahan', command=lambda: process_image('brightness_correction'))
brightness_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode 2 (contrast stretching)
smoothing_button = tk.Button(correction_box, text='Grayscaling', command=lambda: process_image('grayscale'))
smoothing_button.pack(side=tk.LEFT, padx=5)

# menambahkan kotak untuk informasi pembuat program
creator_box = tk.LabelFrame(root, text='Di Susun Oleh', padx=5, pady=5)
creator_box.place(x=475, y=600, width=400, height=70)

# menampilkan informasi pembuat program
show_creator()

# menjalankan program
root.mainloop()

