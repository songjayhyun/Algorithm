n = int(input())
cows = {}
answer = 0
for _ in range(n):
    cow, road = map(int, input().split(" "))
    if cow not in cows.keys():
        cows[cow] = road
        continue
    if road != cows[cow]:
        answer += 1
        cows[cow] = road
print(answer)
