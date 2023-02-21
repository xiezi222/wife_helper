import sys
from tkinter import messagebox

isDebug = True if sys.gettrace() else False


def log_error(msg):
    if isDebug:
        print("\033[0;37;41m警告:" + msg + "\033[0m")
    else:
        messagebox.showerror("警告", msg)


def alert(msg):
    messagebox.showinfo("提示", msg)


def confirm(msg):
    return messagebox.askyesno("确认", msg)