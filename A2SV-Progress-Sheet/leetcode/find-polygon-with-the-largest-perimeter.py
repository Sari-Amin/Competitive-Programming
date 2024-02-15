class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        lsum = nums[0] + nums[1]
        lastpossible = -1
        for i in range(2,len(nums)):
            if lsum > nums[i]:
                lastpossible = lsum + nums[i]

            lsum += nums[i]

        return lastpossible