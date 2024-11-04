string = input()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3
vec = string[0]
op = string[1]
x = 0
y = 0

if vec == 'L':
    dir_num = (dir_num + 3)%4
else:
    dir_num = (dir_num + 1)%4


x += dx[dir_num]
y += dy[dir_num]

print(x,y)