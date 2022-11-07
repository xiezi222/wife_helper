#!usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import tkinter
from tkinter import scrolledtext, Frame


class Console(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.text = scrolledtext.ScrolledText(self, state=tkinter.DISABLED)
        self.text.place(relheight=1, relwidth=1)
        self.redirect()

    def redirect(self):
        tmp = sys.stdout
        sys.stdout = self

    def write(self, string):
        self.text.config(state=tkinter.NORMAL)
        self.text.insert(tkinter.END, string)
        self.text.see(tkinter.END)
        self.text.config(state=tkinter.DISABLED)
