class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = "".join(sorted(chars))
        ans = 0
        charmp = {}
        for i in chars:
            charmp[i] = 1 + charmp.get(i,0)
        for word in words:
            charword = {}
            valid = True
            for i in word:
                charword[i] = 1 + charword.get(i,0)
            for i in word:
                if charmp.get(i,0) < charword.get(i,0):
                    valid = False
            if valid:
                ans += len(word)
        return ans
