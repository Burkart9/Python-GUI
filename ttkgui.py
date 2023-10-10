import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Window
root = ttk.Window(title="My ttk Window", themename="darkly", size=(500, 400), iconphoto="Graphics/notebook2.png")
root.position_center()

# Functions
def test():
    print("Test")

# Widgets
b1 = ttk.Button(root, text="Button 1", command=test, bootstyle=SUCCESS)
b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))

wl = [b1,b2]
for w in wl:
    w.pack(fill=BOTH)

# Mainloop
root.mainloop()