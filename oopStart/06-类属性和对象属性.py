# 对象属性和类属性  就像是java的全局变量和局部变量。

class Person:  # Person就是类对象

    # eg：
    type = "wa"

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('kou', 23)  # p就是实例对象
q = Person('king', 20)

# 类属性可以通过类对象和实例对象来获取
print(Person.type)
print(p.type)

p.type = "human"  # 这个不是把类属性修改了，而是在实例对象新增这个属性
