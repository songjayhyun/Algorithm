from collections import deque

def bfs():
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]

    visited[0][0][0] = True
    q = deque([(0, 0, 1, 0)])  # (x, y, count, break_cnt)

    while q:
        x, y, count, break_cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            return count

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and not visited[nx][ny][break_cnt]:
                    visited[nx][ny][break_cnt] = True
                    q.append((nx, ny, count + 1, break_cnt))
                elif maps[nx][ny] == 1 and break_cnt == 0:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, count + 1, 1))

    return -1

n, m = map(int, input().split())
visited = [[[False, False] for _ in range(m)] for _ in range(n)]
maps = []

for i in range(n):
    maps.append(list(map(int, input().strip())))

print(bfs())
