class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tobeappear = len(nums) // 2
        newnums = list(set(nums))
        for i in newnums:
            if nums.count(i) > tobeappear:
                return i
