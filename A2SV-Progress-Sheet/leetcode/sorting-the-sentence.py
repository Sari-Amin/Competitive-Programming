class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        l = 0
        while l < len(s):
            correct = int(s[l][-1]) - 1
            if s[l] != s[correct]:
                s[l], s[correct] = s[correct], s[l]
            else:
                l += 1
        
        return " ".join([i[:-1] for i in s])

