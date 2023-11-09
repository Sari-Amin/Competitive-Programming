class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.new_s = ""
        for i in s:
            if i.isalnum():
                self.new_s += i.lower()
        return self.new_s == self.new_s[::-1]
