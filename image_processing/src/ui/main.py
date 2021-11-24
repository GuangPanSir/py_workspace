# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
from mainwindow import Ui_MainWindow as mainwindow
from PIL import Image


import sys



# 全局变量图片地址
from src.food.orderDinner import mainForm

image_path = ''


class MainForm(QMainWindow, mainwindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.initui()

    def initui(self):
        self.setupUi(self)
        self.action_3.triggered.connect(self.open_file)
        self.action.triggered.connect(self.order_food)

    def open_file(self):
        # 可设置默认路径与可选文件类型
        global image_path
        image_path, _ = QFileDialog.getOpenFileName(self.centralWidget(), '选择图片', '/', 'Image files(*.jpg *.gif *.png)')
        # 避免取消选择返回空字符串
        if image_path:
            img = Image.open(image_path)
            # 设置label宽度为图片尺寸
            mainwindow_width = self.geometry().width()
            mainwindow_height = self.geometry().height()
            img_width = img.width
            img_height = img.height

            self.label.setGeometry(
                QtCore.QRect((mainwindow_width - img_width) / 2, (mainwindow_height - img_height) * 0.382, img_width,
                             img_height))
            jpg = QtGui.QPixmap(image_path).scaled(self.label.width(), self.label.height())
            self.label.setPixmap(jpg)

    def order_food(self):
        mainForm().show()



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
