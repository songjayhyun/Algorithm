import sys
from collections import Counter

n = sys.stdin.readline()
c = Counter(n)
a_cnt = c['a']
b_cnt = c['b']

if a_cnt == 1 or a_cnt == len(n):
    print(0)
    exit()

l = []
answer = 0

for i in range(len(n)):
    new = n[i:] + n[:i]
    a_cnt = c['a']
    b_cnt = c['b']
    answer = 0

    for i in new:
        if i == 'a':
            a_cnt -= 1

        if a_cnt < 0 or answer > b_cnt:
            break

        if a_cnt == 0:
            break

        if i == 'b':
            answer += 1
            a_cnt -= 1
            
    l.append(answer)

print(min(l))