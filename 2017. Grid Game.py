# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        total_sum = sum(grid[0])
        jit_sum = 0
        ans = float('inf')
        for i in range(n):
            total_sum -= grid[0][i]
            var = max(jit_sum, total_sum)
            ans = min(ans, var)
            jit_sum += grid[1][i]
        
        return ans
    
# Another way:
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        pref1 = [0] * m
        pref2 = [0] * m

        pref1[0] = grid[0][0]
        pref2[0] = grid[1][0]

        for i in range(1, m):
            pref1[i] = pref1[i - 1] + grid[0][i]
            pref2[i] = pref2[i - 1] + grid[1][i]

        result = float('inf')
        for i in range(m):
            top = 0 if i == m - 1 else pref1[m - 1] - pref1[i]
            bottom = 0 if i == 0 else pref2[i - 1]
            result = min(result, max(top, bottom))

        return result