from tkinter import *
root = Tk()
root.geometry("1920x1080")
frame1 = Frame(root,bg="black",width=1500,height=1500)
frame1.pack(padx=200,pady=150)
frame1.propagate(False)

frame2 = Frame(frame1,bg="white",width=1500,height=1500)
frame2.pack(pady=10,padx=10)
frame2.propagate(False)


frame3=Frame(frame2,bg="red",width=90,height=600)
frame3.pack(padx=1,pady=1,side=LEFT)
frame3.propagate(False)
l8=Label(frame3,text="6AM",fg="black").pack(padx=30,pady=30)


frame4=Frame(frame2,bg="blue",width=150,height=600)
frame4.pack(padx=1,pady=1,side=LEFT)
frame4.propagate(False)
b= Button(frame4, text="English",fg="black")
b.place(x=50,y=30)
b= Button(frame4, text="Computer",fg="black")
b.place(x=50,y=90)
l7=Label(frame4,text="Sunday",fg="black").pack(padx=1,pady=1) 

frame5=Frame(frame2,bg="yellow",width=150,height=600)
frame5.pack(padx=1,pady=1,side=LEFT)
frame5.propagate(False)
b= Button(frame5, text="English",fg="black")
b.place(x=50,y=170)
b= Button(frame5, text="Maths",fg="black")
b.place(x=50,y=215)
l1=Label(frame5,text="Monday",fg="black").pack(padx=1,pady=1)


frame6=Frame(frame2,bg="purple",width=150,height=600)
frame6.pack(padx=1,pady=1,side=LEFT)
frame6.propagate(False)
b= Button(frame6, text="English",fg="black")
b.place(x=50,y=290)
b= Button(frame6, text="Computer",fg="black")
b.place(x=50,y=380)
l2=Label(frame6,text="Tuesday",fg="black").pack(padx=1,pady=1)

frame7=Frame(frame2,bg="maroon",width=150,height=600)
frame7.pack(padx=1,pady=1,side=LEFT)
frame7.propagate(False)
b= Button(frame7, text="Maths",fg="black")
b.place(x=50,y=30)
b= Button(frame7, text="Computer",fg="black")
b.place(x=50,y=90)
l3=Label(frame7,text="Wednesday",fg="black").pack(padx=1,pady=1)