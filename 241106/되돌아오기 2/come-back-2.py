s = input()
x,y = 0, 0
dx,dy = [0,1,0,-1], [1,0,-1,0]
time = 0
dirr = 0

for i in s:
    time += 1
    if i == 'L':
        dirr = (dirr + 3)%4
    elif i == 'R':
        dirr = (dirr + 1)%4
    else:
        x,y = x+dx[dirr], y+dy[dirr]
        if x ==  0 and y == 0:
            print(time)
            exit()
    
print(-1)