#  函数相关学习
# 使用# def 来定义函数
def tell_story():
    print("寇王")


def speak(k):
    print("kou", k)


a = 3
if a < 5:
    for i in range(5):
        tell_story()

a = 3
s = "hand"
if a < 5:
    for i in range(3):
        speak(s)


def add(j, b):
    c = j + b
    return c


def test1():
    print("test1开始了")


def test2():
    print("test2开始了")
    test1()


test2()

print(add(1, 2) * 2)


# 求[n，m)之间所有整数之和
def add(n, m):
    x = 0
    for g in range(n, m):
        x += g
    return x


print(add(2, 9))


# 求一个n的阶乘
def factorial(n):
    x = 1
    for j in range(1, n + 1):
        x *= j
    return x


print(factorial(3))


