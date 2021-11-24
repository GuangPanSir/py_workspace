class Dog(object):
    def __init__(self, name, age, sex='雌性'):
        self.name = name
        self.age = age
        self.sex = sex
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = sex

d = Dog('球球', 2)
print("我家狗叫{0}，{1},{2}岁了".format(d.name, d.sex, d.age))
