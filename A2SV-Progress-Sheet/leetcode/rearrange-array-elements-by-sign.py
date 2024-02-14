class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = [i for i in nums if i < 0]
        pos = [i for i in nums if i >= 0]
        l = 0
        nl = 0
        rl = 0
        while l < len(nums):
            nums[l] = pos[nl]
            l += 1
            nums[l] = neg[rl]
            l += 1
            nl += 1
            rl += 1
        return nums