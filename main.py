from tkinter import *
from tkinter import messagebox
from tkextrafont import Font
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3



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
    my_label = Label(frame, image=reimg, borderwidth=0)
    my_label.place(x = 190, y = 150)
    teach = Button(frame, text = "REGISTER", width = 10, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command=framereg)
    teach.place(x = 240, y = 600)
    stu = Button(frame, text = "LOGIN", width = 10, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command=framelog)
    stu.place(x = 240, y = 530)

    win.mainloop()

def login():

    '''login page'''

    global clickhome
    global e
    global e2

    frame = Frame(win,width=1000,height=650, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    #create functions for buttons
    def clickreg():
        frame.pack_forget()
        reg()

    def clickhome():
        frame.pack_forget()
        homepage()

    #inserting labels, images and buttons
    my_label = Label(frame, image=restu, borderwidth=0)
    my_label.place(x = 70, y = 180)
    s = Label(frame, text = "Sign In", font = ("Microsoft Yahei UI light",23))
    s.place (x = 370, y = 20)
    l=Label(frame,text="Email",font = ("Helvetica",12))
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
    #function to hide and show the password
    def show():
        if(check.get()==1):
            e2.config(show='')
        else:
            e2.config(show='*')

    cb = Checkbutton(frame,variable = check,command = show)
    cb.place(x=600, y = 280)
    b= Button(frame, text="Log in",font=5,bg="blue", height = 1, width = 10,fg="white",command=login_check)
    b.place(x =620, y = 310)
    b2= Button(frame,text="Dont have an account ?Register",padx=10,pady=5,command=clickreg)
    b2.place(x = 580, y = 380)


def login_check():

    #creating a table for credentials
    def config():
        conn = sqlite3.connect('Students.db')
        c = conn.cursor()


        c.execute(""" CREATE TABLE creds(
            
            f_name text,
            l_name text,
            email text,
            password text,
            pass_rep text
            )""")
        print("table created successfully")
        conn.commit()
        conn.close()

    # Creates table if not created
    try: 
        config()
    except sqlite3.OperationalError:
        pass


    conn=sqlite3.connect('Students.db')
    c=conn.cursor()

    email=e.get()
    pwd=e2.get()

    if email=='' or pwd=='':        #checking if field is empty
        messagebox.showwarning(title="Field Empty", message="Cannot be left empty")

    else:   #checking the email and password
      conn = sqlite3.connect('Students.db')
      cursor = conn.execute('SELECT * from creds where EMAIL="%s" and PASSWORD="%s"'%(email,pwd))
      if cursor.fetchone():
       messagebox.showinfo(title="Welcome", message="Login Success")
       clickhome()
      else: #if email and password do not match
       messagebox.showinfo(title="Wrong Details", message="Email or password wrong")
       

    conn.commit()
    conn.close()






  
def reg():
 
    '''registration page'''

    global label_2
    global label_3
    global label_4
    global label_5
    global label_6

    def config():
    
        conn = sqlite3.connect('Students.db')
        c = conn.cursor()


        c.execute(""" CREATE TABLE creds(
            f_name text,
            l_name text,
            email text,
            password text,
            pass_rep text
            )""")
        print("table created successfully")
        conn.commit()
        conn.close()

    try: # Creates table if not created
        config()
    except sqlite3.OperationalError:
        pass


    frame = Frame(win,width=650,height=650, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=100)
    frame.pack_propagate(False)

    def clicklog():
        frame.pack_forget()
        login()
    
    def submit():   

        '''
        entering all data into the database
        '''

        global uid

        f_name=enter_1.get()
        l_name=enter_2.get()
        email=enter_3.get()
        p = enter_4.get()
        re_p = enter_5.get()
        if f_name=='' or l_name=='' or email=='' or p=='' or re_p=='':  #checking for emply fields
            messagebox.showwarning(title="Field Empty", message="Cannot be left empty")
        elif p != re_p:
            messagebox.showinfo("Pasword not matched","Passwords do not match")
        else:

            conn= sqlite3.connect('Students.db')

            c= conn.cursor()

            c.execute("INSERT INTO creds VALUES (:f_name, :l_name, :email, :password, :pass_rep)",{
                'f_name':enter_1.get(),
                'l_name':enter_2.get(),
                'email':enter_3.get(),
                'password':enter_4.get(),
                'pass_rep': enter_5.get(),

                })
            uid = c.lastrowid

            messagebox.showinfo("creds","Inserted Sucessfully")
            conn.commit()
            conn.close()
            messagebox.showinfo('Success', f'New user created with ID {uid}')

            enter_1.delete(0,END)
            enter_2.delete(0,END)
            enter_3.delete(0,END)
            enter_4.delete(0,END)
            enter_5.delete(0,END)

    
    #inserting labels, images and Buttons 

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
    check=IntVar(value=0)
    e_str = StringVar()
    enter_4 = Entry(frame,show = "*",textvariable=e_str)  
    enter_4.place(x=290,y=250) 
    
     
    def show():
        if(check.get()==1):
            enter_4.config(show='')
        else:
            enter_4.config(show='*')
        

    cb = Checkbutton(frame,variable = check,command = show)
    cb.place(x=430, y = 250)

    label_6 = Label(frame, text="Repeat password: ", width=20,font=("Verdana",10))  
    label_6.place(x= 150,y=280)
    check1=IntVar(value=0)
    e1_str = StringVar()  
    enter_5 = Entry(frame,show = "*",textvariable=e1_str)  
    enter_5.place(x=290,y=280)  
     
    def show():
        if(check1.get()==1):
            enter_5.config(show='')
        else:
            enter_5.config(show='*')
        

    cb2 = Checkbutton(frame,variable = check1,command = show)
    cb2.place(x=430, y = 280)


 
    submit_button= Button(frame, text='Submit',font = ("Helvetica",10) ,height = 1, width=20, bg="blue",fg='white',command =submit)
    submit_button.place(x=240,y=450)  

    b2= Button(frame,text="Already have an account ? Login",padx=10,pady=5,command=clicklog)
    b2.place(x = 220, y = 510)


    frame.mainloop()


    

def routin():

    '''routine'''

    def clickback():
        frame.pack_forget()
        homepage()

    def clicksecA():
        frame.pack_forget()
        secA()


    def clicksecB():
        frame.pack_forget()
        secB()


    frame = Frame(win,width=700,height=600, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    button = Button(frame, text = "Go back", font = ("heavitas",15), bg = "blue", fg = "white",command = clickback)
    button.place(x =0, y = 0)

    lable = Label(frame, text = "Routine of :", font=("heavitas",30))
    lable.place(x =150, y= 150)

    def secA():

        '''
        routine for section A
        '''

        def clickback():
            frame.pack_forget()
            routin()

        #creating the routine 

        frame = Frame(win,width=1450,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
        frame.pack(padx=20, pady=20)
        frame.pack_propagate(False)

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
        b= Button(frame4, text="English" ,font =("Arial Black",10),fg="black")
        b.place(x=50,y=30)
        b= Button(frame4, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=90)
        l7=Label(frame4,text="Sunday",fg="black").pack(padx=1,pady=1) 

        frame5=Frame(frame2,bg="grey",width=150,height=600)
        frame5.pack(padx=1,pady=1,side=LEFT)
        frame5.propagate(False)
        b= Button(frame5, text="English",font =("Arial Black",10),fg="black")
        b.place(x=50,y=170)
        b= Button(frame5, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=215)
        l1=Label(frame5,text="Monday",fg="black").pack(padx=1,pady=1)


        frame6=Frame(frame2,bg="grey",width=150,height=600)
        frame6.pack(padx=1,pady=1,side=LEFT)
        frame6.propagate(False)
        b= Button(frame6, text="English",font =("Arial Black",10),fg="black")
        b.place(x=50,y=290)
        b= Button(frame6, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=380)
        l2=Label(frame6,text="Tuesday",fg="black").pack(padx=1,pady=1)

        frame7=Frame(frame2,bg="grey",width=150,height=600)
        frame7.pack(padx=1,pady=1,side=LEFT)
        frame7.propagate(False)
        b= Button(frame7, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=30)
        b= Button(frame7, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=90)
        l3=Label(frame7,text="Wednesday",fg="black").pack(padx=1,pady=1)

        frame8=Frame(frame2,bg="grey",width=150,height=600)
        frame8.pack(padx=1,pady=1,side=LEFT)
        frame8.propagate(False)
        b= Button(frame8, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=215)
        b= Button(frame8, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=290)
        l4=Label(frame8,text="Thursday",fg="black").pack(padx=1,pady=1)

        frame9=Frame(frame2,bg="grey",width=150,height=600)
        frame9.pack(padx=1,pady=1,side=LEFT)
        frame9.propagate(False)
        b= Button(frame9, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=90)
        b= Button(frame9, text="computer",font =("Arial Black",10),fg="black")
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

    def secB():

        '''
        routine for section B
        '''

        def clickback():
            frame.pack_forget()
            routin()

        frame = Frame(win,width=1450,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
        frame.pack(padx=20, pady=20)
        frame.pack_propagate(False)

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
        b= Button(frame4, text="English" ,font =("Arial Black",10),fg="black")
        b.place(x=50,y=290)
        b= Button(frame4, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=215)
        l7=Label(frame4,text="Sunday",fg="black").pack(padx=1,pady=1) 

        frame5=Frame(frame2,bg="grey",width=150,height=600)
        frame5.pack(padx=1,pady=1,side=LEFT)
        frame5.propagate(False)
        b= Button(frame5, text="English",font =("Arial Black",10),fg="black")
        b.place(x=50,y=290)
        b= Button(frame5, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=380)
        l1=Label(frame5,text="Monday",fg="black").pack(padx=1,pady=1)


        frame6=Frame(frame2,bg="grey",width=150,height=600)
        frame6.pack(padx=1,pady=1,side=LEFT)
        frame6.propagate(False)
        b= Button(frame6, text="English",font =("Arial Black",10),fg="black")
        b.place(x=50,y=30)
        b= Button(frame6, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=125)
        l2=Label(frame6,text="Tuesday",fg="black").pack(padx=1,pady=1)

        frame7=Frame(frame2,bg="grey",width=150,height=600)
        frame7.pack(padx=1,pady=1,side=LEFT)
        frame7.propagate(False)
        b= Button(frame7, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=125)
        b= Button(frame7, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=170)
        l3=Label(frame7,text="Wednesday",fg="black").pack(padx=1,pady=1)

        frame8=Frame(frame2,bg="grey",width=150,height=600)
        frame8.pack(padx=1,pady=1,side=LEFT)
        frame8.propagate(False)
        b= Button(frame8, text="Computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=30)
        b= Button(frame8, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=125)
        l4=Label(frame8,text="Thursday",fg="black").pack(padx=1,pady=1)

        frame9=Frame(frame2,bg="grey",width=150,height=600)
        frame9.pack(padx=1,pady=1,side=LEFT)
        frame9.propagate(False)
        b= Button(frame9, text="Maths",font =("Arial Black",10),fg="black")
        b.place(x=50,y=290)
        b= Button(frame9, text="computer",font =("Arial Black",10),fg="black")
        b.place(x=50,y=380)
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

    
    button = Button(frame, text = "Section A", font = ("heavitas",25), bg = "white",command = clicksecA)
    button.place(x =200, y = 250)

    button = Button(frame, text = "Section B", font = ("heavitas",25), bg = "white",command = clicksecB)
    button.place(x =200, y = 350)



def homepage():

    '''
    homepage
    '''

    def clickrout():
        frame.pack_forget()
        routin()


    def clickstu():
        frame.pack_forget()
        database()

    def clickfee():
        frame.pack_forget()
        fees()

    def clickacc():
        frame.pack_forget()
        account()
        

    frame = Frame(win,width=800,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

   

    my_label = Label(frame, image=reimg, borderwidth=0)
    my_label.place(x = 250, y = 90)


    rout = Button(frame, text = "ROUTINE", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickrout)
    rout.place(x = 230, y = 420)
    
    students = Button(frame, text = "Students", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickstu)
    students.place(x = 230, y = 490)

    result = Button(frame, text = "Fees", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickfee)
    result.place(x = 230, y = 560)

    acc_details = Button(frame, text = "Account", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickacc)
    acc_details.place(x = 230, y = 630)
    
def database():

    '''
    the student page where we can view, insert, edit and delete student data
    '''

    def clickback():
        frame.pack_forget()
        homepage()

        
    frame = Frame(win,width=1350,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    button = Button(frame, text = "Go back", font = ("heavitas",15), bg = "blue", fg = "white",command = clickback)
    button.place(x =0, y = 0)


            
    Frame1=Frame(frame,bd=4,relief=RIDGE,bg="grey")
    Frame1.place(x=20,y=100,width=450,height=590)

    #==== Frame 1 ================

    Frame1=Frame(frame,bd=4,relief=RIDGE,bg="grey")
    Frame1.place(x=20,y=100,width=450,height=590)

    title1= Label(Frame1,text="Manage Students Info",bd=10,relief=GROOVE,fg="white",font=("times new roman",20,"bold"),bg="red")
    title1.grid(row=0,columnspan=2,pady=20)

    # create a text box and label ---- 

    label_name= Label(Frame1,text="Student Name: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_name.grid(row=1,column=0,pady=10,padx=20,sticky="w")

    text_name= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_name.grid(row=1,column=1,pady=10,padx=20,sticky="w")

    label_roll= Label(Frame1,text="Roll No: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_roll.grid(row=2,column=0,pady=10,padx=20,sticky="w")

    text_roll= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_roll.grid(row=2,column=1,pady=10,padx=20,sticky="w")

    label_gender= Label(Frame1,text="Gender: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_gender.grid(row=3,column=0,pady=10,padx=20,sticky="w")

    text_gender= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_gender.grid(row=3,column=1,pady=10,padx=20,sticky="w")

    combo_gender= ttk.Combobox(Frame1,font=("times new roman",13,"bold"),state="readonly")
    combo_gender['values']=("Male","Female")
    combo_gender.grid(row=3,column=1,padx=20,pady=10)

    label_section= Label(Frame1,text="Section: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_section.grid(row=4,column=0,pady=10,padx=20,sticky="w")

    text_section= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_section.grid(row=4,column=1,pady=10,padx=20,sticky="w")

    label_subject= Label(Frame1,text="Subject: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_subject.grid(row=5,column=0,pady=10,padx=20,sticky="w")

    text_subject= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_subject.grid(row=5,column=1,pady=10,padx=20,sticky="w")

    combo_total_subject= ttk.Combobox(Frame1,font=("times new roman",13,"bold"),state="readonly")
    combo_total_subject['values']=("Science","Maths","English","Nepali","Social","Computer")
    combo_total_subject.grid(row=5,column=1,padx=20,pady=10)

    label_obt_marks= Label(Frame1,text="Obtain Marks: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_obt_marks.grid(row=6,column=0,pady=10,padx=20,sticky="w")

    text_obt_marks= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_obt_marks.grid(row=6,column=1,pady=10,padx=20,sticky="w")

    label_total_marks= Label(Frame1,text="Total Marks: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    label_total_marks.grid(row=7,column=0,pady=10,padx=20,sticky="w")

    text_total_marks= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    text_total_marks.grid(row=7,column=1,pady=10,padx=20,sticky="w")

    combo_total_marks= ttk.Combobox(Frame1,font=("times new roman",13,"bold"),state="readonly")
    combo_total_marks['values']=("75","100")
    combo_total_marks.grid(row=7,column=1,padx=20,pady=10)

    delete_box_lable= Label(Frame1,text="ID Number: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
    delete_box_lable.grid(row=8,column=0,pady=10,padx=20,sticky="w")

    delete_box= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    delete_box.grid(row=8,column=1,pady=10,padx=20,sticky="w")

    #==== Frame 2 ================

    Frame2=Frame(frame,bd=4,relief=RIDGE,bg="grey")
    Frame2.place(x=500,y=100,width=800,height=590)



    # Creating a data table =============
    def config():
        conn=sqlite3.connect('Students.db')
        c=conn.cursor()

        c.execute(""" CREATE TABLE student(
            StudentName text,
            RollNo integer PRIMARY KEY,
            Gender text,
            Section text,
            Subject text,
            ObtMarks integer,
            FinalMarks integer
            )""")
        print("database created successfully")
        conn.commit()
        conn.close()

    try:# Creates table if not made
        config()
    except sqlite3.OperationalError:
        pass

    def initialize():
        global frame,text_name,text_roll,combo_gender,text_section,text_subject,text_obt_marks,text_total_marks



    # update function -------------
    def UPDATE():
        conn= sqlite3.connect('Students.db')
        c= conn.cursor()
        record_id= delete_box.get()

        c.execute(""" UPDATE student SET 
            StudentName = :StudentName,
            RollNo = :RollNo,
            Gender = :Gender,
            Section = :Section,
            Subject = :Subject,
            ObtMarks = :ObtMarks,
            FinalMarks= :FinalMarks

            WHERE oid = :oid""",
            {
            'StudentName': text_name_editior.get(),
            'RollNo': text_roll_editior.get(),
            'Gender': combo_gender_editior.get(),
            'Section': text_section_editior.get(),
            'Subject': combo_total_subject_editior.get(),
            'ObtMarks': text_obt_marks_editior.get(),    
            'FinalMarks': combo_total_marks_editior.get(),

            'oid':  record_id

            })

        conn.commit()
        conn.close()
        editor.destroy()

    def EDIT():

        global editor

        editor= Toplevel()
        editor.title('Update Data')
        editor.geometry("1350x700+0+0")



        conn= sqlite3.connect('Students.db')

        c= conn.cursor()

        record_id= delete_box.get()

        c.execute("SELECT * FROM student WHERE oid = " + record_id)

        records= c.fetchall()

        global Frame1
        global text_name_editior
        global text_roll_editior
        global text_obt_marks_editior
        global text_section_editior
        global combo_total_subject_editior
        global combo_gender_editior
        global combo_total_marks_editior
        
        Frame1=Frame(editor,bd=4,relief=RIDGE,bg="grey")
        Frame1.place(x=430,y=90,width=600,height=590)

        title1= Label(Frame1,text="Update Students",bd=10,relief=GROOVE,fg="white",font=("times new roman",20,"bold"),bg="red")
        title1.grid(row=0,column=1,columnspan=3,pady=20,padx=10)

        label_name_editior= Label(Frame1,text="Student Name: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_name_editior.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        text_name_editior= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_name_editior.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        label_roll_editior= Label(Frame1,text="Roll No: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_roll_editior.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        text_roll_editior= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_roll_editior.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        label_gender_editior= Label(Frame1,text="Gender: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_gender_editior.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        combo_gender_editior= ttk.Combobox(Frame1,font=("times new roman",14,"bold"),state="readonly")
        combo_gender_editior['values']=("Male","Female")
        combo_gender_editior.grid(row=3,column=1)

        label_section_editior= Label(Frame1,text="Section: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_section_editior.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        text_section_editior= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_section_editior.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        label_subject_editior= Label(Frame1,text="Subject: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_subject_editior.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        combo_total_subject_editior= ttk.Combobox(Frame1,font=("times new roman",14,"bold"),state="readonly")
        combo_total_subject_editior['values']=("Science","Maths","English","Nepali","Social","Computer")
        combo_total_subject_editior.grid(row=5,column=1)

        label_obt_marks_editior= Label(Frame1,text="Obtain Marks: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_obt_marks_editior.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        text_obt_marks_editior= Entry(Frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_obt_marks_editior.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        label_total_marks_editior= Label(Frame1,text="Total Marks: ",bg="grey",fg="white",font=("times new roman",15,"bold"))
        label_total_marks_editior.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        combo_total_marks_editior= ttk.Combobox(Frame1,font=("times new roman",14,"bold"),state="readonly")
        combo_total_marks_editior['values']=("75","100")
        combo_total_marks_editior.grid(row=7,column=1)

        
    #  loop through result ------- 
        for record in records:
            text_name_editior.insert(0, record[0])
            text_roll_editior.insert(0, record[1])
            combo_gender_editior.set(record[2])
            text_section_editior.insert(0, record[3])
            combo_total_subject_editior.set(record[4])
            text_obt_marks_editior.insert(0, record[5])
            combo_total_marks_editior.set(record[6])

        Updatebttm_editior= Button(Frame1,text="SAVE",command= UPDATE ,width=10)
        Updatebttm_editior.grid(row=9,column=1,padx=10,pady=10)

        conn.commit()
        conn.close()
        



    #  DELETE function ------------

    def DELETE():
        conn= sqlite3.connect('Students.db')

        c= conn.cursor()

        c.execute("DELETE from student WHERE oid =  " + delete_box.get())
        print('Delete Sucessfully')

        delete_box.delete(0,END)

        records= c.fetchall()
        print(records)

        print_record=''
        for record in records:
            print_record += str(record[0])+'  '+str(record[1])+'  '+str(record[2])+'  '+str(record[3])+'  '+str(record[4])+'  '+str(record[5])+'  '+str(record[6])+"\n"

        query_label= Label(student_table,text= print_record)
        query_label.grid(row=8, column=0,rowspan=2 ,columnspan=20)

        messagebox.showinfo("Alert","Deleted Sucessfully")

        conn.commit()
        conn.close()

    # ADD function --------------
        
    def ADD():

        try:
            conn=sqlite3.connect('Students.db')
            c=conn.cursor()
            
            c.execute('INSERT INTO student VALUES (:StudentName, :RollNo, :Gender, :Section, :Subject,  :ObtMarks, :FinalMarks)',
                {
                'StudentName': text_name.get(),
                'RollNo': text_roll.get(),
                'Gender': combo_gender.get(),
                'Section': text_section.get(),
                'Subject': combo_total_subject.get(),
                'ObtMarks': text_obt_marks.get(),
                'FinalMarks': combo_total_marks.get()
                
                })
            # print('data submitted successfully')

            text_name.delete(0,END)
            text_roll.delete(0,END)
            combo_gender.set('')
            combo_total_subject.set('')
            text_section.delete(0,END)
            text_obt_marks.delete(0,END)
            combo_total_marks.set('')

            messagebox.showinfo("Alert","Added Sucessfully")



            conn.commit()
            conn.close()

        except sqlite3.IntegrityError:
            messagebox.showinfo("Alert","Incomplete or Wrong Data")

        
            

    # SHOW query ------------

    def QUERY():
        conn = sqlite3.connect("Students.db")

        for i in student_table.get_children():
            student_table.delete(i)

        cursor = conn.execute("SELECT * FROM student")
        for row in cursor:
            student_table.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4] ,row[5] ,row[6]))


        conn.commit()
        conn.close()

    
    # Button frame ---------------

    bttm_Frame1=Frame(Frame2,bd=4,bg="grey")
    bttm_Frame1.place(x=20,y=0,width=420)

    Addbttm= Button(bttm_Frame1,text="ADD",width=10,command=ADD).grid(row=0,column=0,padx=10,pady=10)
    Updatebttm= Button(bttm_Frame1,text="EDIT",width=10,command=EDIT).grid(row=0,column=1,padx=10,pady=10)
    Deletebttm= Button(bttm_Frame1,text="DELETE",width=10,command=DELETE).grid(row=0,column=2,padx=10,pady=10)
    querybttm= Button(bttm_Frame1,text="SHOW",width=10,command=QUERY).grid(row=0,column=3,pady=10,padx=10)
 

    # Table frame ---------------

    table_frame= Frame(Frame2,bd=4, relief=RIDGE,bg="white")
    table_frame.place(x=10,y=70,width=770,height=500)

    # scroll -------------------

    scroll_x= Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y= Scrollbar(table_frame,orient=VERTICAL)


    # student_table-----------   

    student_table= ttk.Treeview(table_frame,columns=("StudentName","RollNo","Gender","Section","Subject","ObtainMarks","FinalMarks"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)
    student_table["columns"] = ("StudentName", "RollNo", "Gender","Section","Subject","ObtainMarks","FinalMarks")
    student_table.heading("StudentName",text="StudentName")
    student_table.heading("RollNo",text="RollNo")
    student_table.heading("Gender",text="Gender")
    student_table.heading("Section",text="Section")
    student_table.heading("Subject",text="Subject")
    student_table.heading("ObtainMarks",text="ObtainMarks")
    student_table.heading("FinalMarks",text="FinalMarks")
    student_table['show']='headings'
    student_table.column("StudentName",width=100)
    student_table.column("RollNo",width=50)
    student_table.column("Gender",width=50)
    student_table.column("Section",width=50)
    student_table.column("Subject",width=50)
    student_table.column("ObtainMarks",width=100)
    student_table.column("FinalMarks",width=100)
    student_table.pack(fill=BOTH,expand=1)


def account():

    '''
    the account page where account details can be updated
    '''


    def clickback():
        frame.pack_forget()
        homepage()


    frame = Frame(win,width=600,height=400, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.place(x=500, y=200)
    frame.propagate(False)

    button = Button(frame, text = "Go back", font = ("heavitas",15), bg = "blue", fg = "white",command = clickback)
    button.place(x =0, y = 0)

    label = Label(frame, text = "Enter Your ID number:", font=("Heavitas",15))
    label.place(x = 100, y = 90)

    box = Entry(frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    box.place(x = 180, y = 140)

    


    def UPDATE():
        conn= sqlite3.connect('Students.db')
        c= conn.cursor()
        record_id= box.get()

        c.execute(""" UPDATE creds SET 
            f_name = :fname,
            l_name = :lname,
            email = :email,
            password = :pass,
            pass_rep = :repass

            WHERE oid = :oid""",
            {
            'fname': enter_1.get(),
            'lname': enter_2.get(),
            'email': enter_3.get(),
            'pass': enter_4.get(),
            'repass': enter_5.get(),

            'oid':  record_id

            })

        conn.commit()
        conn.close()
        editor.destroy()

    def EDIT():

        global editor

        editor= Toplevel()
        editor.title('Update Data')
        editor.geometry("610x600")



        conn= sqlite3.connect('Students.db')

        c= conn.cursor()

        record_id= box.get()

        c.execute("SELECT * FROM creds WHERE oid = " + record_id)

        records= c.fetchall()

        global Frame1
        global enter_1
        global enter_2
        global enter_3
        global enter_4
        global enter_5
        
        Frame1=Frame(editor,bd=4,relief=RIDGE)
        Frame1.place(x=0,y = 0,width=600,height=590)

        title1= Label(Frame1,text="Update Profile",bd=10,relief=GROOVE,fg="white",font=("times new roman",20,"bold"),bg="red")
        title1.place(x = 190, y =10)


        label_2 =Label(Frame1, text= "First Name: ", width=20,font=("Verdana",10))  
        label_2.place(x=150,y=130)  
        enter_1 = Entry(Frame1)  
        enter_1.place(x=290,y=130)


        label_3= Label(Frame1,text="Last Name: ",width=20,font=("Verdana",10))
        label_3.place(x=150,y=160)
        enter_2 = Entry(Frame1)  
        enter_2.place(x=290,y=160)

    
        label_4 = Label(Frame1, text="Email: ", width=20,font=("Verdana",10))  
        label_4.place(x=150,y=220)  
        enter_3 = Entry(Frame1)  
        enter_3.place(x=290,y=220)  

        label_5 = Label(Frame1, text="Password: ", width=20,font=("Verdana",10))  
        label_5.place(x= 150,y=250)  
        check=IntVar(value=0)
        e_str = StringVar()
        enter_4 = Entry(Frame1,show = "*",textvariable=e_str)  
        enter_4.place(x=290,y=250) 
        
        
        def show():
            if(check.get()==1):
                enter_4.config(show='')
            else:
                enter_4.config(show='*')
            

        cb = Checkbutton(Frame1,variable = check,command = show)
        cb.place(x=430, y = 250)

        label_6 = Label(Frame1, text="Confirm password: ", width=20,font=("Verdana",10))  
        label_6.place(x= 150,y=280)
        check1=IntVar(value=0)
        e1_str = StringVar()  
        enter_5 = Entry(Frame1,show = "*",textvariable=e1_str)  
        enter_5.place(x=290,y=280)  
        
        def show():
            if(check1.get()==1):
                enter_5.config(show='')
            else:
                enter_5.config(show='*')
            

        cb2 = Checkbutton(Frame1,variable = check1,command = show)
        cb2.place(x=430, y = 280)
   
        submit_button= Button(Frame1, text='Update',font = ("Helvetica",10) ,height = 1, width=20, bg="blue",fg='white',command =UPDATE)
        submit_button.place(x=240,y=450)  

        
    #  loop through result ------- 
        for record in records:
            enter_1.insert(0, record[0])
            enter_2.insert(0, record[1])
            enter_3.insert(0, record[2])
            enter_4.insert(0, record[3])
            enter_5.insert(0, record[4])
            
        conn.commit()
        conn.close()
    button2 = Button(frame, text = "OK", font = ("heavitas",15), bg = "blue", fg = "white",command=EDIT)
    button2.place(x =240, y = 190)
        
    


    




def fees():

    '''where fees are calculated'''
    
    def clickback():
        frame.pack_forget()
        homepage()


    frame = Frame(win,width=600,height=400, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.place(x=500, y=200)
    frame.propagate(False)

    button = Button(frame, text = "Go back", font = ("heavitas",15), bg = "blue", fg = "white",command = clickback)
    button.place(x =0, y = 0)

    label = Label(frame, text = "Enter Student Roll Number:", font=("Heavitas",15))
    label.place(x = 100, y = 90)

    enter = Entry(frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    enter.place(x = 180, y = 140)

    

    def fe():
        root = Tk()
        root.config(bg="grey")
        root.geometry("400x400")
        root.title("Fee detail")




        Fee = Label(root,text = "Fee",font=("times new roman ",20,"bold"),bg = "red",bd=10,relief=GROOVE)
        Fee.pack()
        fee_entry = Entry(root)
        fee_entry.pack(pady=20)
        fee_entry.insert(0,"200000")

        fee_paid = Label(root,text = "Fee paid",font=("times new roman ",20,"bold"),bg = "red",bd=10,relief=GROOVE)
        fee_paid.pack(pady=20)

        fee_paid_entry = Entry(root,width=20)
        fee_paid_entry.pack(pady=20)

        def prepaid():


            num2 = 200000
            num1 = int(fee_paid_entry.get())
            total = num2-num1
            showvalue.set(total)
            fee_due_result.insert(0,total)

        fee_due = Button(root,text="Fee Due",font = ("times new roman ",15,"bold"),bg = "lightgreen",bd=10,relief=GROOVE,command=prepaid)
        fee_due.pack(pady=20)



        showvalue = StringVar()

        fee_due_result = Entry(root,textvariable=showvalue)
        fee_due_result.pack()

        root.mainloop()

    button_submit = Button(frame, text = "Submit", font = ("heavitas",15), bg = "blue", fg = "white",command = fe)
    button_submit.place(x =200, y = 180)
    






if __name__ == "__main__":
    main()
