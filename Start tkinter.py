from tkinter import *


root = Tk()

# gui logic here

# title
root.title("Simple Calculator")
# using geometry

# opening window width x height
root.geometry('655x333')
# width, height use for minimum size
root.minsize(344, 244)
# width, height use for maximum size
root.maxsize(900, 644)



#create a lebel
title_label = Label(text="GUI CALCULATOR", bg ="yellow",font="comicsansms 12 bold",borderwidth=3,relief=SUNKEN, padx=344)
title_label.pack(side= BOTTOM, fill=X)





root.mainloop()