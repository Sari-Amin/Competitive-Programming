class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        pre = [nums[0] for i in range(len(nums))]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] + nums[i]
        ans = float(-inf)
        l, r = 0,k-1
        while r < len(nums):
            if l == 0:
                ans = max(ans,(pre[r]) / k)
            else:
                ans = max(ans,(pre[r] - pre[l-1]) / k)
            l += 1
            r += 1
       
        return ans
