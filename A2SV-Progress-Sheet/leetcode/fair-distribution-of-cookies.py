class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)
        ans = float("inf")
        distribution = [0] * k
        def backtrack(index):
            nonlocal ans
            if index >= len(cookies):
                ans = min(ans, max(distribution))
                return 
            
            for i in range(k):
                distribution[i] += cookies[index]
                backtrack(index + 1)
                distribution[i] -= cookies[index]
        backtrack(0)
        return ans