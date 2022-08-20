import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
from PIL.Image import Resampling
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

filepath = ""

window = tk.Tk()
load = []
watermark = ""


# OPEN FILE

def open_file():
    global filepath
    global load
    filepath = filedialog.askopenfilename(title="Choose your file to open")
    print(filepath)
    load = Image.open(filepath)
    load.thumbnail((400, 400), Resampling.LANCZOS)

    render = ImageTk.PhotoImage(load)

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
    draw = ImageDraw.Draw(load)
    text_font = ImageFont.truetype("arial.ttf", 50)

    # add watermark
    draw.text((0, 0), watermark, color, font=text_font)
    plt.subplot(1, 2, 1)

    render = ImageTk.PhotoImage(load)

    img = tk.Label(image=render)
    img.image = render
    img.grid(column=2, row=1, sticky="e", rowspan=5, padx=20)


def add_watermark_black():
    add_watermark("black")


def add_watermark_white():
    add_watermark("white")


def save_file():
    pass


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

Label(text="Write name of file:").grid(column=0, row=4, sticky=SW)
name_saving_file = Entry(width=40).grid(row=5, columnspan=2, pady=10, sticky=W)

saving_button = Button(text="Save file", command=save_file, width=10)
saving_button.grid(row=5, column=1, sticky=W, padx=10)

watermark_btn = Button(text="Add black Watermark to your picture", command=add_watermark_black, height=2, width=30)
watermark_btn.grid(row=6, column=0, pady=10, padx=10)

watermark_btn = Button(text="Add white Watermark to your picture", command=add_watermark_white, height=2, width=30)
watermark_btn.grid(row=6, column=1, pady=10, padx=10)

window.mainloop()
