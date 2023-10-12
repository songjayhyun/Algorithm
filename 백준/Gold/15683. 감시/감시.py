import copy

n,m = map(int, input().split())
office = []
cctv = []

case = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3,],[0,2,3]],
    [[0,1,2,3]]
]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j], i, j])
        
def fill(office, case, x, y):
    for i in case:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            
            if office[nx][ny] == 6:
                break
            
            if office[nx][ny] == 0:
                office[nx][ny] -= 1

def dfs(depth, arr):
    global ans
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        ans = min(ans,count)
        return
    
    tmp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in case[cctv_num]:
        fill(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(arr)

ans = int(1e9)
dfs(0, office)
print(ans)