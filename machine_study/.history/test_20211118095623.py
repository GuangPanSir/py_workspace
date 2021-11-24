from tkinter import filedialog, ttk
import tkinter as tk
import os


# 打开文件夹
def opendir():
    dir = os.path.dirname(fpath.get())
    os.system('start ' + dir)




root = tk.Tk()
root.geometry('400x400')
fpath = tk.StringVar()
ttk.Button(root, text='打开', command=getfile).grid(row=0, column=0)
ttk.Entry(root, textvariable=fpath).grid(row=0, column=1)
ttk.Button(root, text='打开文件路径', command=opendir).grid(row=1, column=0)
root.mainloop()
