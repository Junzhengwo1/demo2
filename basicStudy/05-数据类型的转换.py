# 类型转换
# int -> Str
f = 20
g = str(f)
print(type(g))
print(str(f))

# Str -> int
a: str = '18'
b = '20'
k = int(b)
print(type(k))
print(int(b))
# 将 x = '1a2c' 字符串当作十六进制转换成Int
x = '1a2c'
y = int(x, 16)
print(y)

# int -> bool  除了零 其他是转换都是True
print(bool(100))
# str -> bool 只有空字符串转换成bool时候是 False  None也是False

# int -> float
v = 20
print(float(v))
# str -> float
m = '12.8'
print(float(m))
