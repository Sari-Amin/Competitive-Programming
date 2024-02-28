class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1 for i in range(len(nums))]
        stack = []
        temp = nums[:] + nums[:]
        
        for i in range(len(temp)):

            while stack and stack[-1][0] < temp[i]:
                ans[stack[-1][1] % len(ans)] = temp[i]
                stack.pop()
            
            stack.append((temp[i], i))
        
        return ans