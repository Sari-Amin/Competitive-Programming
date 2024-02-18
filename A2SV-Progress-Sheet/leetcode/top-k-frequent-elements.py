class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        nums = [i for i in set(nums)]
        nums.sort(key = lambda x : freq[x], reverse = True)
        return nums[:k]