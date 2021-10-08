# 对象属性和类属性

class Person:  # Person就是类对象
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('kou', 23)  # p就是实例对象
q = Person('king', 20)

