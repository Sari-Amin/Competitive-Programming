class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distance = []
        for i in range(len(points)):
            distance.append([(points[i][0] * points[i][0] + points[i][1] * points[i][1]), i])
        distance.sort()
        for i in range(k):
            ans.append(points[distance[i][1]])
        return ans
