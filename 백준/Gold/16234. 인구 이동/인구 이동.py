from collections import deque

def bfs(i,j):
    visited[i][j] = True
    q = deque([(i,j)])
    allias = deque([(i,j)])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                visited[nx][ny] = True
                q.append((nx,ny))
                allias.append((nx,ny))

    return allias

N,L,R = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

cnt = 0
while True:

    visited = [[False for _ in range(N)] for _ in range(N)]
    l = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                allias = bfs(i,j)
                if len(allias) != 1:
                    l.append(allias)
    
    if not l:
        break

    for allias in l:
        sum = 0
        for x,y in allias:
            sum += maps[x][y]
        peo = sum // len(allias)
        for x,y in allias:
            maps[x][y] = peo

    cnt += 1

print(cnt)
