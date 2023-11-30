n = int(input())
ls = [int(i) for i in input().split()]
e,o = 0,0
for i in range(n):
    if ls[i] % 2:
        o += 1
    else:
        e += 1
if o != 0 and e != 0:
    print(*sorted(ls))
else:
    print(*ls)
