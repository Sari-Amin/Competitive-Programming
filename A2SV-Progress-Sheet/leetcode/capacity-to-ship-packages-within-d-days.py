class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysNeeded(limit):

            curr = 0
            days = 1
            for weight in weights:
                if curr + weight > limit:
                    days += 1
                    curr = weight
                else:
                    curr += weight

            return days

        left = max(weights)
        right = sum(weights)
        best = right
        while left <= right:

            mid = left + (right - left) // 2
            if daysNeeded(mid) <= days:
                best = min(best, mid)
                right = mid - 1
            else:
                left = mid + 1
        return best
