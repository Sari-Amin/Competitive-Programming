class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        def rec(n,m):
            if m == 0 or n == 1:
                return 1
            if m % 2 == 0:
                return rec(n * n % MOD, m // 2)
            return n % MOD * rec(n * n % MOD, m // 2)


        ans = 5 if n % 2 else 1
        ans = (ans * rec(20, n//2)) % MOD
         
        return ans