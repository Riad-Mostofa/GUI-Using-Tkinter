from tkinter import *

root = Tk()
root.geometry("770x456")
root.title("Pycharm")

def myfunc():
    print("Complex function")

#TODO:Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


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
mainmenu.add_cascade(label="Help", menu=m11)
root.config(menu=mainmenu)


root.mainloop()
