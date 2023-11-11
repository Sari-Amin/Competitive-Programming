class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            if nums[i] > target:
                break
            ans.append(i)
        return ans
