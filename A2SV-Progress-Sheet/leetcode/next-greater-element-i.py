class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = defaultdict(lambda : -1)
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack[-1]] = num
                stack.pop()
            stack.append(num)

        return [dic[num] for num in nums1]

                    
