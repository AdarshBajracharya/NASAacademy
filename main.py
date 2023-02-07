from tkinter import *
from PIL import Image, ImageTk
from tkextrafont import Font
import customtkinter


def stutea():
    #Creating window
    win = customtkinter.CTk()
    win.title("NASA Academy")
    win.iconbitmap("images/cap.ico")
    win.geometry("1920x1080")

    #Setting background image
    bg = customtkinter.CTkImage(Image.open("images\\sbac.jpg"), size = (1550, 800))
    label1 = customtkinter.CTkLabel(win, image = bg)
    label1.place(x = 0, y = 0)
    
    #Creating frame
    frame = customtkinter.CTkFrame(win,width=700,height=700, corner_radius=30, border_color="black", border_width=1)
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    #Inserting font
    he = Font(file="fonts\Heavitas.ttf", family="Heavitas")

    #Creating Labels, buttons and inserting images
    top = Label(frame, text = "Welcome  to", font = ("Heavitas", 15),bg="#d9d9d9")
    top.pack(padx= 0, pady = 40)
    top2 = Label(frame, text = "NASA ACADEMY", font = ("heavitas", 30),bg="#d9d9d9")
    top2.place(x= 250, y = 67)
    my_image = ImageTk.PhotoImage(file ="images/wlogo.png")                 
    my_label = Label(frame, image=my_image, borderwidth=0)
    my_label.pack(padx= 5, pady= 50)
    im = Label(frame, text = " I am a..", font = ("Bahnschrift", 20), background="#d9d9d9")
    im.place(x= 390 ,y =525)
    teach = customtkinter.CTkButton(frame, text = "Teacher",text_color="black", corner_radius= 20, width = 200, height=65, font =("Arial black", 20), command =loginteach, fg_color="white",border_color="black", border_width=3, hover_color="grey")
    teach.place(x = 250, y  = 460)
    stu = customtkinter.CTkButton(frame, text = "Student",text_color="black", corner_radius= 20,  width = 200, height=65, font =("Arial Black", 20), command = loginstu,fg_color="white",border_color="black", border_width=3,hover_color="grey") 
    stu.place(x = 250, y = 530)

    win.mainloop()

def loginteach():
    window=Tk()
    window.title("Login and Signup")
    window.geometry("1920x1080")


    frame=LabelFrame(window,text="Teacher Portal",padx=200,pady=200)
    frame.pack()
    b= Button(frame, text="Log in",padx=10,pady=5)
    b.pack(padx=160,pady=140)
    b2= Button(frame,text="Dont have an account ?sign up",padx=10,pady=5, command = teareg)
    b2.pack(padx=5,pady=10)
    l=Label(frame,text="username")
    l.place(x=1,y=1)
    l2=Label(frame,text="password")
    l2.place(x=2,y=50)
    e=Entry(frame,borderwidth=5)
    e.place(x=5,y=30)
    e2=Entry(frame,borderwidth=5)
    e2.place(x=8,y=80)
    window.mainloop()
def loginstu():
    window=Tk()
    window.title("Login and Signup")
    window.geometry("1920x1080")


    frame=LabelFrame(window,text="Student portal",padx=200,pady=200)
    frame.pack()
    b= Button(frame, text="Log in",padx=10,pady=5)
    b.pack(padx=160,pady=140)
    b2= Button(frame,text="Dont have an account ?sign up",padx=10,pady=5,command= stureg)
    b2.pack(padx=5,pady=10)
    l=Label(frame,text="Student ID")
    l.place(x=1,y=1)
    l2=Label(frame,text="password")
    l2.place(x=2,y=50)
    e=Entry(frame,borderwidth=5)
    e.place(x=5,y=30)
    e2=Entry(frame,borderwidth=5)
    e2.place(x=8,y=80)
    window.mainloop()

