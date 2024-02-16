class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.k = k
        self.value = value
        self.same = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.same += 1
        if len(self.queue) < self.k:
            self.queue.appendleft(num)
            return self.k == self.same
        if self.k == len(self.queue) and self.value == self.queue[-1]:
            self.same -= 1
        self.queue.pop()
        self.queue.appendleft(num)
        return self.k == self.same


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)