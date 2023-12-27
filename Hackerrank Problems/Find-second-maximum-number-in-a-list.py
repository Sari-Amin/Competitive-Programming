if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    ans = 0
    for i in range(n-1,-1,-1):
        if arr[i] != arr[-1]:
            ans = arr[i]
            break
    print(ans)
