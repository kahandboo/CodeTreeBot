n = int(input())
dx,dy = [-1,0,0,1], [0,1,-1,0]

mydict = {
    'W':0,
    'S':1,
    'N':2,
    'E':3
}

x,y = 0,0
time = 0

for _ in range(n):
    dirr, dis = input().split()
    dis = int(dis)
    dirr_num = mydict[dirr]

    

    while dis > 0:
        x, y = x + dx[dirr_num], y + dy[dirr_num]
        time += 1
        dis -= 1
        if x == 0 and y == 0:
            print(time)
            exit()

if x != 0 or y!=0 :
    print(-1)