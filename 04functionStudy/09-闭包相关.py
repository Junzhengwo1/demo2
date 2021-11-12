# 闭包相关
def outer():
    x = 10

    def inner():  # 内部函数数 只能在函数内部使用
        nonlocal x
        y = x + 1
        print("inner")
        return y

    print(inner())
    print("outer")


outer()
