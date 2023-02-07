from tkinter import *
from tkinter import messagebox
import customtkinter
from tkextrafont import Font
from PIL import ImageTk,Image

window=Tk()
window.title("Student Portal")
window.geometry("1920x1080")

bg = customtkinter.CTkImage(Image.open("images\\sbac.jpg"), size = (1550, 800))

# Show image using label
label1 = customtkinter.CTkLabel(window, image = bg)
label1.place(x = 0, y = 0)

def click():
    e.delete(0 ,'end')

def leave():
    n = e.get()
    if n == '':
        n.insert("Student ID")

my_img = Image.open("images/wlogo.png")                 
my_label = Label(window, image=my_img, borderwidth=0)
img= my_img.resize((400, 400)) 
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
# l=Label(frame,text="Student ID", font = 25, bg = "#d9d9d9")
# l.place(x=750,y=150)
e = Entry(frame, width = 25, fg= "grey", border = 0, bg = "#d9d9d9",  font = ("Ariel",11))
e.place(x=750,y=180)
e.insert(0, "Student ID")
e.bind("<FocusIn>",click)
e.bind("<FocusOut>",leave)
f1 = Frame(frame, width = 295, height=2,bg="black")
f1.place(x = 750, y = 200)
# l2=customtkinter.CTkLabel(frame,text="Password")
# l2.place(x=750,y=210)
e2 = Entry(frame, width = 25, fg= "black", border = 0, bg = "#d9d9d9",  font = ("Ariel",11))
e2.place(x=750,y=230)
e2.insert(0, "password")
window.mainloop()