class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        ans = ""
        odd = len(palindrome) % 2 == 1

        for ch in range(len(palindrome)):
            if palindrome[ch] != "a" and not odd:
                return palindrome[:ch] + "a" + palindrome[ch+1:]
            if odd and palindrome[ch] != "a" and ch != len(palindrome) // 2:
                return palindrome[:ch] + "a" + palindrome[ch+1:]
            if ch == len(palindrome) - 1  and palindrome[ch] == "a":
                return palindrome[:-1] + "b" 

        return ""
