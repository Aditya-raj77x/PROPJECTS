from tkinter import *
root=Tk()
root.geometry("640x600")
root.title("CALCULATOR BY ADITYA")
root.wm_iconbitmap("game.ico")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucide 40 bold")
screen.pack(fill=X,ipadx=8,pady=2,padx=5)


mainloop()