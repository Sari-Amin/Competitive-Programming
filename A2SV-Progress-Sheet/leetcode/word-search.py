class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board[0])
        m = len(board)
        w = len(word)
        flag = False
        st = set()

        def rec(i,j,index):
            nonlocal flag, st
            if index >= w:
                flag = True
                return
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if board[i][j] != word[index]:
                return
                
            if (i,j) in st:
                return

            valid = {(i,j + 1), (i+1, j), (i - 1, j), (i, j - 1)}
            st.add((i,j))
            for k in valid:
                rec(k[0],k[1], index + 1)  
            st.remove((i,j))          

        for row in range(m):
            for col in range(n):
                if flag:
                    return True
                else:
                    rec(row,col, 0)
        return flag