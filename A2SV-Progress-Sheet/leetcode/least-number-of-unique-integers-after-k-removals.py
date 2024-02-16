class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = list(Counter(arr).values())
        freq.sort()
        ans = 0
        lsum = 0
        for i in range(len(freq)):
            if lsum + freq[i] <= k:
                lsum += freq[i]
            else:
                ans += 1

        return ans
