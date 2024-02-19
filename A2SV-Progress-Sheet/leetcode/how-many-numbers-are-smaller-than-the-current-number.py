class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            ans.append(sortednums.index(nums[i]))
        return ans