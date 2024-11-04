def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

n, t = map(int, input().split())

r,c,d = input().split()
r = int(r)
c = int(c)
dy, dx = [1,0,0,-1],[0,1,-1,0]
dict = {
    'R':0,
    'U':2,
    'D':1,
    'L':3
}

dirr = dict[d]

while t>0:
    nr, nc = r+dx[dirr], c+dy[dirr]
    if not in_range(nr,nc):
        dirr = 3 - dirr
    else:
        r,c = nr, nc
    t -= 1
    
print(r + 1,c + 1)