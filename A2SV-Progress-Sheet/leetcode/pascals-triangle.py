class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        def rec(n):
            if n == 1:
                return [1,1]

            pre = rec(n - 1)
            res.append(pre)
            ans = [1]
            for i in range(1,len(pre)):
                ans.append(pre[i - 1] + pre[i])
            ans += [1]
            return ans

        rec(numRows)
        
        return res
        