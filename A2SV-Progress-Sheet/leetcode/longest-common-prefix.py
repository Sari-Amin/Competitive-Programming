class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        length  = len(strs[0])
        ans = ""
        for i in range(length):
            temp = strs[0][i]
            cnt = 1
            for st in range(1, len(strs)):
                if strs[st][i] == temp:
                    cnt += 1
            if cnt == len(strs):
                ans += temp
            else:
                break

        return ans