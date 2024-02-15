class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        r = len(nums) - 2
        ans = 0
        while r > -1:
            if nums[r + 1] < nums[r]:
                no_of_element = ceil(nums[r] / nums[r+1])
                ans += no_of_element - 1
                nums[r] //= no_of_element

            r -= 1
        return ans