# while python 不支持 do while 循环

x = 0
while x < 10:
    print(x)
    x += 2  # python 不支持++

# 求1~100之间偶数的和
i = 0
sm = 0
while i < 100:
    i += 2
    sm = sm + i
print(sm)
# 求35 到 987 之间所有的值

# python 的for 循环 就是值 for  in 循环
# 打印 1，10 的数字
for i in range(1, 11):  # in后面必须要放可迭代的对象 如 列表；字典；元组；集合等
    print(i)

for y in 'kou':
    print(y)

res = 0
for i in range(1, 101):
    res += i
print(res)

# break 和 continue关键字的学习  在python 中 只能用在循环语句中

# 嵌套学习

i = 0
while i < 5:
    i += 1
    print(i*'*')

# 打印矩形 外循环控制行数 内循环控制列数
j = 0
while j < 10:
    j += 1
    # 把下面这个当作整体
    i = 0
    while i < 5:
        i += 1
        print("*", end=' ')
    print()

# 打印三角形*
j = 0
while j < 10:
    j += 1
    # 把下面这个当作整体
    i = 0
    while i < j:
        i += 1
        print("*", end=' ')
    print()

# 打印出九九乘法表
j = 0
while j < 9:
    j += 1
    # 把下面这个当作整体
    i = 0
    while i < j:
        i += 1
        print(i, '*', j, '=', i * j, sep="", end='\t')
    print()


