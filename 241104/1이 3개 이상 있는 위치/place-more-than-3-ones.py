def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]


dx, dy = [1,0,-1,0],[0,-1,0,1]
result = 0

for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if in_range(nx,ny) and matrix[nx][ny] == 1:
                count += 1
        if count >= 3:
            result += 1
        


print(result)