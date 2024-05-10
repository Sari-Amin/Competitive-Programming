# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        minus = 0
        happiness.sort(reverse = True)
        left = 0
        ans = 0
        while k:
            if  happiness[left] - minus > 0:
                ans += happiness[left] - minus
            left += 1
            minus += 1
            k -= 1
        return ans
