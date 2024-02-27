class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[-k:])
        ans = total
        curr = 0
        for i in range(k):
            curr += cardPoints[i]
            total -= cardPoints[i - k]
            ans = max(ans, curr + total)

        return ans