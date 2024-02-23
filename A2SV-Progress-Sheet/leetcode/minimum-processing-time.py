class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        ans = float("-inf")
        l = 0
        for i in range(len(tasks)):
            ans = max(ans, processorTime[l] + tasks[i])
            if (i + 1) % 4 == 0:
                l += 1
        return ans