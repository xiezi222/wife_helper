#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from src.tools.utils import *
from win32com.client import constants, gencache


class Script():

    def run(self, input_path, output_directory):

        name = os.path.split(input_path)[1]
        name = name.split('.')[0]
        if len(name) <= 0:
            alert("输入路径不对：" + input_path)

        output_path = os.path.join(output_directory, name + ".PDF")
        if os.path.exists(output_path):
            os.remove(output_path)

        word = gencache.EnsureDispatch('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(input_path, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(output_path, constants.wdExportFormatPDF)
        word.Quit()
        alert("完成")


if __name__ == '__main__':
    print("不支持直接运行")
