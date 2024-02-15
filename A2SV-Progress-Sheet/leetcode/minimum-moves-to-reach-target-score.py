from math import log2

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        ans = 0
        while target != 0:
            if target % 2 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                target //= 2
                ans += 1
            elif maxDoubles == 0 and target >= 1:
                ans += target
                break
            else:
                ans += 1
                target -= 1

        return ans - 1       