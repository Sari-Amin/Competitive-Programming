class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = float("-inf") 

        for i in range(len(points) - 1):
            ans = max(points[i + 1][0] - points[i][0], ans)

        return ans
