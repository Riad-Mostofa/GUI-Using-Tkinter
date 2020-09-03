from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Slider")
root.geometry("455x233")

# myslider = Scale(root,from_=0, to=100)
# myslider.pack()
def select():
    print(f"Photo {myslider2.get()} Selected")
    tmsg.showinfo("Selected Items.", f"You deleted {myslider2.get()}, Photo Sucessfully!")


Label(root, text="Choose Photo").pack()
myslider2 = Scale(root,from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(10)
myslider2.pack()

Button(root, text="Select", pady=5, command=select).pack()


root.mainloop()