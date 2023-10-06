# mytk
# Aunthor: Burkart_Yang
# External Libs
import tkinter as tk
import xml.etree.ElementTree as ET

# Variables
themes = {
    "light": {"bg": "white", "fg": "black"},
    "dark": {"bg": "black", "fg": "white"},
    "gray_teal":{"bg":"gray","fg":"teal"},
    "dark_teal":{"bg":"black","fg":"teal"},
    "light_teal":{"bg":"teal","fg":"white"},
}

# Functions
def window_init(window:vars,title:str,size:str="300x400",resize:bool=True,iconbitmap:str=""):
    """
    This function helps you to initialize windows. 

    Parameters:

    window: The object
    title: The title of the window
    size: The size of the window
    resize: Can/can't resize
    iconbitmap: The path of ico file
    """
    window.title(title)
    window.geometry(size)
    window.resizable(resize,resize)
    window.iconbitmap(iconbitmap)
    print("大小为{}的{}窗口已经初始化完成。".format(size,title))

def set_widget_theme(theme_name:str,widget_list:list):
    '''
    用于设定控件的原始主题。

    变量：

    theme_name:主题的名称,来自于我的themes字典。

    widget_list:需要设定主题的控件列表。
    '''
    for w in widget_list:
        w.configure(bg=themes[theme_name]["bg"], fg=themes[theme_name]["fg"])
        print("你成功设置了一个{}主题的控件。".format(theme_name))

# Classes
class GUIApplication: # 用于从xml解析并生成带控件的窗口
    def __init__(self, xml_file): # 参数是xml文件的路径
        self.root = tk.Tk()
        self.parse_xml(xml_file)
        self.create_gui()

    def parse_xml(self, xml_file):
        tree = ET.parse(xml_file)
        self.root_element = tree.getroot()

    def create_gui(self):
        self.set_title()
        self.create_components()

    def set_title(self):
        title = self.root_element.find("title").text
        self.root.title(title)

    def create_components(self):
        for component_element in self.root_element.findall("component"):
            component_type = component_element.get("type")
            if component_type == "button":
                self.create_button(component_element)
            # if component_type == other widgets...

    def create_button(self, button_element):
        button_text = button_element.find("text").text
        button_command = button_element.find("command")
        if button_command is not None:
            button_command = eval(button_command.text)  # 将字符串转换为函数
        else:
            button_command = None
        button = tk.Button(self.root, text=button_text, command=button_command)
        # 前景色
        button_fg = button_element.find("fg")
        if button_fg is not None:
            button_fg = button_fg.text
        if button_fg:
            button.configure(fg=button_fg)
        # 背景色
        button_bg = button_element.find("bg")
        if button_bg is not None:
            button_bg = button_bg.text
        if button_bg:
            button.configure(bg=button_bg)
        # 布局按钮   
        button.pack()

    def run(self):
        self.root.mainloop()
        print("You have created a window with widgets from a xml file.")