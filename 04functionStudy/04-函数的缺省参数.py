# 函数的参数相关
def say_hello(name, age):
    print("我是{}，今年{}".format(name, age))


say_hello('kou', 23)


def say_hello(name, age, city='chengdu'):  # 默认参数 就是在给对应参数赋一个值且放在最后面
    print("我是{}，今年{},来自{}".format(name, age, city))


say_hello('king', 25)
say_hello('queen', age=12, city='lou')


# 可变参数
def add_many(m):
    sumac = 0
    for n in m:
        sumac += n
    return sumac


a = (1, 2, 34, 5, 6, 7)
print(add_many(a))


def add(*args):
    print(args)
    s = 0
    for ak in args:
        s += ak
    return s


print(add(1, 3, 4))
