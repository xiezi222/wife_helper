from tkinter import messagebox


def log_error(msg):
    print("\033[0;37;41m警告:" + msg + "\033[0m")

def alert(msg):
    messagebox.showinfo("提示", msg)

def confirm(msg):
    return messagebox.askyesno("确认", msg)