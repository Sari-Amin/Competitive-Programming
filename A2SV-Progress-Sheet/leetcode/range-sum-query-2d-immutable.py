class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n,self.m = len(matrix), len(matrix[0])
        self.prefix_sum = [[0 for i in range(self.m + 1)] for j in range(self.n+1)]
        for row in range(self.n):
            for col in range(self.m):
                self.prefix_sum[row+1][col+1] = self.prefix_sum[row][col+1] + self.prefix_sum[row+1][col] - self.prefix_sum[row][col] + matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)