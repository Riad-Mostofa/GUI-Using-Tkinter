from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("770x456")
root.title("Pycharm")

def myfunc():
    print("Complex function")

def help():
    print("I will help you.")
    tmsg.showinfo("Help", "I will help you")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Experience", "Was your experience is good?")
    if value == "yes":
        msg = "Great.Rate us on Appstore please."
    else:
        msg = "Tell us what is wrong we will fix it soon."
    tmsg.showinfo("Experienced", msg)

def erorr():
    ans = tmsg.askretrycancel("Fatal erorr", "You are in danger.")
    if ans:
        print("Contact with us.")
    else:
        print("Try later!")

#TODO:Use these to create a dropdown menu

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
m1.add_command(label="Exit", command=quit)
mainmenu.add_cascade(label="File", menu=m1)
root.config(menu=mainmenu)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Delete", command=myfunc)
m2.add_command(label="Find", command=quit)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)


m3 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="View", menu=m3)
root.config(menu=mainmenu)

m4 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Navigate", menu=m4)
root.config(menu=mainmenu)

m5 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Code", menu=m5)
root.config(menu=mainmenu)

m6 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Refactor", menu=m6)
root.config(menu=mainmenu)

m7 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Run", menu=m7)
root.config(menu=mainmenu)

m8 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Tools", menu=m8)
root.config(menu=mainmenu)

m9 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="VCS", menu=m9)
root.config(menu=mainmenu)

m10 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Window", menu=m10)
root.config(menu=mainmenu)

m11 = Menu(mainmenu, tearoff=0)
m11.add_command(label="Help", command=help)
m11.add_command(label="Rate us", command=rate)
m11.add_command(label="Erorr", command=erorr)
mainmenu.add_cascade(label="Help", menu=m11)
root.config(menu=mainmenu)


root.mainloop()