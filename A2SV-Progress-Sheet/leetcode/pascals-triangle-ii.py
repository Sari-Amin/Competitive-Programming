class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def rec(n):
            if n == 0:
                return [1]
            if n == 1:
                return [1,1]

            pre = rec(n - 1)
            ans = [1]
            for i in range(1,len(pre)):
                ans.append(pre[i - 1] + pre[i])
            ans += [1]
            return ans
            
        return rec(rowIndex)