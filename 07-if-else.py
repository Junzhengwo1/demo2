# python 里边鼻不支持 switch...case

age = input("亲输入你的年龄：")
if int(age) < 18:
    print('未成年；禁止入内：')
else:
    print("可以进入：")

# 写出判断一个数是否能都同时被3和7整出的
num = int(input("请输入一个数字："))

if num % 4 == 0 and num % 7 == 0:
    print("能被4整出同时被7整出")

# 闰年
year = int(input("请输入一个年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("润年:")

# 计算今天总过上了多久的课
x = 3718
hour = x // 3600
minute = x % 3600 // 60
second = x % 60
print(hour, "小时", minute, "分钟", second, "秒")


