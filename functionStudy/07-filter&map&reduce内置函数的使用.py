# filter 内置函数的使用
from functools import reduce

a = [1, 8, 0, 1, 10, 88]

x = filter(lambda ele: ele > 8, a)

b = []
for k in x:
    b.append(k)
print(b)

y = map(lambda ele: ele + 2, a)
print(list(y))

print(reduce(lambda ele, m: ele + m, a))
