class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = nums.count(1)
        lsum = 0
        ans = defaultdict(list)
        best = -1
        for i in range(len(nums)):
            ans[ones + lsum].append(i)
            best = max(best, ones + lsum)
            if nums[i] == 0:
                lsum += 1
            else:
                ones -= 1
            
        ans[ones + lsum].append(i + 1)
        best = max(best, ones + lsum)

        return ans[best]