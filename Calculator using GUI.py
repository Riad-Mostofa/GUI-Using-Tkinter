from tkinter import *


root = Tk()

root.wm_iconbitmap("1.ico")
root.title("Calculator")
root.geometry("344x596")
# root.configure(background="grey")


#TODO:using to set a screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, background="yellow", font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


#TODO:using to set frame,button and get output

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                scvalue.set("Erorr")
                screen.update()


        scvalue.set(value)
        screen.update()

    elif text == "C":
       scvalue.set("")
       screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

f = Frame(root, bg="grey")

b = Button(f, text="9", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")

b = Button(f, text="5", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")


b = Button(f, text="1", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=4, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")

b = Button(f, text="*", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text=".", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=0, pady=0, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

f.pack()



root.mainloop()