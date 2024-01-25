#https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text2), len(text1)
        dp = [[0] * (m + 1) for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

        return dp[n][m]
