from collections import deque

def fir(i,x):
    if i[x-1] == 0:
        i[x-1] = 1
    return i

def sec(i,x):
    if i[x-1] == 1:
        i[x-1] = 0
    return i

def thi(i):
    if i[19] == 1:
        i[19] = 0
    d = deque(i)
    d.rotate(1)
    return list(d)

def fou(i):
    if i[0] == 1:
        i[0] = 0
    d = deque(i)
    d.rotate(-1)
    return list(d)

n,m = map(int, input().split(" "))
trains = [[0 for _ in range(20)] for _ in range(n)]

for _ in range(m):
    cmds = list(map(int, input().split(" ")))
    train = trains[cmds[1]-1]
    if cmds[0] == 1:
        trains[cmds[1]-1] = fir(train, cmds[2])
    elif cmds[0] == 2:
        trains[cmds[1]-1] = sec(train, cmds[2])
    elif cmds[0] == 3:
        trains[cmds[1]-1] = thi(train)
    elif cmds[0] == 4:
        trains[cmds[1]-1] = fou(train)

l = []
ans = 0
for train in trains:
    if train not in l:
        ans += 1
        l.append(train)

print(ans)