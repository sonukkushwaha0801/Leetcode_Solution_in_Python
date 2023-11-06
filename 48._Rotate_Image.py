# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        
        matrix[:]=list(zip(*matrix[::-1]))

# Another way:
class Solution:
    def rotate(self, x: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(x)):
            for j in range(i,len(x)):
                x[i][j],x[j][i]=x[j][i],x[i][j]
        for i in range(len(x)):
            x[i]=x[i][::-1]