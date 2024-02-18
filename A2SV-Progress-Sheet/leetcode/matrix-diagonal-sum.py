class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row, col = 0,0
        ans = 0
        
        while row < len(mat) and col < len(mat[0]):
            ans += mat[row][col]
            row += 1
            col += 1
        
        row = len(mat) - 1
        col = 0

        while row > -1 and col < len(mat[0]):
            if col != row:
                ans += mat[row][col]
            col += 1
            row -= 1
            
        return ans
