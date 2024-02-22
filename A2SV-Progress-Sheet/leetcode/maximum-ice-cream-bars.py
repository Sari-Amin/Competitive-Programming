class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        lsum = 0
        ans = 0
        for i in range(len(costs)):
            lsum += costs[i]
            if lsum <= coins:
                ans += 1
            else:
                break
        return ans