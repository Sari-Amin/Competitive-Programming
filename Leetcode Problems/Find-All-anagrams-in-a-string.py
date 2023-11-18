class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        p = sorted(p)
        ans = []
        s_len = len(s)
        p_len = len(p)
        for i in range(s_len):
            if i + p_len <= s_len and sorted(s[i:i + p_len]) == p:
                ans.append(i)
        return ans
