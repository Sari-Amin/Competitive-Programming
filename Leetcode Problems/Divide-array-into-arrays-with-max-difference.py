#https://leetcode.com/problems/divide-array-into-arrays-with-max-difference

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        if len(nums) % 3:
            return []
        ans = []
        for i in range(0, len(nums) - 2, 3):
            if nums[i + 2] - nums[i] <= k:
                ans.append(nums[i:i + 3])
            else:
                ans = []
                break
        return ans
