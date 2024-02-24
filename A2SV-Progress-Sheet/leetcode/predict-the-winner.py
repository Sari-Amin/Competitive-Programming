class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(l,r):
            if l == r:
                return nums[l]
            left = nums[l] - rec(l + 1, r)
            right = nums[r] - rec(l, r - 1)
            return max(left, right)
        return rec(0, len(nums) - 1) >= 0