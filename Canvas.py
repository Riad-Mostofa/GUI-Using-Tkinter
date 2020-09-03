from tkinter import *

root = Tk()
#title
root.title("Canvas")

# geometry
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2,y2
can_widget.create_line(0, 0, 800, 400, fill="green")
can_widget.create_line(0, 400, 800, 0, fill="green")

# To create a rectangular specify parameters in this order - coorsponding of top left and coorsponding of bottom right
can_widget.create_rectangle(3, 4, 700, 300, fill="green")

# To create text
can_widget.create_text(700, 300, text="Python")

# To create oval
can_widget.create_oval(344, 233, 244, 355, fill="grey")

root.mainloop()