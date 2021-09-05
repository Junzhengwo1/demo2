# 元组集合字典相关操作
kou = (1, 2, 3, 4, 5, 6, 1)  # 元组是不可变的数据类型
print(kou.index(2))  # 找下标
print(kou.count(1))  # 对应的元素出现的次数
# 如何表示 只有一个元素的元组？
a = (18,)
print(type(a), a)
# 元组与列表之间的转换
words = ['kou', 'jia', 'jun']
print(tuple(words))
print(list(kou))
for you in words:
    print(you)

# 两个元组的合并
m = (1, 2, 3)
n = (4, 5, 6)
print('元组的合并', m + n)

# 字典相关操作  相当于java的map key不允许重复
person = {'name': 'king',
          'age': 23,
          'height': 175,
          'like': ['1', '2', '3']}
print(person)
print(person.get("name"))  # 如果key 不存在会默认返回None
print(person.get('age'))
print(person.values())
# 字典的遍历
print(person.keys())
for a in person.values():
    print(a)
for b in person.get('like'):
    print(b)
for item in person.items():
    print(item[0], '=', item[1])
for k, v in person.items():
    print('拆包', k, v)
for c in person:  # 字典的遍历
    if c.__eq__('like'):
        for k in person.get(c):
            print(k)
    print(c)
# 字典新增和修改
person['height'] = 180  # 如果字典中有key就会修改val 如果没有key 就会新增key
print(person)
# 字典的删除  clear清空字典
person.pop('age')  # 删除键值对
print(person)
result = person.popitem()  # 删除某一个条目 返回值 就是对应删除的键值对，以元组的形式展示
print(person)
print(result)

person2 = {'k': 'king', 'g': 456}
person.update(person2)  # update 方法就是 将两个字典合并成一个字典
print(person)

# 计算相同字符的个数 并拿到最多的值
chars = ['a', 'b', 'c', 'a', 'k', 'a', 'c']
char_count = {}
for c in chars:
    # if c in char_count:
    #     char_count[c] += 1
    # else:
    #     char_count[c] = 1
    if c not in char_count:
        char_count[c] = chars.count(c)
print(char_count)

print(max(char_count.values()))
for k, v in char_count.items():
    if v == max(char_count.values()):
        print(k)
