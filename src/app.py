#!usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
from src.views.home_view import HomeView


class App:
    def __init__(self):
        self.init_window()

    def init_window(self):
        window = tkinter.Tk()
        self.setup_window(window)
        self.create_main_view(window)
        window.mainloop()

    def setup_window(self, window):
        window.title("爱妻小助手")
        width = 600
        height = 400
        left = int((window.winfo_screenwidth() - width) / 2)
        top = int((window.winfo_screenheight() - height) / 2)
        window.geometry(f"{width}x{height}+{left}+{top}")
        # window.config(bg="green")

    def create_main_view(self, window):
        HomeView(window).config(bg="pink")