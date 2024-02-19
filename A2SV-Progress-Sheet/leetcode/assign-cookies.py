class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = 0
        r = 0
        ans = 0
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                ans += 1
                r += 1
                l += 1
            else:
                r += 1
        return ans

