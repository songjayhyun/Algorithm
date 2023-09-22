def convertToSecond(time):
    m,s = map(int, time.split(":"))
    return m * 60 + s

def convertToString(time):
    m = str(time//60)
    s = str(time%60)
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s

    return m + ":" + s

import sys

n = int(input())
f_time = 0
s_time = 0
f_cnt = 0
s_cnt = 0

score_board = {}

for _ in range(n):
    t, score = sys.stdin.readline().split()
    score_board[convertToSecond(score)] = int(t)

for i in range(convertToSecond("48:00")):
    
    if i in score_board:
        if score_board[i] == 1:
            f_cnt += 1
        else:
            s_cnt += 1 

    if f_cnt > s_cnt:
        f_time += 1
    elif f_cnt < s_cnt:
        s_time += 1

print(convertToString(f_time))
print(convertToString(s_time))
