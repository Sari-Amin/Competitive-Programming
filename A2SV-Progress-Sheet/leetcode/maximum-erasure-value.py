class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = 0
        curr = 0
        visited = set()
        while r < len(nums):
            if nums[r] not in visited:
                visited.add(nums[r])
                curr += nums[r]
                r += 1
            else:
                curr -= nums[l]
                visited.remove(nums[l])
                l += 1
            ans = max(ans, curr)
        return ans