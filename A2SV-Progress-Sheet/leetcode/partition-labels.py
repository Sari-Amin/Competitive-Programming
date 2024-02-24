class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in dic:
                dic[s[i]] = i
        ans = []
        l = 0
        mi = 0
        mx = 0
        while l < len(s):
            if mx < dic[s[l]] :
                mx = dic[s[l]]
            if l == mx:
                ans.append(mx - mi + 1)
                mi = l + 1

            l += 1
    
        return ans