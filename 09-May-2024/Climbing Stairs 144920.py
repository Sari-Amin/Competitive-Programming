# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, memo={}):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        return dp(n)


        