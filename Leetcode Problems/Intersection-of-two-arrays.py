class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        for i in range(len(nums1)):
            if nums1[i] not in ans and nums1[i] in nums2:
                ans.append(nums1[i])
        return ans
