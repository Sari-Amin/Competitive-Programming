class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b = blocks[:k].count("B")
        ans = k - b
        for i in range(1, len(blocks)- k + 1):
            if blocks[i - 1] == "B":
                b -= 1
            if blocks[i + k - 1] == "B":
                b += 1
            ans = min(ans, k - b)
        return ans