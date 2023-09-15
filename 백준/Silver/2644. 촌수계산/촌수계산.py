from collections import deque

def bfs(t1, t2):
    v[t1] = True
    q = deque([(t1, 0)])

    while q:
        current, distance = q.popleft()

        if current == t2:
            return distance

        for next in g[current]:
            if not v[next]:
                q.append((next, distance + 1))
                v[next] = True

    return -1

n = int(input())
t1, t2 = map(int, input().split())
m = int(input())

g = [[] for _ in range(n + 1)]
v = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)  # 양방향 간선 추가

result = bfs(t1, t2)
print(result)
