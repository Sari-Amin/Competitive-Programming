class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        end = len(s) - 1
        while left < end:
            if s[left] == s[end]:
                temp = s[left]
                while left < end:
                    if temp == s[left]:
                        left += 1
                    else:
                        break
                while end > left:
                    if temp == s[end]:
                        end -= 1
                    else:
                        break
            else:
                break
        ans = end - left + 1
        if left == end and (end + 1 < len(s) and s[left] == s[end + 1] or left - 1 >= 0 and s[left - 1] == s[end]): 
            ans -= 1 
        
        return ans