class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + "正在睡")


class Dog(Animal):  # 继承Animal
    def bark(self):
        print(self.name + '正在叫')


class Cat(Animal, Dog):  # python可以多继承
    pass


dog = Dog("k", 20)
dog.sleep()
