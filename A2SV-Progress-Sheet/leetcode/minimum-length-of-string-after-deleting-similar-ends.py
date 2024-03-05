class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        end = len(s) - 1
        while left < end and s[left] == s[end]:
            temp = s[left]
            while left <= end and temp == s[left]:
                left += 1
            while end >= left and temp == s[end]:
                end -= 1
            
        return end - left + 1