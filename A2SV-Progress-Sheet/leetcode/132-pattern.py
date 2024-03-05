class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        right = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if stack and right != float("-inf") and nums[i] < right:
                return True

            while stack and nums[i] > stack[-1]:
                right = max(right,stack.pop())
            stack.append(nums[i])

        return False