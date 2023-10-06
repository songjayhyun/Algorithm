from collections import Counter

n,c = map(int, input().split())
l = list(map(int, input().split()))
ans = []
l = sorted(list(Counter(l).items()), key=lambda x:x[1], reverse=True)

for k, v in l:
    for _ in range(v):
        ans.append(k)

print(*ans)