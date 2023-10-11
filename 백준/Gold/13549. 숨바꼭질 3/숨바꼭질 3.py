from collections import deque

N, K = map(int, input().split())
times = []

def bfs(i, j):

    visited = [False for _ in range(1000001)]

    visited[i] = True
    q = deque([(i,0)])

    while q:
        x, time= q.popleft()

        if x == j:
            return time

        dx = [x,-1,1]

        for i in range(3):
            nx = x + dx[i]

            if 0 <= nx <= 100000 and not visited[nx]:
                if dx[i] == x:
                    q.append((nx,time))
                else:
                    q.append((nx,time+1))
                visited[nx] = True

print(bfs(N,K))