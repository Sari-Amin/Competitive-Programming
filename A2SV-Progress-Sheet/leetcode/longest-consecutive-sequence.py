class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()
        curr = nums[0]
        ans = 0
        current_count = 1

        for num in nums:
            if num == curr:
                continue
            if num == curr + 1:
                current_count += 1
                curr += 1
            else:
                ans = max(ans, current_count)
                current_count = 1
                curr = num
        
        return max(ans,current_count)

