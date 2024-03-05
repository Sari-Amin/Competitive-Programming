class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
    
        nums.sort()
        ans = 0
        l = 0
        curr = nums[l]
        while l < len(nums):
            if curr == nums[l]:
                l += 1
            else:
                curr = nums[l]
                ans += (len(nums) - l)
                l += 1

        return ans