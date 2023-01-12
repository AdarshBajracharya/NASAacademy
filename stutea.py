from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    586.0, -74.0,
    text = "Welcome to",
    fill = "#000000",
    font = ("InriaSans-Regular", int(10.0)))

canvas.create_text(
    596.0, -17.5,
    text = "NASA ACADEMY",
    fill = "#000000",
    font = ("Basic-Regular", int(10.0)))

canvas.create_text(
    575.0, 455.0,
    text = "I am a...",
    fill = "#000000",
    font = ("None", int(10.0)))

window.mainloop()
