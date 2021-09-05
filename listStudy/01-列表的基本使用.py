# 列表的基本使用 也就是java 的数组
names = ['kou', 'jia', 'king', 'jun', 'king']  # 可以使用切片
names = list(names)
names[2] = 'queen'
print(names)

'''
操作列表（数组）
'''
# 在随后面追加添加元素
names.append('king')
print(names)
# 插如元素
names.insert(3, 'hou')
print(names)
names2 = ['jun', 'zheng', 'wo']
names.extend(names2)  # 将names2 加到 names中
print(names)

# 删除元素
names.pop()  # 默认删除列表的最后的数字
print(names)
names.pop(6)  # 删除指定下标的数据
print(names)
names.remove('hou')  # 如果删除的元素不存在的 就会报错
print(names)
print(names2)
names2.clear()
print(names2)

s = ['kou', 'jia', 'king', 'jun', 'king']
# 查询相关的方法
print(names.index("kou"))
print(names.index("jun"))
print(s.count("king"))

# 修改相关
s[2] = 'queen'
print(s)
