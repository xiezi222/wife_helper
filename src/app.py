#!usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import tkinter
from src.views.home_view import HomeView

project_dir = os.path.dirname(os.path.abspath(__file__))


class App:
    def __init__(self):
        self.window = None
        self.init_window()

    def init_window(self):
        self.window = tkinter.Tk()
        self.setup_window()
        self.create_main_view()
        self.window.mainloop()

    def setup_window(self):
        self.window.title("爱妻助手")
        try:

            # icon_path = os.path.join(project_dir, 'src')
            icon_path = os.path.join(project_dir, 'assets')
            icon_path = os.path.join(icon_path, 'logo')
            icon_path = os.path.join(icon_path, 'logo.ico')
            self.window.iconbitmap(bitmap=icon_path)
        except Exception as e:
            print("window.icon load error:" + str(e))
        width = 600
        height = 400
        left = int((self.window.winfo_screenwidth() - width) / 2)
        top = int((self.window.winfo_screenheight() - height) / 2)
        self.window.geometry(f"{width}x{height}+{left}+{top}")
        # window.config(bg="green")

    def create_main_view(self):
        HomeView(self.window).config(bg="pink")
