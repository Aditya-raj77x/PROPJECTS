from tkinter import *
root=Tk()
root.geometry("500x300")
def ms():
    print("your form have been accepted")
Label(root,text="Python Registration Form",font="ar 17 bold").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="PHone")
gender=Label(root,text="Gender")
email=Label(root,text="Mail ID")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)
n=StringVar
p=StringVar
g=StringVar
e=StringVar
button=IntVar
nentry=Entry(root,textvariable=n)
pentry=Entry(root,textvariable=p)
gentry=Entry(root,textvariable=g)
eentry=Entry(root,textvariable=e)
nentry.grid(row=1,column=3)
pentry.grid(row=2,column=3)
gentry.grid(row=3,column=3)
eentry.grid(row=4,column=3)

ckbutton=Checkbutton(text="remember me ",variable=button)
ckbutton.grid(row=5,column=3)

Button(text="SUBMIT",command=ms).grid(row=6,column=3)



root.mainloop()