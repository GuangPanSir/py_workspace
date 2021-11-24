class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def show_info(self):
        print("动物的名字:{0}".format(self.name))

    def move(self):
        print("动一动......")


class Cat(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

    # 父类方法重写
    def move(self):
        print("动两动......")


cat = Cat('Tom', 2)
cat.move()
cat.show_info()

#多继承
class Horse:
    def __init__(self, name):
        self.name = name
    
    def show_info(self):
        return "马的名字:{0}".format()
        