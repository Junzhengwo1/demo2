# 内置属性相关
# __slots__
# 笔记
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


p1 = Person('kou', 18)
print(dir(p1))  # 对应对象的属性和行为都打印出来
print(p1.__class__)
print(p1.__dict__)
p2 = Person('jia', 20)
