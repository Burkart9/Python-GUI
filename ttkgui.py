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
b1.pack(side=LEFT, padx=5, pady=10, expand=True, fill=X)
b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10, expand=True, fill=X)

# Mainloop
root.mainloop()