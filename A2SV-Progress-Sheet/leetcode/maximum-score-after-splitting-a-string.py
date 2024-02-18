class Solution:
    def maxScore(self, s: str) -> int:
        number_of_ones = s.count("1") - int(s[0])
        lsum = s[0] == "0"
        ans = 0
        for ch in s[1:-1]:

            ans = max(ans, lsum + number_of_ones)
            
            if ch == "1":
                number_of_ones -= 1
            else:
                lsum += 1

        ans = max(ans, lsum + number_of_ones)
        
        return ans