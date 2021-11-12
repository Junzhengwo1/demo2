# 基本数据类型：(在python中变量是没有数据类型的)
# Numbers
# Int
# float
# long (python 3 已经不用这个东东了)
# complex
# 布尔类型
# String
# Set
# Tuple
# Dictionary
from typing import Tuple

a = 80
print(a)
print(3.1415926)
print((-1) ** 0.5)  # 复数
b = 'king'
print(b)
print(4 > 3)

# list 列表就像是数组
names = ['king', 'queen']
print(names)

# 字典类型 map
person = {'name': 'king', 'age': 81}
print(person)
print(person.values())
print(person.get('name'))  # 有点像java的map
# 元组类型
nums: Tuple[int, int, int] = (1, 3, 4,)
print(nums)
# Set
X = {9, 'kou,', True}
print(X)
print(X.pop())

# 查看数据类型
print(type(X))
print(type(names))
print(type(a))
print(type(nums))
print(type(person))
print(type(b))
print(type(3.1415926))

# 标识符和关键字
# 变量、模块名、函数名、类名 （由数字字母下划线组成-不能以数字开头-不能使用关键字）


