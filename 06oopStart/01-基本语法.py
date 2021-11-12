# 面向对象的基本语法
# 类名大驼峰

# class Student(object):
#     pass


class Student:
    __slots__ = ('name', 'age', 'height')  # 规定对象里面可以定义的属性
    # 定义属性的

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print("正在跑步")

    def eat(self):
        print("在吃饭")


stu = Student('kou', 23, 175)
stu2 = Student("queen", 20, 165)

stu.run()
stu2.eat()
print(stu.name)
