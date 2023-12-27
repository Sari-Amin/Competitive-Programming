# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
ans = []
space = m//2 - 1
for i in range(n//2):
    curr = "-" * (space) + "."
    indx = space
    while indx < m//2 - 1:
        curr += "|"
        curr += ".."
        indx += 3
    curr += "|"
    curr = curr + curr[:-1][::-1]
    ans.append(curr)
    space -= 3
for i in ans:
    print(i)
print("-" * ((m-7)//2) + "WELCOME" + "-" * ((m-7)//2))
for i in ans[::-1]:
    print(i)
