from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(1000001)]

def bfs(i, j):

    visited[i] = True
    q = deque([(i,0)])

    while q:
        x, time = q.popleft()

        if x == j:
            return time

        dx = [-1,1,x]

        for i in range(3):
            nx = x + dx[i]

            if 0 <= nx <= 100000 and not visited[nx]:
                q.append((nx,time+1))
                visited[nx] = True
    return -1

print(bfs(N,K))
