# Simple GUI
# Demonstrates creating a window
from tkinter import *
# create the root window
root = Tk()
# modify the window
root.title("Simple GUI")
root.geometry("200x100")
# kick off the window's event loop
root.mainloop()
# create a frame in the window to hold other widgets
app = Frame(root)
app.grid()
# create a label in the frame
lbl = Label(app, text = "I'm a label!")
lbl.grid()
# kick off the window's event loop
root.mainloop()
# create a button in the frame
bttn1 = Button(app, text = "I do nothing!")
bttn1.grid()
# create a second button in the frame
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me too!")
# create a third button in the frame
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same here!"
# kick off the window's event loop
root.mainloop()
