class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = ans = 0
        min_queue = deque()
        max_queue = deque()
        for i in range(len(nums)):

            while min_queue and min_queue[-1] > nums[i]:
                min_queue.pop()
            min_queue.append(nums[i])

            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
            max_queue.append(nums[i])

            if max_queue[0] - min_queue[0] > limit:
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                left += 1

            ans = max(ans, i - left + 1)

        return ans