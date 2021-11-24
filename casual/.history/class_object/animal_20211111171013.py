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


cat = Cat('Tom', 2)
cat.move()
