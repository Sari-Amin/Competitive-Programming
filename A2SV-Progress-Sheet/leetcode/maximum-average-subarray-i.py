class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = sum(nums[:k])
        avg = tot / k
        for i in range(1,len(nums) - k + 1):
            tot = tot - nums[i-1] + nums[i + k - 1]
            avg = max(avg, tot/k)
        return avg