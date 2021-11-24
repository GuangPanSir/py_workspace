import random
import csv

from PyQt5.QtWidgets import *
from food import Ui_Dialog
import sys

from PyQt5.QtCore import QTimer

with open("food.csv", "r", encoding="utf8") as f1:
    my_data = list(csv.reader(f1))
my_len = len(my_data)
my_food = []


def first_floor(data):
    return data[1] == "一楼"


def second_floor(data):
    return data[1] == "二楼"


list_1 = list(filter(first_floor, my_data))
list_2 = list(filter(second_floor, my_data))


class MainForm(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("自助点餐")
        self.label.setText("吃什么呢")
        self.comboBox.addItems(["2楼", "1楼"])
        self.my_timer = QTimer()
        self.my_timer.timeout.connect(self.order)

    def order(self):
        my_food_id = random.randint(0, len(my_food) - 1)
        self.label.setText(my_food[my_food_id][2])

    def start(self):
        self.my_timer.start(50)

    def end(self):
        self.my_timer.stop()

    def select_floor(self):
        global my_food
        floor = self.comboBox.currentText()
        if floor == "1楼":
            my_food = list_1
        else:
            my_food = list_2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
