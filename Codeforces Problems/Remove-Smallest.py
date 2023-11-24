t= int(input())
for i in range(t):
    n = int(input())
    ls = [int(j) for j in input().split()]
    ls.sort()
    ans = True
    ptr = 0
    while ptr != n - 1:
        if abs(ls[ptr]-ls[ptr + 1]) <= 1:
            ptr += 1
        else:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")