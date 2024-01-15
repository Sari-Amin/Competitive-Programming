class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == 0:
            return 0
        ans = 0
        l,r = 0,0
        zero = 0
        while l < len(nums) and r < len(nums):
            if nums[r] == 1 and zero <= 1:
                r += 1
            else:
                if zero == 1:
                    if nums[l] == 0:
                        zero -= 1
                    l += 1
                else:
                    zero += 1
                    r += 1
            ans = max(ans, r - l - 1)
        return ans
