class Dog(object):
    def __init__(self, name, age,sex='cixing'):
        self.name = name
        self.age = age


d = Dog('球球', 2)
print("我家狗叫{0}，{1}岁了".format(d.name, d.age))