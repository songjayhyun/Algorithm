import sys
from heapq import heappush, heappop
n = int(sys.stdin.readline().rstrip())
h = []
for _ in range(n):
    c = list(map(int, sys.stdin.readline().split()))
    for i in c:
        heappush(h, i)
    if len(h) > n:        
        for i in range(n):
            heappop(h)
print(h[0])