from tkinter import *


root = Tk()

# gui logic here

# title
root.title("Simple Frame")
# using geometry

# opening window width x height
root.geometry('655x333')


#frame work
f1 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f1.pack(side=TOP, fill="x")


f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=0)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red")
l.pack()



root.mainloop()