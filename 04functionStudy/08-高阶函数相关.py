# 高阶函数相关
# 1、一个函数作为另一个函数的返回值
# 2、一个函数作为另一个函数的参数（lambda 的使用场景）
# 3、 在一个函数的里面定义另一个函数

def foo():
    print("我是Foo")
    return 'foo'


# def bar():
#     print("我是bar")
#     return foo()
def bar():
    print("我是bar")
    return foo


def outer():
    m = 100

    def inner():  # 内部函数数 只能在函数内部使用
        n = 90
        print("inner")

    inner()
    print("outer")


print(type(bar()))
print(bar()())

outer()
