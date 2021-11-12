# sort 函数的相关使用
# 内置函数和内置类，的匿名函数的使用
a = [1, 8, 0, 1, 10, 88]
a.sort()
print(a)
print(sorted(a))  # sorted就是一个内置函数，且使用了匿名函数

persons = [{'name': 'kou', 'age': 20, 'height': 177},
           {'name': 'king', 'age': 21, 'height': 178},
           {'name': 'queen', 'age': 22, 'height': 173}]


def self_sort(ele):
    return ele['height']


persons.sort(key=self_sort)
print(persons)

persons.sort(key=lambda ele: ele['name'])
print(persons)
