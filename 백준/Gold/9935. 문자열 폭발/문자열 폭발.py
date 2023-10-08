import sys
input = sys.stdin.readline

s = input().rstrip()
bomb_str = input().rstrip()
stack = []

for i in s:
    stack.append(i)   

    if len(stack) >= len(bomb_str):
        if stack[-len(bomb_str):] == list(bomb_str):
            for _ in range(len(bomb_str)):
                stack.pop()

stack = "".join(stack)

if not stack:
    stack = "FRULA"

print(stack)