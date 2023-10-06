import sys
input = sys.stdin.readline

n,l = map(int, input().split())

muds = [(list(map(int, input().split()))) for _ in range(n)]
muds.sort(key=lambda x:x[0])
ans = 0
plank = muds[0][0]

for s,e in muds:
    if s > plank:
        plank = s
    diff = e - plank
    if diff % l == 0:
        count = diff // l
        plank = e
    else:
        count = diff // l + 1
        plank = e + (l-diff%l)
    
    ans += count
print(ans)