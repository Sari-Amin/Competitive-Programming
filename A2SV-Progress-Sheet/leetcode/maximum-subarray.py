class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lsum = 0
        ans = float("-inf")
        for num in nums:
            if lsum + num > num:
                lsum += num
            else:
                lsum = num
            ans = max(ans, lsum)
            
        return ans
        
