# 导入模块相关
import math
# from math import *
import datetime
# from datetime import *
import os
import sys
import random
import time
import hashlib
import hmac
from flask import Flask
print(math.pi)
# os模块
print(os.name)  # nt 获取操作系统的名字 nt 即是说windows
print(os.path.abspath('01-导入模块相关.py'))
print(os.path.isdir('01-导入模块相关.py'))  # False
print(os.path.splitext('01-导入模块相关.py'))
# sys模块 做了解

# math 模块
print(math.pow(2, 3))  # 幂运算
print(math.factorial(6))
print(math.floor(12.98))  # 向下去整
print(math.ceil(12.98))

print(math.sin(math.pi / 6))  # sin30度
# random模块
print(random.randint(1, 9))
print(random.random())  # 0,1 的随机浮点数
words = ['kou', 'jia', 'jun']
print(random.choice(words))
print(random.sample(words, 2))

# datetime
print(datetime.datetime.now())
s = datetime.date.today().year
print(s)

print(datetime.date(2021, 9, 12))
print(datetime.time(13, 12, 45))

# time
print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.ctime())
print(time.asctime())
print(time.localtime())


# hashlib模块 hmac模块 加密模块
x = hashlib.md5()
x.update('123'.encode('utf8'))
print(x.hexdigest())

