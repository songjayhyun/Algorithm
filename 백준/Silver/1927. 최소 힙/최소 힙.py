import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().rstrip())
h = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if not h:
            print(0)
        else:
            print(heappop(h))
    else:
        heappush(h,x)