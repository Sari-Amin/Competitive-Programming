class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = []
        pre.append(nums[0])
        for i in nums[1:]:
            pre.append(pre[-1] + i)

        ans = [0] * n
        for i in range(n):

            if i == 0:
                ans[i] =(pre[-1] - nums[i]) - nums[i] * (n - i - 1)
            else:
                ans[i] = i * nums[i] - pre[i - 1] + (pre[-1] - pre[i]) - nums[i] * (n - i - 1)

        return ans