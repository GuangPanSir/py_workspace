class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def show_info(self):
        print("动物的名字:{0}".format(self.name))
    
    def move(self):
        