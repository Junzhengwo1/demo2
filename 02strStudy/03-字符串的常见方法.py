# 字符串的常见方法
m = 'kou.jia.jun'
n = 'kou'
j = '100'
# 获取长度的内置函数
print(len(m))
# 查找相关大方法 find/index/rfind/rindex
print(m.find('j'))
print(m.rfind('j'))  # 找到下标最大的
print(m.find('a', 3, 7))  # 返回值为下标 从第几个找到第几个
print(m.find('l'))  # 如果找不到的话 返回-1
print(m.index('a'))  # 也是返回的下标 （找不到的话 直接报错）
# 判断相关方法 startswith/endswith/isalpha/isdigit……
print(m.startswith('k'))
print(m.isalpha())
print(n.isalpha())  # 是否是字母
print(m.isdigit())  # 是否是数字
print(j.isdigit())
# 字符串的替换 replace
k = m.replace('.', ':')
print(m.replace('.', ':'))
print(k)
print(m)
# 内容分割 split splitlines partition rpartition
u = m.split('.', 1)  # 分割成列表 分割一次
print(u)
print(m.rsplit('.', 1))
x = 'koukingjiajun'
print(x.partition("king"))  # 分割成元组

'''
# 修改大小写
'''
print(m.capitalize())  # 修改首字母为大写
print(m.upper())  # 全部改为大写

# 格式化字符串
print('大家好，我是{}，我今年{}岁了'.format('kou', 23))
print('大家好，我是{1}，我今年{0}岁了'.format(23, 'kou'))
d = ['kou', 23, '成都']
b = '我是{}，今年{}岁，来自{}'.format(*d)  # 自动拆包
print(b)
