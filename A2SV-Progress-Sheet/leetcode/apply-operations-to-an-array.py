class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        r = 0
        zero = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            else:
                zero += 1
            r += 1
        nums[l:] = [0] * zero
        return nums