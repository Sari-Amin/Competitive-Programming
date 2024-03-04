class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def rec(index, sm = 0, memo = {}):

            if index == len(nums):
                if sm == target:
                    return 1
                else:
                    return 0

            positive = rec(index + 1, sm + nums[index])
            negative = rec(index + 1, sm - nums[index])
            return positive + negative
        
        return rec(0)
        
