"""
Дополнительное задание лабораторной работы №7.
Студент: Denis Novikov-Ahbabovic
"""

import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

CAT_URL = "https://cataas.com/cat?width=500&height=400"


def load_new_cat():
    try:
        response = requests.get(CAT_URL, timeout=15)
        response.raise_for_status()

        image = Image.open(io.BytesIO(response.content))
        image.thumbnail((500, 400))

        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

    except (requests.RequestException, OSError) as error:
        messagebox.showerror("Ошибка", "Не удалось загрузить картинку.\n\n" + str(error))


root = tk.Tk()
root.title("Генератор котов — Lab 7")
root.geometry("560x500")
root.resizable(False, False)

tk.Label(root, text="Случайный кот", font=("Arial", 18, "bold")).pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

tk.Button(
    root,
    text="Следующая картинка",
    command=load_new_cat,
    font=("Arial", 12),
    width=22
).pack(pady=10)

load_new_cat()
root.mainloop()
