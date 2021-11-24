from tkinter import filedialog, ttk
import tkinter as tk


# 打开文件对话框
def getfile():
    file_path = filedialog.askopenfilename()
    img_gif = Tkinter.PhotoImage(file = 'img_gif.gif')
    label_img = Tkinter.Label(root, image = img_gif)
label_img.pack()
    fpath.set(file_path)
    

root = tk.Tk()
root.geometry('400x400')

fpath = tk.StringVar()
ttk.Button(root, text='打开', command=getfile).grid(row=0, column=0)
ttk.Entry(root, textvariable=fpath).grid(row=0, column=1)
root.mainloop()
