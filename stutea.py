from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title("NASA Academy")
my_image = ImageTk.PhotoImage(Image.open("logo.png"))
my_label = Label(image=my_image)
my_label.pack()

def loginteach():
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Teacher login')

    #username label and text entry box
    usernameLabel = Label(tkWindow, text="Teacher ID").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  


    #login button
    loginButton = Button(tkWindow, text="Login").grid(row=4, column=0)  

    tkWindow.mainloop()

def loginstu():
    tkWindo = Tk()  
    tkWindo.geometry('400x150')  
    tkWindo.title('Student Login')

    #username label and text entry box
    usernameLabel = Label(tkWindo, text="Student ID").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindo, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(tkWindo,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindo, textvariable=password, show='*').grid(row=1, column=1)  


    #login button
    loginButton = Button(tkWindo, text="Login").grid(row=4, column=0)  

    tkWindo.mainloop()

im = Label(win, text = " I am a..", font = 15)
im.pack()
teach = Button(win, text = "Teacher", command= loginteach)
teach.pack()
stu = Button(win, text = "Student", command = loginstu)
stu.pack()

win.mainloop()