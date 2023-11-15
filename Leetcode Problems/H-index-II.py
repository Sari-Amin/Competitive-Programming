class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = citations[::-1]
        ans = 0
        l,r = 0, len(citations) - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= mid + 1:
                ans = max(ans, mid + 1)
                l = mid + 1
            else:
                r = mid - 1
            
        return ans
