class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hourNeeded(k):
            hours = 0
            for num in piles:
                hours += math.ceil(num / k)
            return hours

        left = 1
        right = max(piles)
        best = float("inf")

        while left <= right:

            mid = left + (right - left) // 2

            val = hourNeeded(mid)

            if val <= h:
                best = min(best, mid)
                right = mid - 1
            else:
                left = mid + 1
        return best
