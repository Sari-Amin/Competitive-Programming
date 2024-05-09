# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        root = {i : i for i in range(n)}
        size = [1] * n
        score = defaultdict(int)
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
    
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                    score[rootX] += score[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
                    score[rootY] += score[rootX]
        ans = [0 for i in range(n)]
        reverseQueries = removeQueries[::-1]
        curr = 0

        for i in range(n):
            ans[i] = curr
            min_ = reverseQueries[i] - 1
            max_ = reverseQueries[i] + 1
        
            score[reverseQueries[i]] = nums[reverseQueries[i]]
            if min_ in score:
                union(min_, reverseQueries[i])
            if max_ in score:
                union(max_, reverseQueries[i])
            curr = max(curr, score[find(reverseQueries[i])])

        return ans[::-1]