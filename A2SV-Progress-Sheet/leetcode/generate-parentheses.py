class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def backtrack(path = [], op = 0, close = 0):

            if op  > n or close > op:
                return
                
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            for i in ["(", ")"]:
                path.append(i)
                if i == "(":
                    op += 1
                else:
                    close += 1
                backtrack(path, op , close) 
                path.pop()
                if i == "(":
                    op -= 1
                else:
                    close -= 1
        backtrack()
        return ans