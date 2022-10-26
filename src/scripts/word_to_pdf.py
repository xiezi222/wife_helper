#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from src.tools.utils import *
from win32com.client import constants, gencache


class Script():

    def __init__(self, input_path, output_directory):

        self.input_path = input_path
        self.output_directory = output_directory

    def executive(self):

        name = os.path.split(self.input_path)[1]
        if len(name) <= 0:
            alert("输入路径不对："+self.input_path)

        output_path = os.path.join(self.output_directory, name+".PDF")
        if os.path.exists(output_path):
            os.remove(output_path)

        word = gencache.EnsureDispatch('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(self.input_path, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(self.output_path, constants.wdExportFormatPDF)
        word.Quit()
        alert("完成")
