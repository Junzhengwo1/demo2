# 把对象当作字典来使用 __setitem__
# __gititem__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('w', 18)

print(p.__dict__)
