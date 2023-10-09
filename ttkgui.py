import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Window
root = ttk.Window(title="My ttk Window",themename="darkly",size=(500,400),iconphoto="Graphics/notebook2.png")
root.position_center()

# Widgets
b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)
b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

# Functions












# Mainloop
root.mainloop()