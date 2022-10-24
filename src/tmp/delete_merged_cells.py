#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import xlwings as xw


def log_error(msg):
    print("\033[0;37;41m警告:" + msg + "\033[0m")


def local_excel_files():
    local = os.getcwd()
    paths = []
    for name in os.listdir(local):
        is_excel = name.endswith("xlsx") or name.endswith("xls")
        not_valid = name.startswith(".") or name.startswith("~")
        if is_excel and not_valid:
            paths.append(name)
    return paths


def delete_merged_rows(sheet):
    max_row = sheet.used_range.last_cell.row
    max_column = sheet.used_range.last_cell.column
    current_row = 1
    start_delete = False
    while current_row <= max_row:
        current_row_range = sheet.range((current_row, 1), (current_row, max_column))
        merged = current_row_range.api.merge_cells()
        if merged is False and start_delete is False:
            start_delete = True
            current_row += 1
            continue
        if merged is True and start_delete is True:
            current_row_range.delete()
            max_row -= 1
        else:
            current_row += 1


def start():

    for app in xw.apps:
        app.kill()
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    file_path = "../../xlsx/工作簿1.xlsx"
    book = xw.Book(file_path)
    for sheet in book.sheets:
        delete_merged_rows(sheet)
    book.save()
    app.quit()


if __name__ == '__main__':
    print("开始执行任务……")
    start()
    print("任务执行完毕")
