#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from src.tools.utils import *
from win32com.client import constants, gencache


class Script:

    def __init__(self):
        self.word = self.create_word_app('Word.Application')
        if self.word is None:
            log_error("检查office软件是否正确安装")
            self.word = self.create_word_app('wps.Application')
            if self.word is None:
                log_error("检查wps软件是否正确安装")

    def create_word_app(self, identifier):
        application = None
        try:
            application = gencache.EnsureDispatch(identifier)
        except Exception as e:
            print(str(e))
        return application

    def run(self, input_path, input_directory, output_directory):
        if self.word is None:
            alert("检查word软件是否正确安装")
            return

        name = os.path.split(input_path)[1]
        name = name.split('.')[0]
        if len(name) <= 0:
            alert("输入路径不对：" + input_path)

        output_path = os.path.join(output_directory, name + ".PDF")
        if os.path.exists(output_path):
            os.remove(output_path)
        self.word.Visible = False
        doc = self.word.Documents.Open(input_path, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(output_path, constants.wdExportFormatPDF)
        self.word.Quit()
        alert("完成")


if __name__ == '__main__':
    print("不支持直接运行")
