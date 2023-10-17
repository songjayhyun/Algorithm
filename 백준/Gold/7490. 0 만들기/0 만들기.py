
def join(a,b):
    return a + " " + str(b)

def plus(a,b):
    return str(a) + "+" + str(b)

def minus(a,b):
    return str(a) + "-" + str(b)

def dfs(depth,l,expression):

    if depth == len(l):
        tmp = expression.replace(" ", "")
        if eval(tmp) == 0:
            ans.append(expression)
        return

    dfs(depth+1,l,plus(expression,l[depth]))
    dfs(depth+1,l,minus(expression,l[depth]))
    dfs(depth+1,l,join(expression,l[depth]))

    return expression

t = int(input())

for _ in range(t):
    l = [i for i in range(1,int(input())+1)]
    ans = []
    dfs(1,l,str(l[0]))
    ans.sort()
    for a in ans:
        print(a)
    print()