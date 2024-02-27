class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        tot = 0
        ans = len(nums) + 1 
        for i in range(len(nums)):
            tot += nums[i]
            while tot >= target:
                ans = min(i-l+1, ans)
                tot -= nums[l]
                l += 1
        return ans if ans != len(nums) + 1  else 0