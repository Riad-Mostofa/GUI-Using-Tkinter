from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i = 0
root = Tk()
root.title("List Box")
root.geometry("600x456")


lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()