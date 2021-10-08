# 魔法方法 是类里面的特殊方法 （在合适的时候自动调用）__fn__ 都是系统规定好的


class Person(object):
    def __init__(self, name, age):  # 这个方法就是魔法方法(有点像Java的构造方法)
        self.name = name
        self.age = age

    def __str__(self):  # (有点像Java的重写toString())
        return '姓名：{},年龄：{}'.format(self.name, self.age)
    # def __del__(self):  # 对象销毁是 自动调用
    #     pass


p = Person('k', 56)

print(p.age)
print(p)
