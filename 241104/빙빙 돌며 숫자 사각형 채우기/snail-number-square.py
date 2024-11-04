def in_range(x,y):
    return x >=0 and y>=0 and x<n and y<m
n,m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
dx, dy = [0,1,0,-1], [1,0,-1,0]

dirr = 0
x ,y = 0,0
matrix[x][y] = 1

for i in range(2,n*m+1):
    nx, ny = x+dx[dirr], y+dy[dirr]
    if not in_range(nx,ny) or matrix[nx][ny] !=0:
        dirr = (dirr + 1)%4

    x,y = x+dx[dirr], y+dy[dirr]
    matrix[x][y] = i

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = ' ')
    print()