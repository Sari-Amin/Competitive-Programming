class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix) , len(matrix[0])
        res = [[float("inf")] * (col + 1) for i in range(row)]
        res[-1] = matrix[-1] + [float("inf")]
        for r in range(row-2, -1, -1):
            for c in range(col-1,-1,-1):
                res[r][c] = matrix[r][c] + min(res[r + 1][c-1],res[r+1][c+1], res[r+1][c])
        
        return min(res[0])
