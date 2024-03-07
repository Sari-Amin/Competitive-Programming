class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def getDivisor(key):
            divisor = 0
            for num in nums:
                divisor += math.ceil(num / key)

            return divisor

        left = 1
        right = max(nums)
        best = float("inf")

        total = sum(nums)

        while left <= right:

            mid = left + (right - left) // 2

            if getDivisor(mid) <= threshold:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best