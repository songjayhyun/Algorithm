n = int(input())
s = input()
s1,s2 = s.split("*") 

for _ in range(n):
    f = input()
    
    if f.startswith(s1) and f.endswith(s2) and len(f) >= len(s1) + len(s2):
        print("DA")
    else:
        print("NE")