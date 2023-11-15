class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        n = len(citations)
        for i in range(n):
            if citations[i] >= i + 1 :
                ans = max(ans, i + 1)
        return ans
