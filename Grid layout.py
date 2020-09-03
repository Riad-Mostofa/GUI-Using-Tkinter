from tkinter import *


root = Tk()

# title
root.title("Password Tracker")

# opening window width x height
root.geometry('655x333')

#create a lebel
user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

#Using Variable

def getvals():
 print(f"The value of username is {uservalue.get()}")

 print(f"The value of password is {passvalue.get()}")

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()


root.mainloop()