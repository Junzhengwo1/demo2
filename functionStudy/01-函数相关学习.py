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


print(add(1, 2) * 2)
