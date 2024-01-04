class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for val in counter:
            if counter[val] == 1:
                return -1
            ans += math.ceil(counter[val]/3)
        return ans
