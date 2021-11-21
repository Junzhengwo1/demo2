# class PoliceDog(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def attack_enemy(self):
#         print(self.name + "正在攻击人……")
#
#
# class Person(object):  # 继承Animal
#     def __init__(self, name, age, dog):
#         self.name = name
#         self.age = age
#         self.dog = dog
#
#     def work_with_pd(self):
#         print(self.name + '正在工作……')
#         self.dog.attack_enemy()
#
#
# pd = PoliceDog("a", 13)
# police = Person("king", 21, pd)
# police.work_with_pd()

class Dog(object):

    def work(self):
        print("狗正在工作")


class PoliceDog(Dog):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(self.name + "正在攻击人……")


class BlindDog(Dog):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(self.name + "正在领路……")


class DrugDog(Dog):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(self.name + "正在搜毒……")


class Person(object):
    def __init__(self, name, age):
        self.dog = None
        self.name = name
        self.age = age
        #  self.dog=dog

    def work_with_dog(self):
        self.dog.work()


pd = PoliceDog("a", 13)
police = Person("king", 21)
police.dog = pd
police.work_with_dog()
