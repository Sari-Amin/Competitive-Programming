class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        freq = Counter(senate)
        if len(freq) == 1:
            return "Radiant" if senate[0] == "R" else "Dire"
        ban_from_d = 0
        ban_from_r = 0
        while len(queue) != 1:
            turn = queue.popleft()
            if ban_from_r > 0 and turn == "R":
                ban_from_r -= 1
                freq["R"] -= 1
                if freq["R"] == 0:
                    return "Dire"
                continue
            if ban_from_d > 0 and turn == "D":
                ban_from_d -= 1
                freq["D"] -= 1
                if freq["D"] == 0:
                    return "Radiant"
                continue
            if turn == "D":
                ban_from_r += 1
            else:
                ban_from_d += 1
            queue.append(turn)
                
        return "Radiant" if queue[0] == "R" else "Dire"
            