class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = nums.count(0), nums.count(1), nums.count(2) 
        nums[:red] = [0] * red 
        nums[red:red + white] = [1] * white 
        nums[red + white:] = [2] * blue
        
