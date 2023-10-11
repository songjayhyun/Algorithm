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

        dx = [-1,1,x]

        for i in range(3):
            nx = x + dx[i]

            if 0 <= nx <= 100000 and not visited[nx]:
                q.append((nx,time+1))
                visited[nx] = True

def find_ways(i, j, fastest_time):

    visited = [False for _ in range(1000001)]
    count = 0

    visited[i] = True
    q = deque([(i,0)])

    while q:
        x, time = q.popleft()

        if x == j and time == fastest_time:
            count += 1

        dx = [-1,1,x]
        
        visited[x] = True

        for i in range(3):
            nx = x + dx[i]

            if 0 <= nx <= 100000 and not visited[nx]:
                q.append((nx,time+1))
                
    return count

time = bfs(N,K)
print(time)
print(find_ways(N,K,time))