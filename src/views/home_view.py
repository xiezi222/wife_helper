#!usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import os.path
import importlib
from tkinter import Frame, Button, Label, Entry, filedialog
from tkinter.ttk import Separator, Combobox

class HomeView(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.config(bg="gray")
        self.pack(fill="both", expand=True)

        self.input_file = Entry(self, bg="red")
        self.input_directory = Entry(self, bg="blue")
        self.input_script = Combobox(self, values=self.get_script_list())
        self.output_directory = Entry(self, bg="yellow")
        self.add_subviews()

    def add_subviews(self):
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        Label(self, text="选择源文件").grid(row=0, column=0, padx=10, pady="10 0", sticky='w')
        self.input_file.grid(row=1, column=0, sticky='ew', padx="10 0")
        Button(self, text="选择", command=self.get_input_file).grid(row=1, column=1, sticky='w', padx="10 0")

        Label(self, text="选择源文件夹").grid(row=2, column=0, padx=10, pady="10 0", sticky='w')
        self.input_directory.grid(row=3, column=0, sticky='ew', padx="10 0")
        Button(self, text="选择", command=self.get_input_directory).grid(row=3, column=1, sticky='w', padx="10 0")
        Separator(self, orient='horizontal').grid(row=4, column=0, columnspan=2, sticky='ew', pady="10 20")

        Label(self, text="选择脚本").grid(row=5, column=0, padx=10, pady="10 0", sticky='w')
        self.input_script.grid(row=6, column=0, sticky='ew', padx="10 0")
        Separator(self, orient='horizontal').grid(row=7, column=0, columnspan=2, sticky='ew', pady="10 20")

        Label(self, text="选择输出目录").grid(row=8, column=0,  padx=10, pady="10 0", sticky='w')
        self.output_directory.grid(row=9, column=0, sticky='ew', padx="10 0")
        Button(self, text="选择", command=self.get_output_directory).grid(row=9, column=1, sticky='w', padx="10 0")
        Separator(self, orient='horizontal').grid(row=10, column=0, columnspan=2, sticky='ew', pady="10 20")

        Button(self, text="执行", command=self.executive).grid(row=11, column=0, columnspan=2)

    def get_script_directory(self):
        current_path = os.path.dirname(__file__)
        return os.path.join(current_path, "../scripts/")

    def get_script_list(self):
        script_directory = self.get_script_directory()
        script_names = []
        for file_name in os.listdir(script_directory):
            if file_name.endswith("py") and not file_name.startswith("__init__"):
                script_names.append(file_name)
        return script_names

    def get_input_file(self):
        path = filedialog.askopenfilename(title="选择源文件")
        self.input_file.delete(0, "end")
        self.input_file.insert(0, path)

    def get_input_directory(self):
        path = filedialog.askdirectory(title="选择源文件夹")
        self.input_directory.delete(0, "end")
        self.input_directory.insert(0, path)

    def get_output_directory(self):
        path = filedialog.askdirectory(title="选择输出文件夹")
        self.output_directory.delete(0, "end")
        self.output_directory.insert(0, path)

    def executive(self):
        print("executive")
        input_file = self.input_file.get()
        input_directory = self.input_directory.get()
        input_path = input_directory if len(input_directory) > 0 else input_file
        output_path = self.output_directory.get()

        module_name = str(self.input_script.get()).split('.')[0]
        module_path = "src.scripts." + module_name

        module = importlib.import_module(module_path)
        cls = getattr(module, "Script")
        obj = cls()
        obj.run()


