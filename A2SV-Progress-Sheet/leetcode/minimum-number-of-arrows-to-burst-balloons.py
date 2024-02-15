class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda a : a[1])
        ans = 1
        minend = points[0][1]
        for i in range(1,len(points)):
        
            if minend < points[i][0]:
                minend = points[i][1]
                ans += 1

        return ans 
       