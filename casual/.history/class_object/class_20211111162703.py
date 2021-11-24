class Dog(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

# 函数重载
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    def run(self):
        print("{0}在跑......".format())

d = Dog('球球', 2)
print("我家狗叫{0}，{1},{2}岁了".format(d.name, d.sex, d.age))
