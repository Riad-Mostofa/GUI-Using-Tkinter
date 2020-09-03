from tkinter import *

root = Tk()
root.title("Scroll Bar")
root.geometry("600x456")
# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(root)
# for i in range(344):
#     listbox.insert(END, f"Item {i}")
#
# listbox.pack(fill="both")
# scrollbar.config(command=listbox.yview)

root.mainloop()