from tkinter import *
from tkinter import messagebox
from tkextrafont import Font
from PIL import ImageTk,Image


def stutea():
    #Creating window
    global win
    global bg
    win = Tk()
    win.title("NASA Academy")
    win.iconbitmap("images/cap.ico")
    win.geometry("1920x1080")
        
    #Setting background image
    bg = ImageTk.PhotoImage(Image.open("images\\sbac.jpg"))
    label1 = Label(win, image = bg)
    label1.place(x = 0, y = 0)
    
    #Creating frame
    frame = Frame(win,width=700,height=750, bd = 10, highlightthickness=3, highlightbackground="black")
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)


    # def framecl():
    #     frame.pack_forget()
    #     loginstu()
    

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
    im = Label(frame, text = " I am a..", font = ("Bahnschrift", 18))
    im.place(x= 300 ,y =490)
    teach = Button(frame, text = "Teacher", width = 10, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    teach.place(x = 240, y = 600)
    stu = Button(frame, text = "Student", width = 10, height=1, font =("Heavitas", 20), activebackground= "grey",bg="white")
    stu.place(x = 240, y = 530)

    win.mainloop()


stutea()
