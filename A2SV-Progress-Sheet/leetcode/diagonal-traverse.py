class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        row = 0
        col = 0
        up = True
        while row < len(mat) and col < len(mat[0]):
            if up:
                while row > 0 and col < len(mat[0]) - 1:
                    ans.append(mat[row][col])
                    col += 1
                    row -= 1
                ans.append(mat[row][col])
                if col == len(mat[0]) - 1:
                    row += 1
                else:
                    col += 1

            else:
                while row < len(mat) - 1 and col > 0:
                    ans.append(mat[row][col])
                    col -= 1
                    row += 1
                ans.append(mat[row][col])

                if row == len(mat) - 1:
                    col += 1
                else:
                    row += 1
                    
            up = not up

        return ans