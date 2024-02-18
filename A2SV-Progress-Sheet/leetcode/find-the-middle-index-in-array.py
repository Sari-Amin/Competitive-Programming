class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lsum = 0
        rightsum = sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            if lsum == rightsum:
                return i
            lsum += nums[i]

        return -1