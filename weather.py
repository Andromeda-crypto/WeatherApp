import tkinter as tk
import requests
import time


def getWeather():
    city = textfield.get()
    



canvas = tk.TK()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t, width=20)
textfield.pack(pady=20)
textfield.focus()

label1 = tk.label(canvas,font= t)
label1.pack()
label2 = tk.label(canvas,font = f)
label2.pack()

canvas.mainloop()

