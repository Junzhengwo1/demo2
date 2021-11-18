class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__height = 1000  # 一两个下划线开头的属性就是私有属性


p = Person("king", 10)
print(p.name)

# print(p.__height) # 私有属性不能直接获取

# 获取私有属性的方法
# 1、对象._类名__私有变量
print(p._Person__height)
# 2、定义get和set方法来获取

# 3、使用property来获取

