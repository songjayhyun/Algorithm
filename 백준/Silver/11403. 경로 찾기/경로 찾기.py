def dfs(graph, visited, n, start, end):
    visited[start][end] = 1  # 현재 정점에서 시작하여 end 정점에 도달할 수 있는 경우 1로 표시

    for i in range(n):
        if graph[end][i] == 1 and visited[start][i] == 0:  # end 정점에서 i 정점으로 갈 수 있는 경우
            dfs(graph, visited, n, start, i)

n = int(input())
graph = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [[0] * n for _ in range(n)]  # visited 배열 초기화

    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(graph, visited, n, i, j)

    # 결과 출력
for i in range(n):
    for j in range(n):
        print(visited[i][j], end=' ')
    print()