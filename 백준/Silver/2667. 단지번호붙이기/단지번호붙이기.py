import sys
sys.setrecursionlimit(1000000)

homes = []

def dfs(x,y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True
    size = 1 

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
            size += dfs(nx, ny)
    return size

n = int(input())

graph = []
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))



for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            homes.append(dfs(i,j))

print(len(homes))
homes.sort()
for h in homes:
    print(h)