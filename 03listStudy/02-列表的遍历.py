# 列表的遍历 即数组的遍历
s = ['kou', 'jia', 'king', 'jun', 'king']
for a in s:
    print(a)

print("------------")
i = 0
while i < len(s):
    print(s[i])
    i += 1

# 带下标的遍历
for a in enumerate(s):
    print(a)