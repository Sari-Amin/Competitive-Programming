class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def rec(nums,cur):
            if len(nums) == k:
                ans.append(nums.copy())
                return
    
            for i in range(cur,n + 1):
                nums.append(i)
                rec(nums,i+1)
                nums.pop()
        rec([], 1)
        return ans