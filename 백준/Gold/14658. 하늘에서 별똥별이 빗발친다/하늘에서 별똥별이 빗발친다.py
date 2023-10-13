def counting_stars(i, j):
    cnt = 0
    for star in stars:
        if i<=star[0]<=i+L and j<=star[1]<=j+L:
            cnt += 1
    return cnt

N, M, L, K = map(int, input().split())
res = 0
stars = []

for i in range(K):
    x, y = map(int, input().split())
    stars.append([x, y])

for i in stars:
    for j in stars:
        res = max(res, counting_stars(i[0],j[1]))

print(K-res)