def stureg():
    root = Tk()
    root.geometry("500x500")
    Label(root,text="your detail",font="ar 15 bold").grid(row=0,column = 6)
    Label(root,text="Please fill out these fields",font="ar 7 bold").grid(row=1,column = 6)

    def getvals():
        print("accepted")
        
    Name = Label(root,text = "Name")
    classroll = Label (root,text="class roll")
    date_of_birth = Label(root,text = "Date Of Birth")
    Address = Label(root,text = "Address")
    City = Label(root,text = "City")
    Province_State = Label(root,text = "Province/State")
    School = Label(root,text="School")
    Collage = Label(root,text = "Collage")
    Gender = Label(root,text= "Gender")
    Background = Label(root,text = "Background")
    Contact_number = Label(root,text = "Contact Number")
    Parents_Contact_number = Label(root,text = "Parents Contact Number")
    Parents_First_Name = Label(root,text = "Parents First Name")
    Parents_LAst_Name = Label(root,text = "Parents Last Name")
    Parents_Email_Address = Label(root,text = "Parents Email Address")


    Name.grid(row=3,column = 3)
    classroll.grid(row=3,column=5)
    date_of_birth.grid(row=3, column = 7)
    Address.grid(row=4,column = 3)
    City.grid(row=4,column = 5)
    Province_State.grid(row=4,column = 7)
    School.grid(row=5,column = 3)
    Collage.grid(row=5,column = 5)
    Gender.grid(row=5,column=7)
    Background.grid(row=6,column = 3)
    Contact_number.grid(row=6,column = 5)
    Parents_Contact_number.grid(row=6,column = 7)
    Parents_First_Name.grid(row=7,column = 3)
    Parents_LAst_Name.grid(row=7,column = 5)
    Parents_Email_Address.grid(row=7,column = 7)

    NameVAlue = StringVar
    ClassrollValue = IntVar
    date_of_birth_value = StringVar
    Addressvalue = StringVar
    CityVAlue = StringVar
    ProvinceVAlue = StringVar
    SchoolVAlue = StringVar
    CollageVAlue = StringVar
    Gendervalue = StringVar
    BackgroundVAlue = StringVar
    ContactnumberVAlue = IntVar
    ParentscontactnumberVAlue = StringVar
    parentsfirstnameVAlue = StringVar
    ParentslastnameVAlue = StringVar
    ParentsEmailadressVAlue = StringVar
    Upadtevalue = IntVar

    NameEntry = Entry(root,textvariable =NameVAlue )
    ClassrollEntry = Entry(root,textvariable=ClassrollValue)
    date_of_birth_Entry = Entry(root,textvariable=date_of_birth_value)
    AddressEntry = Entry(root,textvariable =Addressvalue )
    CityEntry = Entry(root,textvariable =CityVAlue )
    Province_StateEntry = Entry(root,textvariable =ProvinceVAlue )
    SchoolEntry = Entry(root,textvariable =SchoolVAlue )
    CollageEntry = Entry(root,textvariable =CollageVAlue )
    GenderEntry = Entry(root,textvariable=  Gendervalue)
    BackgroundEntry = Entry(root,textvariable =BackgroundVAlue )
    Contact_numberEntry = Entry(root,textvariable =ContactnumberVAlue )
    PArents_contactEntry = Entry(root,textvariable =ParentscontactnumberVAlue )
    Parents_firstnameEntry = Entry(root,textvariable =parentsfirstnameVAlue )
    Parents_lastnameEntry = Entry(root,textvariable =ParentslastnameVAlue )
    Parents_EmailaddressEntry = Entry(root,textvariable =ParentsEmailadressVAlue )

    NameEntry.grid(row=3,column = 4)
    ClassrollEntry.grid(row=3,column = 6)
    date_of_birth_Entry.grid(row=3,column=8)
    AddressEntry.grid(row=4,column = 4)
    CityEntry.grid(row=4,column = 6)
    Province_StateEntry.grid(row=4,column = 8)
    SchoolEntry.grid(row=5,column = 4)
    CollageEntry.grid(row=5,column = 6)
    GenderEntry.grid(row=5,column=8)
    BackgroundEntry.grid(row=6,column = 4)
    Contact_numberEntry.grid(row=6,column = 6)
    PArents_contactEntry.grid(row=6,column = 8)
    Parents_firstnameEntry.grid(row=7,column = 4)
    Parents_lastnameEntry.grid(row=7,column = 6)
    Parents_EmailaddressEntry.grid(row=7,column = 8)

    Button(text = "Update",command=getvals,bg="blue").grid(row=8,column=6)
    root.mainloop()

