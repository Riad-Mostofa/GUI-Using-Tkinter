from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.title("Radio Button")
root.geometry("600x456")

def start():
    tmsg.showinfo("Selected Channel.", f"You selected {var.get()}, channel is not availabel now.")

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text = "What you want to listen?", font="lucida 19 bold", justify=LEFT, padx=14).pack()

radio = Radiobutton(root, text="Radio Mirchi.", variable=var, value="Radio Mirchi.").pack(anchor="w")
radio = Radiobutton(root, text="Radio Padmna.", variable=var, value="Radio Padmna.").pack(anchor="w")
radio = Radiobutton(root, text="Radio Jamuna.", variable=var, value="Radio Jamuna.").pack(anchor="w")
radio = Radiobutton(root, text="Radio Gonja.", variable=var, value="Radio Gonja.").pack(anchor="w")

Button(text="Listen Now", command=start).pack()


root.mainloop()