from tkinter import *
from tkinter import messagebox
from tkextrafont import Font
from PIL import ImageTk,Image
import creds
import database


def main():

    """
    main function where images, fonts and window is defined and starting page is displayed
    """


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

    my_image = Image.open("images\\logoo.png")     
    img= my_image.resize((300, 300))  
    reimg = ImageTk.PhotoImage(img)      

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
        homepage()
    

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

    def clickreg():
        frame.pack_forget()
        reg()

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
    e2_str=StringVar()
    l3=Label(frame,text="Show password",font = ("Helvetica",10))
    l3.place(x=630,y=282)
    e2 =Entry(frame, width =30,show = "*",textvariable=e2_str)
    e2.place(x=550,y=250)
    check=IntVar(value=0)

    def show():
        if(check.get()==1):
            e2.config(show='')
        else:
            e2.config(show='*')

    cb = Checkbutton(frame,variable = check,command = show)
    cb.place(x=600, y = 280)
    b= Button(frame, text="Log in",font=5,bg="blue", height = 1, width = 10,fg="white")
    b.place(x =620, y = 310)
    b2= Button(frame,text="Dont have an account ?Register",padx=10,pady=5,command=clickreg)
    b2.place(x = 580, y = 380)




  
def reg():

    frame = Frame(win,width=650,height=650, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=100)
    frame.pack_propagate(False)

    def clicklog():
        frame.pack_forget()
        login()
    
     

    label_1 = Label(frame, text=" REGISTRATION ",font=("Heavitas",20))  
    label_1.place(x=200,y=30)  

    label_2 =Label(frame, text= "First Name: ", width=20,font=("Verdana",10))  
    label_2.place(x=150,y=130)  
    enter_1 = Entry(frame)  
    enter_1.place(x=290,y=130)


    label_3= Label(frame,text="Last Name: ",width=20,font=("Verdana",10))
    label_3.place(x=150,y=160)
    enter_2 = Entry(frame)  
    enter_2.place(x=290,y=160)

  
    label_4 = Label(frame, text="Email: ", width=20,font=("Verdana",10))  
    label_4.place(x=150,y=220)  
    enter_3 = Entry(frame)  
    enter_3.place(x=290,y=220)  

    label_5 = Label(frame, text="Password: ", width=20,font=("Verdana",10))  
    label_5.place(x= 150,y=250)  
    enter_4 = Entry(frame)  
    enter_4.place(x=290,y=250)  

    label_6 = Label(frame, text="Repeat password: ", width=20,font=("Verdana",10))  
    label_6.place(x= 150,y=280)  
    enter_5 = Entry(frame)  
    enter_5.place(x=290,y=280)  

 
    submit_button= Button(frame, text='Submit',font = ("Helvetica",10) ,height = 1, width=20, bg="blue",fg='white')
    submit_button.place(x=240,y=450)  

    b2= Button(frame,text="Already have an account ? Login",padx=10,pady=5,command=clicklog)
    b2.place(x = 220, y = 510)


    frame.mainloop()


