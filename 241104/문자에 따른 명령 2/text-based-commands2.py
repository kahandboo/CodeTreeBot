string = input()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3

x = 0
y = 0

for i in string:
    if i == 'L':
        dir_num = (dir_num + 3)%4
    elif i == 'R':
        dir_num = (dir_num + 1)%4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x,y)