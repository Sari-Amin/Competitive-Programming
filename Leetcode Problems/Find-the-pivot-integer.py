class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n*(n+1)//2
        lsum = 0
        for i in range(1,n+1):
            total -= i
            if total == lsum:
                return i
            lsum += i
        return -1
