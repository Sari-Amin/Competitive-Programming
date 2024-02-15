class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            temp = ""
            for j in range(len(strs)):
                temp += strs[j][i]
            ans += temp != "".join(sorted(temp))
            
        return ans
