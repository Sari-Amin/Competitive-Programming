class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            ans.append(asteroid)
            while len(ans) > 1 and ans[-1] < 0 and ans[-2] > 0:
                if abs(ans[-1]) == abs(ans[-2]):
                    ans.pop()
                    ans.pop()
                elif abs(ans[-2]) > abs(ans[-1]):
                    ans.pop()
                else:
                    temp = ans.pop()
                    ans.pop()
                    ans.append(temp)
            
        return ans
