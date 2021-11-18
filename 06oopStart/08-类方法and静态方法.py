class Person:
    type = 10

    @staticmethod
    def demo():
        print("hello")

    @classmethod
    def test(cls):
        print(cls.type + 10)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 实例方法
        print(self.name + '正在吃' + food)


p = Person("king", 10)
Person.demo()  # 静态方法的调用方法
p.eat("面包")
p.test()
Person.test()