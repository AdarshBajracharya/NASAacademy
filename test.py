from tkinter import *
root = Tk()
root.geometry("1920x1080")
frame1 = Frame(root,bg="black",width=1500,height=1500)
frame1.pack(padx=200,pady=150)
frame1.propagate(False)

frame2 = Frame(frame1,bg="white",width=1500,height=1500)
frame2.pack(pady=10,padx=10)
frame2.propagate(False)
