# 冒泡排序
a = [8, 7, 6, 5, 4, 3]

# 去掉空字符串
k = ["kou", '', 'king', '', 'jun', '']
# for word in k:  # 最好不要用for循环去执行删除操作，因为下标会变
#     if word == '':
#         k.remove(word)

# 逆向处理
words = []
for w in k:
    if w != '':
        words.append(w)
print(words)

print(k)
# 推荐使用 while 循环来
i = 0
while i < len(k):
    if k[i] == '':
        k.remove(k[i])
        i -= 1
    i += 1
print(k)

# 找打最大的值
x = a[0]
for u in a:
    if u > x:
        x = u
print(x)

# 第一步
n = 0
while n < len(a) - 1:
    if a[n] > a[n + 1]:
        a[n], a[n + 1] = a[n + 1], a[n]
    n += 1
print(a)

# 第二步
count = 0
i = 0
while i < len(a) - 1:
    flag = True
    count += 1
    n = 0
    while n < len(a) - 1 - i:
        if a[n] > a[n + 1]:
            flag = False
            a[n], a[n + 1] = a[n + 1], a[n]
        n += 1
    if flag:
        break
    i += 1
print(a)
print(count)
