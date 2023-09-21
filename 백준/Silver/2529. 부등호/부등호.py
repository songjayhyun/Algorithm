from itertools import permutations

K = int(input())
l = [0,1,2,3,4,5,6,7,8,9]
A = input().split()

nums = list(permutations(l, K+1))
nums.sort()
new_list = []

for num in nums:
    for i in range(len(A)):
        if A[i] == ">":
            if num[i] < num[i+1]:
                break
        else:
            if num[i] > num[i+1]:
                break
    else:
        new_list.append(num)

print("".join(str(s) for s in new_list[-1]))
print("".join(str(s) for s in new_list[0]))