class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        if x >= 0:
            temp = int(str(x)[::-1])
            return  temp if temp < 2147483648 else 0
        else:
            temp = -1 * int(str(x)[::-1][:-1])
            return temp if temp >= -2147483648 else 0
