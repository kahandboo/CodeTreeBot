def in_range(x, y, n):
    return 0 < x <= n and 0 < y <= n

n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
r -= 1
c -= 1
direction_map = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3
}

dirr = direction_map[d]

for _ in range(t):
    nr = r + dx[dirr]
    nc = c + dy[dirr]
    
    if not in_range(nr, nc, n):
        dirr = (dirr + 2) % 4
        nr = r + dx[dirr]
        nc = c + dy[dirr]

    r, c = nr, nc

print(r, c)