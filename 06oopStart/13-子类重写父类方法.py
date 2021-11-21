class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + "正在睡……")


class Dog(Animal):  # 继承Animal
    def __init__(self, name, age, height):
        # self.name = name
        # self.age = age
        # Animal.__init__(self, name, age)
        # 子类在父类实现的基础上又添加了新的功能
        super(Dog, self).__init__(name, age)
        self.height = height

    def bark(self):
        print(self.name + '正在叫……')

    def sleep(self):  # 重写父类的方法
        print(self.name + "正在课间睡……")

    # 重写父类的方法


d = Dog("king", 20, 100000000)
d.sleep()
# print(Dog.__mro__)  # 方法的调用顺序
