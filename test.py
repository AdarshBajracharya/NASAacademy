from tkinter import *
from tkinter import messagebox
from tkextrafont import Font
from PIL import ImageTk,Image
import sqlite3

def stutea():

    
    global win
    global re
    global reimg
    global restu
    global reteach
   
    #Creating window
    win = Tk()
    win.title("NASA Academy")
    win.iconbitmap("images/cap.ico")
    win.geometry("1920x1080")
        


    studen = Image.open("images\\student.png")     
    imge= studen.resize((300, 300))  
    restu = ImageTk.PhotoImage(imge)      

    teac = Image.open("images\\teacher.png")     
    timg= teac.resize((300, 300))  
    reteach = ImageTk.PhotoImage(timg)     

    #Setting background image
    bg = Image.open("images\\sbac.jpg")     
    imag= bg.resize((1600, 1080))  
    re = ImageTk.PhotoImage(imag)   
    l1 = Label(win, image=re, borderwidth=0)
    l1.place(x=0, y=0)
    
    #Creating frame
    frame = Frame(win,width=700,height=750, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)


    def framelog():
        frame.pack_forget()
        login()
    

    def framereg():
        frame.pack_forget()
        reg()


    #Inserting font
    he = Font(file="fonts\Heavitas.ttf", family="Heavitas")

    #Creating Labels, buttons and inserting images
    top = Label(frame, text = "Welcome  to", font = ("Heavitas", 15))
    top.pack(padx= 0, pady = 20)
    top2 = Label(frame, text = "NASA ACADEMY", font = ("heavitas", 30))
    top2.place(x= 170, y = 50)
    my_image = Image.open("images/logoo.png")     
    img= my_image.resize((300, 300))  
    reimg = ImageTk.PhotoImage(img)        
    my_label = Label(frame, image=reimg, borderwidth=0)
    my_label.place(x = 190, y = 150)
    teach = Button(frame, text = "REGISTER", width = 10, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command=framereg)
    teach.place(x = 240, y = 600)
    stu = Button(frame, text = "LOGIN", width = 10, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command=framelog)
    stu.place(x = 240, y = 530)

    win.mainloop()

def login():

    frame = Frame(win,width=1000,height=650, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)
     
    my_label = Label(frame, image=restu, borderwidth=0)
    my_label.place(x = 70, y = 180)
    s = Label(frame, text = "Student Sign In", font = ("Microsoft Yahei UI light",23))
    s.place (x = 370, y = 20)
    l=Label(frame,text="Student ID",font = ("Helvetica",12))
    l.place(x=550,y=150)
    e = Entry(frame,width = 30)
    e.place(x=550,y=180)
    l2=Label(frame,text="Password",font = ("Helvetica",12))
    l2.place(x=550,y=220)
    e2 =Entry(frame, width =30)
    e2.place(x=550,y=250)
    b= Button(frame, text="Log in",font=5,bg="blue", height = 1, width = 10,fg="white")
    b.place(x =620, y = 310)
    b2= Button(frame,text="Dont have an account ?sign up",padx=10,pady=5,command=reg)
    b2.place(x = 580, y = 380)


