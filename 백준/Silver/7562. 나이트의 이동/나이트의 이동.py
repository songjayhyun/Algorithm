from collections import deque

T = int(input())
d = [(1,-2),(2,-1),(-1,-2),(-2,-1),(1,2),(2,1),(-2,1),(-1,2)]

def bfs(s1,s2,t1,t2):
    visited[s1][s2] = True
    q = deque([(s1,s2,0)])

    while q:
        x,y,count = q.popleft()

        if x == t1 and y == t2:
            return count
            break

        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                q.append((nx,ny,count + 1))
                visited[nx][ny] = True
    return -1

for _ in range(T):
    n = int(input())
    maps = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))

    cnt = bfs(start[0], start[1], target[0], target[1])
    print(cnt)