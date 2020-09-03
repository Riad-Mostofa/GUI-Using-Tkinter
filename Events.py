from tkinter import *
def riad(event):
    print(f"You click on the button at {event.x}, {event.y}")
root = Tk()
#title
root.title("Events")

root.geometry("644x334")

widget = Button(root, text="Click Me")
widget.pack()

# widget bind
widget.bind('<Button-1>', riad)
widget.bind('<Double-1>', quit)

root.mainloop()