from tkinter import *
root = Tk()

root.title("Title of my GUI")
root.geometry("655x444")
root.wm_iconbitmap("1.ico")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()

root.mainloop()