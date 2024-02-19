class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        left, right = 0, n - 1
        counter = 0
        while left < right:
            if nums[left] + nums[right] < target:   
                counter += right - left
                left += 1
            else:
                right -= 1
        
        return counter