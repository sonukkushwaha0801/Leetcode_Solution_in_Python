# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        farmlands = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    bottom_row = i
                    right_col = j
                    while bottom_row + 1 < rows and land[bottom_row + 1][j] == 1:
                        bottom_row += 1
                    while right_col + 1 < cols and land[i][right_col + 1] == 1:
                        right_col += 1

                    farmlands.append([i, j, bottom_row, right_col])
                    
        return farmlands
    
# ANother way:
from collections import deque
from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0]) 
        farmland_groups = []
        queue = deque()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1:
                    queue.append((row, col))
                    land[row][col] = 0
                    farmland_coords = [row, col, -1, -1]
                    max_row, max_col = row, col
                    while queue:
                        r, c = queue.popleft()
                        max_row, max_col = max(max_row, r), max(max_col, c)
                        for dr, dc in directions:
                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols and land[new_r][new_c] == 1:
                                land[new_r][new_c] = 0
                                queue.append((new_r, new_c))
                    farmland_coords[2], farmland_coords[3] = max_row, max_col
                    farmland_groups.append(farmland_coords)
        return farmland_groups