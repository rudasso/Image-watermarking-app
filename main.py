import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageGrab
from PIL.Image import Resampling
import matplotlib.pyplot as plt


filepath = ""
load = []
watermark = ""
render = ""

window = tk.Tk()


# OPEN FILE

def open_file():
    global filepath
    global load
    filepath = filedialog.askopenfilename(title="Choose your file to open")
    print(filepath)
    load = Image.open(filepath)
    print(type(load))
    preview = load
    preview.thumbnail((400, 400), Resampling.LANCZOS)
    print(type(load))

    render = ImageTk.PhotoImage(preview)

    img = tk.Label(image=render)
    img.image = render
    img.grid(column=2, row=1, sticky="e", rowspan=5, padx=20)
    return load


# SAVE WATERMARK
def getvalue():
    global watermark
    watermark = watermark_entry.get()


# ADD WATERMARK

def add_watermark(color):
    global watermark
    global load
    global render

    def watermark_to_file(file):
        file = Image.open(filepath)
        draw = ImageDraw.Draw(file)
        text_font = ImageFont.truetype("arial.ttf", 70)
        draw.text((0, 0), watermark, color, font=text_font)
        plt.subplot(1, 2, 1)
        return file

    load = watermark_to_file(load)
    preview = watermark_to_file(load)

    preview.thumbnail((400, 400), Resampling.LANCZOS)

    render = ImageTk.PhotoImage(preview)

    img = tk.Label(image=render)
    img.image = render
    img.grid(column=2, row=1, sticky="e", rowspan=5, padx=20)


def add_watermark_black():
    add_watermark("black")


def add_watermark_white():
    add_watermark("white")


def save_file():
    global load
    files = [("All files", "*.*"), ("JPG files", ".jpg"), ("JPEG files", ".jpeg")]
    img = asksaveasfile(title="Save your file", filetypes=files, defaultextension=files, mode="wb")
    load.save(img)


window.title("Watermark your image")
window.config(padx=70, pady=10, width=400, height=400)

title_label = Label(text="Open file to watermark ")
title_label.grid(row=0, columnspan=3, ipadx=20, ipady=10)

choose_file = Button(text="Choose file", command=open_file, height=2, width=30)
choose_file.grid(row=1, columnspan=2, pady=10, sticky=W)

Label(text="Write your watermark text:").grid(column=0, row=2, sticky=W)
watermark_entry = tk.Entry(window, width=40)
watermark_entry.grid(column=0, row=3, sticky=W)

saving_text_button = Button(text="Save text", command=getvalue, width=10)
saving_text_button.grid(row=3, column=1, sticky=W, padx=10)

watermark_btn = Button(text="Add black Watermark to your picture", command=add_watermark_black, height=2, width=30)
watermark_btn.grid(row=5, column=0, pady=10, sticky=W)

watermark_btn = Button(text="Add white Watermark to your picture", command=add_watermark_white, height=2, width=30)
watermark_btn.grid(row=5, column=1, pady=10)

saving_button = Button(text="Save file", command=save_file, width=10)
saving_button.grid(row=6, column=0, sticky=W)

window.mainloop()
