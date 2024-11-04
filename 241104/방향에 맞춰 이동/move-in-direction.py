n = int(input())


dx = [1,0,-1,0]
dy = [0,1,0,-1]


x = 0
y = 0


for _ in range(n):
    char, num = input().split()
    num = int(num)
    if char == 'W':
        move_dir = 2
    elif char == 'N':
        move_dir = 1
    elif char == 'E':
        move_dir = 0
    else:
        move_dir = 3

    x += dx[move_dir] * num
    x += dy[move_dir] * num


print(x,y)