from tkinter import filedialog, ttk
import tkinter as tk


# 打开文件对话框
def getfile():
    file_path = filedialog.askopenfilename()
    fpath.set(file_path)


root = tk.Tk()
root.geometry('400x400')
img_gif = tk.PhotoImage(file = 'img_gif.gif')
label_img = Tkinter.Label(root, image = img_gif)
label_img.pack()
fpath = tk.StringVar()
ttk.Button(root, text='打开', command=getfile).grid(row=0, column=0)
ttk.Entry(root, textvariable=fpath).grid(row=0, column=1)
root.mainloop()
