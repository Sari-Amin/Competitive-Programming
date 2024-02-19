class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != 0:
                continue
            for j in range(i,len(nums)-1):
                nums[j],nums[j+1] = nums[j+1],nums[j]
        