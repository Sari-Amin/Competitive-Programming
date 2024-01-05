class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        indx = len(s) - 1
        ans = 0
        while indx > -1:
            if indx-1 > -1 and s[indx-1:indx+1] in dic:
                ans += dic[s[indx-1:indx+1]]
                indx -= 2
            else:
                ans += dic[s[indx]]
                indx -= 1
        return ans


