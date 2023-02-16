from tkinter import*

root = Tk()
root.geometry("425x350")
root.title("Result")
def result():
    f2 = Frame(bg="Navyblue")
    f2.place(x=0,y=0,width=425,height = 350)

    viva = Label(f2,text="viva  ",font=45)
    viva.place(x = 50,y = 15)
    written = Label(f2,text="written  ",font=45 )
    written.place(x = 50,y = 35)
    total = Label(f2,text="total " ,font=45)
    total.place(x = 50,y = 55)
    b1 = Button(f2,text="back",command=home)
    b1.place(x = 50,y = 80,width=100,height=40)

def home():
    f1 = Frame(bg="Navyblue",)
    f1.place(x=0,y=0,width=425,height=350)

    sub = Label(text="Select Subjects")
    sub.place(x=50,y=15)



    eng = Button(f1,text="English",command=result)
    eng.place(x = 50,y = 50,width=80,height=30)

    math = Button(f1,text = "Math",command=result)
    math.place(x = 50,y = 100,width=80,height=30)

    computer = Button(f1,text = "Computer",command=result)
    computer.place(x = 50,y = 150,width=80,height=30)

home()

root.mainloop()
