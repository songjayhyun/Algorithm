s = input()
answer = ""
word = ""
tag = ""
tag_flag = False

for i in s:
    if i == ">":
        answer = answer + tag + i
        tag = ""
        tag_flag = False
    elif i == "<" or tag_flag:
        if len(word) >= 0:
            answer += word[::-1]
            word = ""
        tag += i
        tag_flag = True
    elif i == " ":
        answer = answer + word[::-1] + " "
        word = ""
    else:
        word += i

if len(word) >= 0:
    answer += word[::-1]

print(answer)
