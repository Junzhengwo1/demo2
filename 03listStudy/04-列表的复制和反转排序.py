# 列表的排序和反转
a = [1, 4, 2, 8, 6, 5]
a.sort(reverse=True)
print(a)
print(sorted(a))  # 内置的排序函数

s = [1, 4, 2, 8, 6, 5]
s.reverse()  # 反转
print(s)

# 列表的复制
s = [1, 2, 4, 3, 5]
w = s.copy()  # copy之后就可以操作W了，地址是不同的
print(w)



