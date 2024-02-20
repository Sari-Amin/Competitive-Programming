class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x,n):
            if n == 0:
                return 1
            if n < 0:
                return 1/rec(x, -n)
            if n % 2:
                return x * rec(x*x, n//2)
            else:
                return rec(x*x, n//2)


        return rec(x,n)