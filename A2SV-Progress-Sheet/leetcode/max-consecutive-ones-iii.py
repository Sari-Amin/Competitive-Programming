class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        ans = 0
        zero = 0
        while l < len(nums) and r < len(nums):
            if nums[r] == 1 and zero <= k:
                r += 1
            else:
                if zero < k:
                    zero += 1
                    r += 1
                else:
                    if nums[l] == 0:
                        zero -= 1
                    l += 1
            ans = max(ans, r - l)
        return ans

