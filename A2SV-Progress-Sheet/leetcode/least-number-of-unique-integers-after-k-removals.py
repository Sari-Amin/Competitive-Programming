class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = list(Counter(arr).values())
        freq.sort()
        lsum = 0
        for i in range(len(freq)):
            if lsum + freq[i] <= k:
                lsum += freq[i]
            else:
                return len(freq) - i

        return 0
