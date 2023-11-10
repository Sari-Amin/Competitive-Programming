class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.list = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.list.append("FizzBuzz")
            elif i % 3 == 0:
                self.list.append("Fizz")
            elif i % 5 == 0:
                self.list.append("Buzz")
            else:
                self.list.append(str(i))
        return self.list
