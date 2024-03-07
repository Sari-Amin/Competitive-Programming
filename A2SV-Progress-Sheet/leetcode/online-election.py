class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        dt = defaultdict(int)
        self.ans = []
        curr = None
        self.times = times
        for i,v in enumerate(persons):
            dt[v] += 1
            if curr == None:
                curr = v
            else:
                if curr != v and dt[v] >= dt[curr]:
                    curr = v
            self.ans.append(curr)
       
    def q(self, t: int) -> int:
        x = bisect_right(self.times, t) - 1
        return self.ans[x]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)