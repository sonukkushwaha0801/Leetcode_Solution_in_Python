# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
       
        colMax = set(map(max,zip(*matrix)))
        
        for row in matrix:
            mn = min(row)
            if mn in colMax: return [mn]
       
# Another way:
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return {min(row) for row in matrix} & {max(col) for col in zip(*matrix)}