import sys
from collections import Counter

T = int(input())
clothes = {}

for _ in range(T):
    N = int(input())
    ans = 1

    for _ in range(N):
        thing, kind = input().split()
        
        if kind not in clothes.keys():
            clothes[kind] = []

        clothes[kind].append(thing)

    l = list(Counter(clothes).values())

    for i in range(len(l)):
        length = len(l[i])
        ans *= (length + 1)
        
    clothes.clear()

    print(ans-1)