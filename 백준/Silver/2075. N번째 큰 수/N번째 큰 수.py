import heapq

N = int(input())
table = []

# N x N 표의 수를 읽어와서 heapq에 저장
for _ in range(N):
    row = list(map(int, input().split()))
    for num in row:
        heapq.heappush(table, num)
        # table에는 현재까지 가장 작은 N개의 수가 저장됩니다.
        if len(table) > N:
            heapq.heappop(table)

# N번째로 큰 수 출력
print(table[0])
