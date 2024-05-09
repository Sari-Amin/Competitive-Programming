# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int, memo = {}) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3) 
        return memo[n]
        