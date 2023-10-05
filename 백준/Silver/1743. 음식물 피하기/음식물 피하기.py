from collections import deque

n,m,k = map(int, input().split())

def bfs(i,j):
    count = 1
    visited[i][j] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([(i,j)])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and maps[nx][ny] == 1:
                q.append((nx,ny))
                count += 1
                visited[nx][ny] = True

    return count
    
maps = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    maps[a-1][b-1] = 1

answer = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == False:
            answer.append(bfs(i,j))

print(max(answer))