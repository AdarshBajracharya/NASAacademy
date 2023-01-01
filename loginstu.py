from tkinter import *

def loginstu():

    tkWindo = Tk()  
    tkWindo.geometry('400x150')  
    tkWindo.title('Student Login')

    #username label and text entry box
    usernameLabel = Label(tkWindo, text="Student ID").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindo, textvariable=username).grid(row=0, column=1)  

        #password label and password entry box
    passwordLabel = Label(tkWindo,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindo, textvariable=password, show='*').grid(row=1, column=1)  


    #login button
    loginButton = Button(tkWindo, text="Login").grid(row=4, column=0)  

    tkWindo.mainloop()