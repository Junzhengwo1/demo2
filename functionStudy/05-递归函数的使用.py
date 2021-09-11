# 递归函数使用
def test():
    print("test")


count = 0


def demo():
    global count
    count += 1
    print('demo')
    if count < 5:
        demo()


demo()

# 求1到n的和
s = 1


def sum_one_to_n(n):
    if n == 0:
        return 0
    return n + sum_one_to_n(n - 1)


print(sum_one_to_n(6))


# 使用递归 n!

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 匿名函数的使用
# 调用方式 1、给他起个名字
#         2、把这个函数当作参数 传给另一个函数使用
lambda n, m: n + m


def calc(a, b, fn):
    return fn(a, b)


def add(n, m):
    return n + m


def sub(n, m):
    return n - m


# 回调函数
print(calc(2, 3, add))
print(calc(2, 3, sub))

print(calc(2, 3, lambda x, y: x * y))
