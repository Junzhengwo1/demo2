# 随机分配老师问题
import random
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)
