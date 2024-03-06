class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        left = 0
        right = len(letters) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if target < letters[mid]:
                if letters[mid - 1] == target:
                    return letters[mid]
                right = mid - 1
            else:
                left = mid + 1

        return letters[left]