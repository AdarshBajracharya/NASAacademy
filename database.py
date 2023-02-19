
import sqlite3
from tkinter import messagebox
from tkextrafont import Font
from tkinter import *
import tkinter as ttk
import main

def databas():

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
            'Subject': combo_total_subject.get(),
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
                'FinalMarks': text_total_marks.get()
                
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
            student_table.insert(parent='', index='end', values=(row[0], row[1], row[2],row[3],row[4],row[5],row[6]))


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

