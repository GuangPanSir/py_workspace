from tkinter import filedialog, ttk
import tkinter as tk
from PIL import Image, ImageTk


# 打开文件对话框
def getfile():
    file_path = filedialog.askopenfilename()
    aa(fil)
    fpath.set(file_path)


def aa(file_path):

    global img0
    photo = Image.open("小猫.jpg")  # 括号里为需要显示在图形化界面里的图片

    photo = photo.resize((400, 400))  # 规定图片大小
    img0 = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img0)

    img1.pack()


root = tk.Tk()
root.geometry('400x400')

fpath = tk.StringVar()
ttk.Button(root, text='打开', command=getfile).grid(row=0, column=0)
ttk.Entry(root, textvariable=fpath).grid(row=0, column=1)
root.mainloop()
