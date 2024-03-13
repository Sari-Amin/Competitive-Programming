class Solution:
    def pivotInteger(self, n: int) -> int:
        lsum = 0
        total = n * (n + 1) // 2
        for num in range(1, n + 1):
            lsum += num
            if lsum == total:
                return num
            total -= num

        return -1