# 算术相关的魔法方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('kou', 18)
p2 = Person('jia', 20)

print(p1 is p2)