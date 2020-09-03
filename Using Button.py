from tkinter import *


root = Tk()

# title
root.title("Using Button")

# using geometry
# opening window width x height
root.geometry('655x333')

#frame work
frame = Frame(root, bg="yellow", borderwidth=6, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

#Use command on button
def first():
    print("1")
def second():
    print("2")
def third():
    print("3")
def four():
    print("4")

# button
b1 = Button(frame, fg="Black", text="One", command=first)
b1.pack(side=LEFT, padx=4)

b2 = Button(frame, fg="Black", text="Two", command=second)
b2.pack(side=LEFT, padx=4)

b3 = Button(frame, fg="Black", text="Three", command=third)
b3.pack(side=LEFT, padx=4)

b4 = Button(frame, fg="Black", text="Four", command=four)
b4.pack(side=LEFT, padx=4)




root.mainloop()