def teareg():

    root=Tk()
    root.title("Registratiion Form")
    root.geometry("550x600")

    label_1 = Label(root, text=" TEACHER REGISTRATION ",font=("bold",20),fg='#F5761A',bg='#746AB0')  
    label_1.place(x=90,y=60)  

    label_2 =Label(root, text= "First Name: ", width=20,font=("bold",10))  
    label_2.place(x=80,y=130)  
    enter_1 = Entry(root)  
    enter_1.place(x=240,y=130)


    label_3= Label(root,text="Last Name: ",width=20,font=("bold",10))
    label_3.place(x=80,y=160)
    enter_2 = Entry(root)  
    enter_2.place(x=240,y=160)

    label_14 = Label(root, text="Gender: ", width=20,font=("bold",10))  
    label_14.place(x=80,y=190)  

    vars = IntVar() 

    gender_button_male= Radiobutton(root, text="Male", padx= 5, variable= vars, value=1).place(x=230, y=190)  
    gender_button_female= Radiobutton(root, text="Female", padx= 20, variable= vars, value=2).place(x=285,y=190)  

    label_4 = Label(root, text="Email: ", width=20,font=("bold",10))  
    label_4.place(x=80,y=220)  
    enter_3 = Entry(root)  
    enter_3.place(x=240,y=220)  

    label_5 = Label(root, text="Address: ", width=20,font=("bold",10))  
    label_5.place(x= 80,y=250)  
    enter_4 = Entry(root)  
    enter_4.place(x=240,y=250)  

    label_6 = Label(root, text="Nationality: ", width=20,font=("bold",10))  
    label_6.place(x= 80,y=280)  
    enter_5 = Entry(root)  
    enter_5.place(x=240,y=280)  

    label_7 = Label(root, text="Subject: ", width=20,font=("bold",10))  
    label_7.place(x= 80,y=310)  
    list_of_subject=[ 'Maths' ,'Science' , 'English' ,'Social' ,'Nepali' , 'Computer' , 'Opt-Maths' , 'Account' , 'G.k']  
    li = StringVar()  
    drplist = OptionMenu(root, li, *list_of_subject)  
    drplist.config(width=15,bg='grey')  
    li.set('Select your Subject')  
    drplist.place(x=235, y=304)  


    label_8 = Label(root, text="Date Of Birth: ", width=20,font=("bold",10))  
    label_8.place(x= 80,y=340)  
    enter_7 = Entry(root)  
    enter_7.place(x=240,y=340) 

    label_9 = Label(root, text="Place Of Birth: ", width=20,font=("bold",10))  
    label_9.place(x= 80,y=370)  
    enter_8 = Entry(root)  
    enter_8.place(x=240,y=370) 

    label_10 = Label(root, text="Language: ", width=20,font=("bold",10))  
    label_10.place(x= 80,y=400)  
    enter_9 = Entry(root)  
    enter_9.place(x=240,y=400)

    label_13= Label(root, text="Social Network Site: ", width=20,font=("bold",10))  
    label_13.place(x= 80,y=490)  
    enter_11 = Entry(root)  
    enter_11.place(x=240,y=490)

    submit_button= Button(root, text='Submit' , width=20, bg="black",fg='white')
    submit_button.place(x=180,y=530)  


    root.mainloop()

stutea()
