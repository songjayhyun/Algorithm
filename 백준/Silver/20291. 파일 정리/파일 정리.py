n = int(input())
names = {}
answer = 0
for _ in range(n):
    name = input().split(".")[1]
    if name not in names.keys():
        names[name] = 1
        continue
    names[name] += 1
names = sorted(names.items(), key = lambda x : x[0])

for key, value in names:
    print(key, value)
