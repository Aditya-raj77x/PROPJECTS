from tkinter import *
def click(events):
    global scvalue
    text=events.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except EXCEPTION as e:
                print(e)
                value="error"

        scvalue.set(value)
        screen.update()
    elif text=="c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root=Tk()
root.geometry("600x970")
root.title("CALCULATOR BY ADITYA")
root.wm_iconbitmap("game.ico")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucide 40 bold")
screen.pack(fill=X,ipadx=8,pady=2,padx=5)
f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="9",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)


f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="6",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)


f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="3",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="1",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)

f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="0",padx=15,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)


f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="c",padx=8,pady=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=2,pady=11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="/",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)
b=Button(f,text="!",padx=11,pady=17,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=4)
b.bind("<Button-1>",click)


mainloop()