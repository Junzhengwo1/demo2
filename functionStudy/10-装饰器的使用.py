import time


# 装饰器的使用 todo 重点理解

# def demo():
#     x = 0
#     for i in range(1, 10000000):
#         x += i
#     print(x)


# def cal_time(fn):
#     start = time.time()
#     fn()
#     end = time.time()
#     print("时长{}".format(end - start))
# cal_time(demo)

# 装饰器来优化代码
# def cal_time_len(fn):
#     def inner():
#         start = time.time()
#         fn()
#         end = time.time()
#         print("时长{}".format(end - start))
#     return inner
#
#
# @cal_time_len
# def demo2():
#     x = 0
#     for i in range(1, 10000000):
#         x += i
#     print(x)
#
#
# demo2()

# 装饰器来优化代码 场景2
def cal_time_len(fn):
    def inner(n):
        start = time.time()
        x = fn(n)
        end = time.time()
        print("时长{}".format(end - start))
        return x, start-end
    return inner


@cal_time_len
def demo2(n):
    x = 0
    for i in range(1, n):
        x += i
    return x


print(demo2(10000000))