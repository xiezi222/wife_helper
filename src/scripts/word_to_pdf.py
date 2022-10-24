#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from base_script import BaseScript
# from win32com.client import constants, gencache

class WordToPDF(BaseScript):

    def __init__(self, word_path):
        self.word_path = word_path

        # 获取文件路径
        filepath = os.path.abspath(word_path)
        index = filepath.rindex('.')
        # 通过截取获取pdfpath
        self.out_path = filepath[:index] + '.pdf'

    def remove_old_out_file(self):
        if os.path.exists(self.out_path):
            print("删除之前的输出文件")
            os.remove(self.out_path)

    def executive(self):
        self.remove_old_out_file()

        # word = gencache.EnsureDispatch('Word.Application')
        # doc = word.Documents.Open(self.word_path, ReadOnly=1)
        # # 转换方法
        # doc.ExportAsFixedFormat(self.out_path, constants.wdExportFormatPDF)
        # word.Quit()
