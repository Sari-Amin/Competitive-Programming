class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 1
        l,r = 0, 1
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
            else:
                r += 1
            ans = max(ans, r-l)
        return ans