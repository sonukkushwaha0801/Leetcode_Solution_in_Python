# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return zip(*matrix)

# Another way:
class Solution(object):
    def transpose(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        result = [[0] * row for _ in range(col)]
        
        for i in range(col):
            for j in range(row):
                result[i][j] = matrix[j][i]
                
        return result
        
