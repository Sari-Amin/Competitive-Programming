class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float("inf")

        dic = {}

        for  i in range(len(cards) - 1, -1, -1):
            if cards[i] not in  dic:
                dic[cards[i]] = i
            else:
                ans = min(ans, dic[cards[i]] - i + 1)
                dic[cards[i]] = i

        if ans == float("inf"):
            ans = -1
            
        return ans