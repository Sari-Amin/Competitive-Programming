class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0 for i in range(len(s))]
        for shift in shifts:
            if shift[2] == 1:
                pre[shift[0]] += 1
                if shift[1] + 1 < len(s):
                    pre[shift[1]+1] -= 1
            else:
                pre[shift[0]] -= 1
                if shift[1] + 1 < len(s):
                    pre[shift[1]+1] += 1
        ans = ""
        for i in range(len(pre)):
            if i != 0:
                pre[i] += pre[i-1]
            ans += chr((ord(s[i]) - ord('a') + pre[i]) % 26 + ord('a'))
            
        return ans