class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        print(freq)
        ans = 0
        once  = False
        odds = []
        for i in freq:
            if freq[i] % 2 == 0:
                ans += freq[i]
            else:
                once = True
                ans += freq[i] - 1
        if once:
            ans += 1
        return ans 
