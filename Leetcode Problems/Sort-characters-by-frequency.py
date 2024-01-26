#https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        ans = sorted(freq.items(), key = lambda a: a[1], reverse = True)
        return "".join([char * rep for char, rep in ans])
