class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__height = 100  # 私有属性也是不可以继承的

    def sleep(self):
        print(self.name + "正在睡")

    def __bark(self):  # 私有方法是无法继承的
        print(self.name + '正在叫')


class Cat(Animal):
    pass

