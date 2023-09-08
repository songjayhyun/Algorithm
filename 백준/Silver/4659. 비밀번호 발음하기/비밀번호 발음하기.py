
con = ['a','e','i','o','u']

while(True):
    s = input()
    if s == 'end':
        break

    flag = True

    if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') == 0:
        print(f"<{s}> is not acceptable.")
        continue

    pre = []

    for i in s:
        c_cnt = 0
        v_cnt = 0

        if not pre:
            pre.append(i)
            continue

        if i == pre[-1]:
            if i not in ['e', 'o']:
                flag = False
        
        pre.append(i)
        for j in pre[len(pre)-3:]:
            if j in con:
                c_cnt += 1
            else:
                v_cnt += 1
        if c_cnt == 3 or v_cnt == 3:
            
            flag = False
    if flag:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")