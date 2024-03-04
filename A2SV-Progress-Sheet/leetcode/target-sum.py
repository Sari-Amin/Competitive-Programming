class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ans = 0
        @cache
        def rec(index, sm = 0, memo = {}):
            nonlocal ans
            if index == len(nums):
                if sm == target:
                    return 1
                else:
                    return 0

            positive = rec(index + 1, sm + nums[index])
            negative = rec(index + 1, sm - nums[index])
            return positive + negative
        
        return rec(0)
        
