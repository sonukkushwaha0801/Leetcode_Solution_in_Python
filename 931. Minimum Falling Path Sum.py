# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import reduce


class Solution:
    def minFallingPathSum(self, m: list[list[int]]) -> int:
        return min(reduce(lambda a,r:[min(a[max(0,c-1):c+2])+r[c] for c in range(len(m))],m))
    
# Another way:
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows):
            for c in range(cols):
                top_left = matrix[r - 1][c - 1] if c - 1 >= 0 else float ('inf')
                top_above = matrix[r - 1][c]
                top_right = matrix[r - 1][c + 1] if c + 1 < cols else float('inf')

                matrix[r][c] = matrix[r][c] + min(top_left, top_above, top_right)
        return min(matrix[-1])