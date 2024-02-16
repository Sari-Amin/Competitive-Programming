class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_ = float("-inf")
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                temp = sum(grid[i][j:j + 3]) + grid[i + 1][j + 1] + sum(grid[i + 2][j: j + 3])
               
                max_ = max(max_, temp)

                
        return max_