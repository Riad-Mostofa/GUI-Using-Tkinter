from  tkinter import *
from PIL import Image, ImageTk

root = Tk()

# gui logic here

# title
root.title("Image")
# using geometry

# opening window width x height
root.geometry('655x333')
# width, height use for minimum size
root.minsize(344, 244)
# width, height use for maximum size
root.maxsize(900, 644)

#For png Image

# photo = PhotoImage(file="2.png")

#For jpg Image

image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)

riad_label = Label(image=photo)
riad_label.pack()

root.mainloop()