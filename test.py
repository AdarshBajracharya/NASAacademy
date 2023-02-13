from tkinter import *
from tkinter import messagebox
import customtkinter
from tkextrafont import Font
from PIL import ImageTk,Image


def loginstu():

    global bg 
    global my_image
    window=Tk()
    window.title("Student Portal")
    window.geometry("1920x1080")

    bg = customtkinter.CTkImage(Image.open("images\\sbac.jpg"), size = (1550, 800))

    # Show image using label
    label1 = customtkinter.CTkLabel(window, image = bg)
    label1.place(x = 0, y = 0)


    frame=customtkinter.CTkFrame(window,width = 1200, height = 700, corner_radius=20, border_color="black", border_width=2)
    frame.pack(padx=20, pady=45)
    frame.pack_propagate(False)
    my_image = Image.open("images/student.png")     
    img= my_image.resize((400, 400))  
    reimg = ImageTk.PhotoImage(img)        
    my_label = Label(frame, image=reimg, borderwidth=0, bg ="#d9d9d9")
    my_label.place(x= 115, y= 150)
    b= customtkinter.CTkButton(frame, text="Log in")
    b.place(x =850, y = 310)
    # b2= Button(frame,text="Dont have an account ?sign up",padx=10,pady=5)
    # b2.pack(padx=5,pady=10)
    s = Label(frame , text = "Student Sign In", font = ("Microsoft Yahei UI light",23), bg ="#d9d9d9")
    s.place(x = 800, y = 50)  
    l=Label(frame,text="Student ID", bg = "#d9d9d9")
    l.place(x=750,y=150)
    e = customtkinter.CTkEntry(frame,width = 250)
    e.place(x=750,y=170)
    l2=customtkinter.CTkLabel(frame,text="Password")
    l2.place(x=750,y=210)
    e2 = customtkinter.CTkEntry(frame, width =250)
    e2.place(x=750,y=235)

    window.mainloop()


loginstu()

# from tkinter import *
# root = Tk()
# root.geometry("1920x1080")
# frame1 = Frame(root,bg="black",width=1500,height=1500)
# frame1.pack(padx=200,pady=150)
# frame1.propagate(False)

# frame2 = Frame(frame1,bg="white",width=1500,height=1500)
# frame2.pack(pady=10,padx=10)
# frame2.propagate(False)

# frame3=Frame(frame2,bg="red",width=90,height=600)
# frame3.pack(padx=1,pady=1,side=LEFT)
# frame3.propagate(False)

# frame4=Frame(frame2,bg="blue",width=150,height=600)
# frame4.pack(padx=1,pady=1,side=LEFT)
# frame4.propagate(False)

# frame5=Frame(frame2,bg="yellow",width=150,height=600)
# frame5.pack(padx=1,pady=1,side=LEFT)
# frame5.propagate(False)
# l1=Label(frame5,text="Monday",fg="white", bg = "yellow").pack(padx=0,pady=0)

# frame6=Frame(frame2,bg="purple",width=150,height=600)
# frame6.pack(padx=1,pady=1,side=LEFT)
# frame6.propagate(False)

# frame7=Frame(frame2,bg="maroon",width=150,height=600)
# frame7.pack(padx=1,pady=1,side=LEFT)
# frame7.propagate(False)

# frame8=Frame(frame2,bg="green",width=150,height=600)
# frame8.pack(padx=1,pady=1,side=LEFT)
# frame8.propagate(False)

# frame9=Frame(frame2,bg="black",width=150,height=600)
# frame9.pack(padx=1,pady=1,side=LEFT)
# frame9.propagate(False)

# frame10=Frame(frame2,bg="grey",width=150,height=600)
# frame10.pack(padx=1,pady=1,side=LEFT)
# frame10.propagate(False)


# root.mainloop()