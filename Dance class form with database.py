from tkinter import *


root = Tk()
# title
root.title("Kylin Dance Club")

# opening window width x height
root.geometry('655x333')

# Text for our form
Label(root, text="Welcome to Kylin Dance Club", font="comicsansms 13 bold",pady=10).grid(row=0, column=3)
name = Label(root, text="Name")
gender = Label(root, text="Gender")
age = Label(root, text="Age")
payment = Label(root, text="Payment")

# Pack text for our form
name.grid(row=1, column=2)
gender.grid(row=2, column=2)
age.grid(row=3, column=2)
payment.grid(row=4, column=2)

# Tkinter variable for storing entry
namevalue = StringVar()
gendervalue = StringVar()
agevalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
genderentry = Entry(root, textvariable=gendervalue)
ageentry = Entry(root, textvariable=agevalue)
paymententry = Entry(root, textvariable=paymentvalue)

# packing entry
nameentry.grid(row=1, column=3)
genderentry.grid(row=2, column=3)
ageentry.grid(row=3, column=3)
paymententry.grid(row=4, column=3)

# checkbox
foodservice = Checkbutton(text="Want to prebook your T-Shirt?", variable= foodservicevalue)
foodservice.grid(row=5,column=3)

# Button and packing it and assigning it a command
def getvals():
    print("Submitting form sucessfully!")

    print(f"{namevalue.get(), gendervalue.get(), agevalue.get(), paymentvalue.get(), foodservicevalue.get() }")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), gendervalue.get(), agevalue.get(), paymentvalue.get(), foodservicevalue.get() }\n ")


Button(text="Submit to Kylin Dance Club", command=getvals).grid(row=6, column=3)

root.mainloop()
