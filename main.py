from tkinter import *
from loginteach import *
from loginstu import *
from PIL import Image, ImageTk


win = Tk()
win.title("NASA Academy")
my_image = ImageTk.PhotoImage(Image.open("logo.png"))
my_label = Label(image=my_image)
my_label.pack()
im = Label(win, text = " I am a..", font = 15)
im.pack()
teach = Button(win, text = "Teacher", command= loginteach)
teach.pack()
stu = Button(win, text = "Student", command = loginstu)
stu.pack()

win.mainloop()