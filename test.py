from tkinter import *
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("350x100") 
font1=('Times',18,'bold')	
sv = tk.StringVar() # connected to 1st Label and Spinbox
        
l1=tk.Label(my_w,text='Password',font=font1)  
l1.grid(row=1,column=1,padx=10,pady=10)
e1_str=tk.StringVar() # string variable   
e1 = tk.Entry(my_w,font=font1,width=15,show='*',textvariable=e1_str)
e1.grid(row=1,column=2,padx=5,pady=5)
c_v1=IntVar(value=0)
def my_show():
    if(c_v1.get()==1):
        e1.config(show='')
    else:
        e1.config(show='*')

c1 = tk.Checkbutton(my_w,text='Show Password',variable=c_v1,
	onvalue=1,offvalue=0,command=my_show)
c1.grid(row=2,column=1)    
my_w.mainloop()  
=======
root = Tk()
root.geometry("1920x1080")
frame1 = Frame(root,bg="black",width=1500,height=1500)
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
 
frame10=Frame(frame2,bg="grey",width=150,height=600)
frame10.pack(padx=1,pady=1,side=LEFT)
frame10.propagate(False)
l6=Label(frame10,text="Saturday",fg="black").pack(padx=1,pady=1)
l9=Label(frame3,text="7AM",fg="black").pack(padx=10,pady=10)
l10=Label(frame3,text="8AM",fg="black").pack(padx=10,pady=10)
l11=Label(frame3,text="9AM",fg="black").pack(padx=10,pady=10)
l12=Label(frame3,text="10AM",fg="black").pack(padx=10,pady=10)
l13=Label(frame3,text="11AM",fg="black").pack(padx=10,pady=10)
l14=Label(frame3,text="12PM",fg="black").pack(padx=10,pady=10)
l15=Label(frame3,text="1PM",fg="black").pack(padx=10,pady=10)
l16=Label(frame3,text="2PM",fg="black").pack(padx=10,pady=10)
l17=Label(frame3,text="3PM",fg="black").pack(padx=10,pady=10)
root.mainloop() 

