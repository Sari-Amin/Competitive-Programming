class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_ = max(freq.values())
        ans = 0
        for key in freq:
            if freq[key] == max_:
                ans += freq[key]
        return ans