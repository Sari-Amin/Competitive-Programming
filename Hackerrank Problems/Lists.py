if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        a = input().split()
        if a[0] == "print":
            print(ls)
        elif a[0] == "pop":
            ls.pop()
        elif a[0] == "sort":
            ls.sort()
        elif a[0] == "append":
            ls.append(int(a[1]))
        elif a[0] == "remove":
            ls.remove(int(a[1]))
        elif a[0] == "insert":
            ls.insert(int(a[1]),int(a[2]))
        else:
            ls = ls[::-1]
        
