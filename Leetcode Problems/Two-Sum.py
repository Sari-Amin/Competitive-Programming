class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0,0]
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                ans = [dic[target-nums[i]],i]
                break
            dic[nums[i]] = i
        return ans
