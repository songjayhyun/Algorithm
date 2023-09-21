def cal_strike(l1, l2):
    strike = 0

    for a,b in zip(l1, l2):
        if a == b:
            strike += 1
    return strike

def cal_ball(l1, l2):
    ball = 0

    for a,b in zip(l1, l2):
        if a == b:
            continue
        else:
            if a in l2:
                ball += 1
    return ball

N = int(input())
l = []

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i != j and j != k and i != k:
                l.append(i*100+j*10+k)

exs = []
for _ in range(N):
    num, s, b = map(int, input().split())
    exs.append([num,s,b])

answer = []
for i in l:
    i = str(i)
    for j in exs:
        j[0] = str(j[0])
        if cal_strike(i,j[0]) != j[1]:
            break

        if cal_ball(i,j[0]) != j[2]:
            break
    else:
        answer.append(i)

print(len(answer))