def routin():
    
    frame = Frame(win,width=1450,height=900, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    def eng():
        root = Tk()
        root.geometry("290x300")
        root.propagate(False)
        root.title("Class info")

        Teach_label = Label(root, text="Teacher : ",font = "Ariel")
        Teach_label.place(x = 20, y =20)

        Teach_Entry = Entry(root)
        Teach_Entry.place(x = 120, y =30)

        Class_label = Label(root, text="Class : ",font = "Ariel")
        Class_label.place(x = 20, y =50)

        Class_Entry = Entry(root)
        Class_Entry.place(x = 120, y =60)

    def comp():
        root = Tk()
        root.geometry("290x300")
        root.propagate(False)
        root.title("Class info")

        Teach_label = Label(root, text="Teacher : ",font = "Ariel")
        Teach_label.place(x = 20, y =20)

        Teach_Entry = Entry(root)
        Teach_Entry.place(x = 120, y =30)

        Class_label = Label(root, text="Class : ",font = "Ariel")
        Class_label.place(x = 20, y =50)

        Class_Entry = Entry(root)
        Class_Entry.place(x = 120, y =60)


    def maths():
        root = Tk()
        root.geometry("290x300")
        root.propagate(False)
        root.title("Class info")

        Teach_label = Label(root, text="Teacher : ",font = "Ariel")
        Teach_label.place(x = 20, y =20)

        Teach_Entry = Entry(root)
        Teach_Entry.place(x = 120, y =30)

        Class_label = Label(root, text="Class : ",font = "Ariel")
        Class_label.place(x = 20, y =50)

        Class_Entry = Entry(root)
        Class_Entry.place(x = 120, y =60)


    def clickback():
        frame.pack_forget()
        homepage()

    button = Button(frame, text = "Go back", font = ("heavitas",15), bg = "blue", fg = "white",command = clickback)
    button.place(x =0, y = 0)


    frame1 = Frame(frame,bg="black",width=1500,height=1500)
    frame1.pack(padx=200,pady=150)
    frame1.propagate(False)

    frame2 = Frame(frame1,bg="white",width=1500,height=1500)
    frame2.pack(pady=10,padx=10)
    frame2.propagate(False)


    frame3=Frame(frame2,bg="black",width=90,height=600)
    frame3.pack(padx=1,pady=1,side=LEFT)
    frame3.propagate(False)
    l8=Label(frame3,text="6AM",fg="black").pack(padx=30,pady=30)


    frame4=Frame(frame2,bg="grey",width=150,height=600)
    frame4.pack(padx=1,pady=1,side=LEFT)
    frame4.propagate(False)
    b= Button(frame4, text="English" ,font =("Arial Black",10),fg="black",command = eng)
    b.place(x=50,y=30)
    b= Button(frame4, text="Computer",font =("Arial Black",10),fg="black",command = comp)
    b.place(x=50,y=90)
    l7=Label(frame4,text="Sunday",fg="black").pack(padx=1,pady=1) 

    frame5=Frame(frame2,bg="grey",width=150,height=600)
    frame5.pack(padx=1,pady=1,side=LEFT)
    frame5.propagate(False)
    b= Button(frame5, text="English",font =("Arial Black",10),fg="black",command = eng)
    b.place(x=50,y=170)
    b= Button(frame5, text="Maths",font =("Arial Black",10),fg="black",command =maths)
    b.place(x=50,y=215)
    l1=Label(frame5,text="Monday",fg="black").pack(padx=1,pady=1)


    frame6=Frame(frame2,bg="grey",width=150,height=600)
    frame6.pack(padx=1,pady=1,side=LEFT)
    frame6.propagate(False)
    b= Button(frame6, text="English",font =("Arial Black",10),fg="black",command = eng)
    b.place(x=50,y=290)
    b= Button(frame6, text="Computer",font =("Arial Black",10),fg="black",command = comp)
    b.place(x=50,y=380)
    l2=Label(frame6,text="Tuesday",fg="black").pack(padx=1,pady=1)

    frame7=Frame(frame2,bg="grey",width=150,height=600)
    frame7.pack(padx=1,pady=1,side=LEFT)
    frame7.propagate(False)
    b= Button(frame7, text="Maths",font =("Arial Black",10),fg="black",command =maths)
    b.place(x=50,y=30)
    b= Button(frame7, text="Computer",font =("Arial Black",10),fg="black",command = comp)
    b.place(x=50,y=90)
    l3=Label(frame7,text="Wednesday",fg="black").pack(padx=1,pady=1)

    frame8=Frame(frame2,bg="grey",width=150,height=600)
    frame8.pack(padx=1,pady=1,side=LEFT)
    frame8.propagate(False)
    b= Button(frame8, text="Computer",font =("Arial Black",10),fg="black",command = comp)
    b.place(x=50,y=215)
    b= Button(frame8, text="Maths",font =("Arial Black",10),fg="black",command =maths)
    b.place(x=50,y=290)
    l4=Label(frame8,text="Thursday",fg="black").pack(padx=1,pady=1)

    frame9=Frame(frame2,bg="grey",width=150,height=600)
    frame9.pack(padx=1,pady=1,side=LEFT)
    frame9.propagate(False)
    b= Button(frame9, text="Maths",font =("Arial Black",10),fg="black",command =maths)
    b.place(x=50,y=90)
    b= Button(frame9, text="computer",font =("Arial Black",10),fg="black",command = comp)
    b.place(x=50,y=170)
    l5=Label(frame9,text="Friday",fg="black").pack(padx=1,pady=1)
    
    
    
    l9=Label(frame3,text="7AM",fg="black").pack(padx=10,pady=10)
    l10=Label(frame3,text="8AM",fg="black").pack(padx=10,pady=10)
    l11=Label(frame3,text="9AM",fg="black").pack(padx=10,pady=10)
    l12=Label(frame3,text="10AM",fg="black").pack(padx=10,pady=10)
    l13=Label(frame3,text="11AM",fg="black").pack(padx=10,pady=10)
    l14=Label(frame3,text="12PM",fg="black").pack(padx=10,pady=10)
    l15=Label(frame3,text="1PM",fg="black").pack(padx=10,pady=10)
    l16=Label(frame3,text="2PM",fg="black").pack(padx=10,pady=10)
    l17=Label(frame3,text="3PM",fg="black").pack(padx=10,pady=10)

    
def homepage():

    def clickrout():
        frame.pack_forget()
        routin()

    frame = Frame(win,width=800,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    my_label = Label(frame, image=reimg, borderwidth=0)
    my_label.place(x = 250, y = 100)

    
    routine = Button(frame, text = "Routine", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickrout)
    routine.place(x = 230, y = 420)

    students = Button(frame, text = "Students", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    students.place(x = 230, y = 490)

    result = Button(frame, text = "Result", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    result.place(x = 230, y = 560)

    acc_details = Button(frame, text = "Account", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    acc_details.place(x = 230, y = 630)
    

main()
