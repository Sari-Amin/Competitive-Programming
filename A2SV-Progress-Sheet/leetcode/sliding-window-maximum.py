class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = 0
        queue = deque()
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])

            if i + 1 >= k:
                ans.append(queue[0])
                if queue[0] == nums[left]:
                    queue.popleft()
                left += 1

        return ans
