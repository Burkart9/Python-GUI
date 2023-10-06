# Libs
import tkinter as tk
import mytk
import json

# Main
root = tk.Tk()
mytk.window_init(root,"测试窗口","300x400",False)

## Parse Json File
with open("config.json") as json_file:
    json_data = json.load(json_file)
current_theme = json_data["current_theme"]
fg_color = json_data["theme"][current_theme]["fg"]
bg_color = json_data["theme"][current_theme]["bg"]

## Create Widgets
button_1 = tk.Button(root,text="Button_1")
button_2 = tk.Button(root,text="Button_2")
buttton_list = [button_1,button_2]

## Pack Widgets
for w in buttton_list:
    w.pack()

## Configure Widgets
root.config(bg=bg_color)
for w in buttton_list:
    w.config(fg=fg_color,bg=bg_color)





## Mainloop
root.mainloop()