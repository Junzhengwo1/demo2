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

# 输入任意数 求是几位数
count = 0
num = int(input("请输入一个数字："))
while True:
    count += 1
    num //= 10
    if num == 0:
        break
print(count)

# 打印水仙花数
for i in range(100, 1000):
    ge = i % 10  # 个位数
    shi = i // 10 % 10  # 十位数
    bai = i // 100  # 百位数
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i)

# 求素数即质数
for i in range(2, 100):
    flag = True  # 假设每次 i 都是质数
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, "是质数")

# 求斐波那契数的第12个数
# 1，1，2，3，5，8，13，21，34……
num1 = 1
num2 = 1
for i in range(0, 12-2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)

# 求斐波那契数列中第n个数的值，n是正整数
n = int(input("请输入你想知道第几个数的值 n："))
num1 = 1
num2 = 1
for i in range(0, n-2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)

