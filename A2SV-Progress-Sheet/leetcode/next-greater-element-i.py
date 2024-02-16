class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            stack = []
            for j in nums2:
                if nums1[i] == j:
                    stack.append(j)
                else:
                    if stack and stack[-1] < j:
                        ans.append(j)
                        stack.pop()
                        break
            if stack and stack[-1] == nums1[i]:
                ans.append(-1)
        return ans

                    
