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




  
def reg():

    frame=Tk()
    frame.title("Registratiion Form")
    frame.geometry("550x600")

    label_1 = Label(frame, text=" TEACHER REGISTRATION ",font=("bold",20),fg='#F5761A',bg='#746AB0')  
    label_1.place(x=90,y=60)  

    label_2 =Label(frame, text= "First Name: ", width=20,font=("bold",10))  
    label_2.place(x=80,y=130)  
    enter_1 = Entry(frame)  
    enter_1.place(x=240,y=130)


    label_3= Label(frame,text="Last Name: ",width=20,font=("bold",10))
    label_3.place(x=80,y=160)
    enter_2 = Entry(frame)  
    enter_2.place(x=240,y=160)

    label_14 = Label(frame, text="Gender: ", width=20,font=("bold",10))  
    label_14.place(x=80,y=190)  

    vars = IntVar() 

    gender_button_male= Radiobutton(frame, text="Male", padx= 5, variable= vars, value=1).place(x=230, y=190)  
    gender_button_female= Radiobutton(frame, text="Female", padx= 20, variable= vars, value=2).place(x=285,y=190)  

    label_4 = Label(frame, text="Email: ", width=20,font=("bold",10))  
    label_4.place(x=80,y=220)  
    enter_3 = Entry(frame)  
    enter_3.place(x=240,y=220)  

    label_5 = Label(frame, text="Address: ", width=20,font=("bold",10))  
    label_5.place(x= 80,y=250)  
    enter_4 = Entry(frame)  
    enter_4.place(x=240,y=250)  

    label_6 = Label(frame, text="Nationality: ", width=20,font=("bold",10))  
    label_6.place(x= 80,y=280)  
    enter_5 = Entry(frame)  
    enter_5.place(x=240,y=280)  

    label_7 = Label(frame, text="Subject: ", width=20,font=("bold",10))  
    label_7.place(x= 80,y=310)  
    list_of_subject=[ 'Maths' ,'Science' , 'English' ,'Social' ,'Nepali' , 'Computer' , 'Opt-Maths' , 'Account' , 'G.k']  
    li = StringVar()  
    drplist = OptionMenu(frame, li, *list_of_subject)  
    drplist.config(width=15,bg='grey')  
    li.set('Select your Subject')  
    drplist.place(x=235, y=304)  


    label_8 = Label(frame, text="Date Of Birth: ", width=20,font=("bold",10))  
    label_8.place(x= 80,y=340)  
    enter_7 = Entry(frame)  
    enter_7.place(x=240,y=340) 

    label_9 = Label(frame, text="Place Of Birth: ", width=20,font=("bold",10))  
    label_9.place(x= 80,y=370)  
    enter_8 = Entry(frame)  
    enter_8.place(x=240,y=370) 

    label_10 = Label(frame, text="Language: ", width=20,font=("bold",10))  
    label_10.place(x= 80,y=400)  
    enter_9 = Entry(frame)  
    enter_9.place(x=240,y=400)

    label_13= Label(frame, text="Social Network Site: ", width=20,font=("bold",10))  
    label_13.place(x= 80,y=490)  
    enter_11 = Entry(frame)  
    enter_11.place(x=240,y=490)

    submit_button= Button(frame, text='Submit' , width=20, bg="black",fg='white')
    submit_button.place(x=180,y=530)  


    frame.mainloop()


stutea()
