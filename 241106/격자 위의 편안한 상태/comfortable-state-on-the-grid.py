n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
dx,dy = [-1,0,1,0], [0,1,0,-1]

def in_range(x, y):
    return x>=0 and y>=0 and x<n and y<n

for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    dirr = 0
    count = 0
    matrix[r][c] = 1
    
    while dirr < 4:
        nr, nc = r + dx[dirr], c + dy[dirr]
        if in_range(nr,nc) and matrix[nr][nc] != 0:
            count += 1
        dirr += 1

    if count == 3:
        print(1)
    else:
        print(0)