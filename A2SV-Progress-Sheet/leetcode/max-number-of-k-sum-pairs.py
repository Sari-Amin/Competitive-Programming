class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l , r = 0 , len(nums) - 1
        ans = 0
        nums.sort()
        while l < r:
            temp = nums[l] + nums[r]
            if temp == k:
                ans += 1
                l += 1
                r -= 1
            elif temp < k:
                l += 1
            else:
                r -= 1
        return ans