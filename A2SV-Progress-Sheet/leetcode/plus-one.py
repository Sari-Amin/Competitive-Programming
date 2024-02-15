class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        remainder = digits[-1] // 10
        digits[-1] %= 10

        for i in range(len(digits) - 2, -1, -1):
            digits[i] += remainder
            remainder = digits[i] // 10
            digits[i] %= 10

        if remainder > 0:
            return [remainder] + digits
        return digits