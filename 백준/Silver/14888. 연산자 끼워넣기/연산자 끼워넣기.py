maximum = -int(1e9)
minimum = int(1e9)

def dfs(depth, current_sum, plus, minus, multiply, divide):
    global maximum
    global minimum

    if depth == n:
        maximum = max(maximum, current_sum)
        minimum = min(minimum, current_sum)
        return 

    if plus:
        dfs(depth+1, current_sum + l[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, current_sum - l[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, current_sum * l[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(current_sum / l[depth]), plus, minus, multiply, divide-1)

n = int(input())
l = list(map(int, input().split()))
operations = list(map(int, input().split()))

dfs(1, l[0], operations[0], operations[1], operations[2], operations[3])
print(maximum)
print(minimum)