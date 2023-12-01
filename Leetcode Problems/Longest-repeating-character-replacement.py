class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        count = {}
        currmax = 0
        for  i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0)
            currmax = max(currmax,count[s[i]])
            while i - l + 1 - currmax > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, i-l+1)
        return ans
