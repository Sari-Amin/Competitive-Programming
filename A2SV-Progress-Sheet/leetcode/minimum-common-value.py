class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {}
        for i, val in enumerate(nums1):
            dic[val] = i
        for i in nums2:
            if i in dic:
                return i
        return -1