class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((i, tickets[i]) for i in range(len(tickets)))
        freq = {}
        ans = 0
        while queue:
            num = queue.popleft()
            ans += 1
            if num[1] - 1 != 0:
                queue.append((num[0], num[1] - 1))
            else:
                freq[num[0]] = ans

        return freq[k]


