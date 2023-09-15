from sys import stdin
import sys
sys.setrecursionlimit(1000000)


def dfs(x,y):
    if x>=n or x<= -1 or y>=m or y<=-1:
        return False
    if graph[x][y] == 1:
        graph[x][y] += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

t = int(stdin.readline())
for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    graph = [[0 for i in range(m)] for i in range(n)]
    cnt = 0
    for _ in range(k):
        a,b = map(int,stdin.readline().split())
        graph[b][a] = 1


    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)

