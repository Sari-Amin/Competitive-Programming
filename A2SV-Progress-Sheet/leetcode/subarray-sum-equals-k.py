class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(lambda : 0)
        d[0] = 1
        lsum = 0
        for i in range(len(nums)):
            lsum += nums[i]
            if lsum - k in d:
                ans += d[lsum - k]
            d[lsum] += 1

        return ans
   