class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(lambda : 0)
        d[0] = 1
        lsum = 0
        for num in nums:
            lsum += num
            if lsum % k in d:
                ans += d[lsum % k]
            d[lsum % k] += 1

        return ans
   