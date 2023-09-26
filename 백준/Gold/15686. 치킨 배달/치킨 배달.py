from itertools import combinations

n,m = map(int, input().split())
chicken_house = []
house = []
answer = 999999

for i in range(n):
    l = list(map(int, input().split()))
    for j,v in enumerate(l):
        if v == 1:
            house.append([i,j])
        elif v == 2:
            chicken_house.append([i,j])

for chi in combinations(chicken_house, m):
    temp = 0           
    for h in house: 
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    answer = min(answer, temp)

print(answer)