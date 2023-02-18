from tkinter import *
from tkinter import messagebox
from tkextrafont import Font
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3
# import creds
# import database


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

    def clickstu():
        frame.pack_forget()
        database()
        

    frame = Frame(win,width=800,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

   

    my_label = Label(frame, image=reimg, borderwidth=0)
    my_label.place(x = 250, y = 70)

    
    routine = Button(frame, text = "Routine", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickrout)
    routine.place(x = 230, y = 420)

    students = Button(frame, text = "Students", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white",command = clickstu)
    students.place(x = 230, y = 490)

    result = Button(frame, text = "NOTICE", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    result.place(x = 230, y = 560)

    acc_details = Button(frame, text = "Account", width = 15, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    acc_details.place(x = 230, y = 630)
    
def database():

    def clickback():
        frame.pack_forget()
        homepage()

    
    frame = Frame(win,width=1350,height=800, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    button = Button(frame, text = "Go back", font = ("heavitas",15), bg = "blue", fg = "white",command = clickback)
    button.place(x =0, y = 0)

#==== Frame 1 ================

    Frame1=Frame(root,bd=4,relief=RIDGE,bg="grey")
    Frame1.place(x=20,y=100,width=450,height=590)

    title1= Label(Frame1,text="Manage Students Result",bd=10,relief=GROOVE,fg="white",font=("times new roman",20,"bold"),bg="red")
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

    Frame2=Frame(root,bd=4,relief=RIDGE,bg="grey")
    Frame2.place(x=500,y=100,width=800,height=590)

    lbl_search=Label(Frame2,text="Search By: ",bg="grey",fg="white",font=("times new roman",20,"bold"))
    lbl_search.grid(row=0,column=0,padx=20,pady=20,sticky="w")

    combo_search= ttk.Combobox(Frame2,width=15,font=("times new roman",13,"bold"),state="readonly")
    combo_search['values']=("Roll No","StudentName")
    combo_search.grid(row=0,column=1,padx=20,pady=10)

    text_Search= Entry(Frame2,width=15,font=("times new roman",15,"bold"),bd=5)
    text_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

    # Creating a data table =============

    conn=sqlite3.connect('Students.db')
    c=conn.cursor()

    # c.execute(""" CREATE TABLE student(
    #     StudentName text,
    #     RollNo integer PRIMARY KEY,
    #     Gender text,
    #     Section text,
    #     Subject text,
    #     ObtMarks integer,
    #     FinalMarks integer
    #     )""")
    # print("database created successfully")
    conn.commit()
    conn.close()

    def initialize():
            global root,text_name,text_roll,combo_gender,text_section,text_subject,text_obt_marks,text_total_marks

    # update function -------------

    def EDIT():

        editor= Toplevel()
        editor.title('Update Data')
        editor.geometry("1350x700+0+0")

        conn= sqlite3.connect('Students.db')

        c= conn.cursor()

        record_id= delete_box.get()

        c.execute("SELECT * FROM student WHERE oid = " + record_id)

        records= c.fetchall()

        
        Frame1=Frame(editor,bd=4,relief=RIDGE,bg="grey")
        Frame1.place(x=430,y=90,width=600,height=590)

        title1= Label(Frame1,text="Update Students Result",bd=10,relief=GROOVE,fg="white",font=("times new roman",20,"bold"),bg="red")
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
            combo_gender_editior.insert(0, record[2])
            text_section_editior.insert(0, record[3])
            combo_total_subject_editior.insert(0, record[4])
            text_obt_marks_editior.insert(0, record[5])
            combo_total_marks_editior.insert(0, record[6])

        Updatebttm_editior= Button(Frame1,text="SAVE",command= SAVE ,width=10)
        Updatebttm_editior.grid(row=9,column=1,padx=10,pady=10)


    # SAVE function ----------

    def SAVE():
        print("save")


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
            print_record += str(record[0])+' '+str(record[1])+' '+str(record[2])+' '+str(record[3])+' '+str(record[4])+' '+str(record[5])+' '+str(record[6])+"\n"

        query_label= Label(student_table,text= print_record)
        query_label.grid(row=8, column=0,rowspan=2 ,columnspan=20)

        messagebox.showinfo("Alert","Deleted Sucessfully")

        conn.commit()
        conn.close()

    # ADD function --------------
        
    def ADD():
        conn=sqlite3.connect('Students.db')
        c=conn.cursor()
        
        c.execute('INSERT INTO student VALUES (:StudentName, :RollNo, :Gender, :Section, :Subject,  :ObtMarks, :FinalMarks)',
            {
            'StudentName': text_name.get(),
            'RollNo': text_roll.get(),
            'Gender': combo_gender.get(),
            'Section': text_section.get(),
            'Subject': text_subject.get(),
            'ObtMarks': text_obt_marks.get(),
            'FinalMarks': text_total_marks.get()
            
            })
        # print('data submitted successfully')

        text_name.delete(0,END)
        text_roll.delete(0,END)
        combo_gender.delete(0,END)
        text_subject.delete(0,END)
        text_section.delete(0,END)
        text_obt_marks.delete(0,END)
        text_total_marks.delete(0,END)

        messagebox.showinfo("Alert","Added Sucessfully")
        
        conn.commit()

        conn.close()

    # SHOW query ------------

    def QUERY():

        conn= sqlite3.connect('Students.db')

        c= conn.cursor()

        c.execute("SELECT *, oid FROM student")

        records= c.fetchall()
        print(records)

        print_record=' '
        for record in records:
            print_record += str(record[0])+ "  "+"\t"+" " +str(record[1])+ "  "+"\t"+" " +str(record[2])+" "+"\t"+ " "+str(record[3])+ " "+ "\t" +" "+str(record[6])+"\n"

        query_label= Label(student_table,text= print_record)
        query_label.grid(row=1,column=4,padx=10,pady=30)

        conn.commit()
        conn.close()



    
    # Button frame ---------------

    bttm_Frame1=Frame(Frame1,bd=4,bg="grey")
    bttm_Frame1.place(x=15,y=530,width=400, height=50)



    Addbttm= Button(bttm_Frame1,text="ADD",command=ADD).grid(row=3,column=0,padx=20,pady=20)
    Updatebttm= Button(bttm_Frame1,text="UPDATE",command=EDIT).grid(row=3,column=1,padx=20,pady=20)
    querybttm= Button(bttm_Frame1,text="SHOW",command=QUERY).grid(row=3,column=2,padx=20,pady=20)
    Deletebttm= Button(bttm_Frame1,text="DELETE",command=DELETE).grid(row=3,column=3,padx=20,pady=20)
    Searchbttm= Button(Frame2,text="SEARCH",command=QUERY).grid(row=0,column=3,padx=10,pady=20)


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
    student_table.heading("StudentName",text="StudentName")
    student_table.heading("RollNo",text="RollNo")
    student_table.heading("Gender",text="Gender")
    student_table.heading("Section",text="Section")
    student_table.heading("Subject",text="Subject")
    student_table.heading("ObtainMarks",text="ObtainMarks")
    student_table.heading("FinalMarks",text="FinalMarks")
    student_table['show']='headings'
    student_table.pack(fill=BOTH,expand=1)


    try:# Creates tables for new host machine.
        config()
    except sqlite3.OperationalError:
        pass


if __name__ == "__main__":
    main()
