# 字符串的下标和切片
kou = 'king'
print(kou[2])
print(kou.index('i'))  # 显示对应字符的索引
m = 'kou.jia.jun'
print(m[::-1])  # 倒叙
print(m[0:3])  # 切片(左闭右开)
print(m[3:0:-1])
print(m[0:9:2])  # 切片中 步长不能为零（为负数的话，就是从右往左找）
for king in kou:
    print(king, end=",")
