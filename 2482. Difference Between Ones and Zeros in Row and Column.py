# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
from itertools import product


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        def summation(nums) : 
            return 2 * sum(nums) - len(nums)
        m, n = len(grid), len(grid[0])
            
        rows = list(map(summation, grid))
        cols = list(map(summation, zip(*grid)))
        
        for i,j in product(range(m), range(n)):
            grid[i][j] = rows[i] + cols[j]
        return grid
    
# Another way:
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        return (R:=list(map(sum, grid))) and (C:=list(map(sum, zip(*grid)))) and \
            [[2*R[i]+2*C[j]-len(R)-len(C) for j in range(len(C))] for i in range(len(R))]