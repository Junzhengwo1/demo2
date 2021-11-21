class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__height = 1000


class Student(Person):
    pass


p1 = Person("1", 10)
p2 = Person("2", 10)
p3 = Person("3", 10)

print(p1 is p2)  # 获取两个对象的内存地址来比较的

if type(p1) == Person:
    print("YES")

print(isinstance(p1, Person))  # 判断是否由指定的类或者父类
