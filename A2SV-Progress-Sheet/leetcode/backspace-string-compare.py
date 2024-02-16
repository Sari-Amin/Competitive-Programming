class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            stack = []
            for ch in s:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack
        
        return helper(s) == helper(t)
        