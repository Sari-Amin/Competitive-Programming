class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        ans = 0
        for i in freq:
           ans += (i+1) * (ceil(freq[i] / (i + 1)))
        return ans