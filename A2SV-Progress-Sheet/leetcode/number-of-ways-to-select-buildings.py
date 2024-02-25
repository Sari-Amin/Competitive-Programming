class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = s.count("1")
        zeros = len(s) - ones
        prev_zeros = 0
        prev_ones = 0
        ans = 0
        for i in s:
            
            if i == "0":
                ans += prev_ones * (ones - prev_ones)
                prev_zeros += 1
            else:
                ans += prev_zeros * (zeros - prev_zeros)
                prev_ones += 1
        return ans
