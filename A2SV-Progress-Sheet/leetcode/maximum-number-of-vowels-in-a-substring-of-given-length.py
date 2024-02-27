class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vow = 0
        for i in range(k):
            if s[i] in "aeiou":
                vow += 1
        ans = max(ans,vow)
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                vow += 1
            if s[i-k] in "aeiou":
                vow -= 1
            ans = max(ans,vow)
        return ans
