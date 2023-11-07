# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = []
        def helper(row,col):
            for i in range(0,len(matrix[0])):
                matrix[row][i] = 0
            for j in range(0,len(matrix)):
                matrix[j][col] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    visited.append((i,j))

        for i,j in visited:
            helper(i,j)
        
        
# Another way:
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for row in range(n):
                        if matrix[i][row]!=0:
                            matrix[i][row]=-2**32
                    for col in range(m):
                        if matrix[col][j]!=0:
                            matrix[col][j]=-2**32

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==(-2**32):
                    matrix[i][j]=0
        