class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = []
        for log in logs:
            if len(ans) != 0 and log == "../":
                ans.pop()
            elif log[-2] != ".":
                ans.append(log)
        return len(ans)
