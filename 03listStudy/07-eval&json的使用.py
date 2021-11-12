import json

# eval & json的使用
k = {5, 2, 7, 9, 2, 8}
x = set(k)
y = list(x)
y.sort(reverse=True)
print(y)

# 内置类的一些转换方法 内置函数 eval
# print(eval('input("请输入一个数据")'))
person = {'name': 'king',
          'age': 23,
          'height': 175,
          'like': ['1', '2', '3']}
print(json.dumps(person))       # 集合不能转成JSON
s = '{"name": "king", "age": 23}'
print(json.loads(s))
