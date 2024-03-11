class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ind = {val:i for i, val in enumerate(order)}
        return "".join(sorted(s, key = lambda x : ind.get(x, ord(x))))