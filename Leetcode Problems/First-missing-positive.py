#https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = 0
        while l < len(nums):
            correct = nums[l] - 1
            if nums[l] < len(nums) and nums[l] > 0 and nums[l] != nums[correct]:
                nums[l], nums[correct] = nums[correct], nums[l]
            else:
                l += 1

        for index, val in enumerate(nums):
            if index + 1 != val:
                return index + 1
        return len(nums) + 1
