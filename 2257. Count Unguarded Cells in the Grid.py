# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    num_seen = 0
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for wall in walls:
            grid[wall[0]][wall[1]] = 2
        for guard in guards:
            grid[guard[0]][guard[1]] = 2
        for guard in guards:
            x, y = guard
            for j in range(y - 1, -1, -1):
                if not self.traverse(grid, x, j, -1):
                    break
            for j in range(y + 1, n):
                if not self.traverse(grid, x, j, -1):
                    break
            for i in range(x - 1, -1, -1):
                if not self.traverse(grid, i, y, 1):
                    break
            for i in range(x + 1, m):
                if not self.traverse(grid, i, y, 1):
                    break
        return m * n - len(guards) - len(walls) - self.num_seen


    def traverse(self, grid, x, y, expected_value):
        if grid[x][y] == 2:
            return False
        if grid[x][y] == 0 or grid[x][y] * expected_value < 0:
            if grid[x][y] == 0:
                grid[x][y] = expected_value
                self.num_seen += 1
            return True

        return False
    
# Another way:
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        a = [[0] * n for _ in range(m)]  # Initialize grid with 0 (unguarded cells)
        tot = m * n  # Total number of cells

        # Mark walls and guards, and adjust `tot`
        for i, j in walls:
            a[i][j] = "w"
            tot -= 1
        for i, j in guards:
            a[i][j] = "g"
            tot -= 1

        # Process guards and mark guarded cells
        for i, j in guards:
            # Upward influence
            k = i - 1
            while k >= 0 and a[k][j] not in ("w", "g"):
                if a[k][j] == 0:  # Only count unguarded cells
                    tot -= 1
                    a[k][j] = 1
                k -= 1

            # Downward influence
            k = i + 1
            while k < m and a[k][j] not in ("w", "g"):
                if a[k][j] == 0:
                    tot -= 1
                    a[k][j] = 1
                k += 1

            # Leftward influence
            k = j - 1
            while k >= 0 and a[i][k] not in ("w", "g"):
                if a[i][k] == 0:
                    tot -= 1
                    a[i][k] = 1
                k -= 1

            # Rightward influence
            k = j + 1
            while k < n and a[i][k] not in ("w", "g"):
                if a[i][k] == 0:
                    tot -= 1
                    a[i][k] = 1
                k += 1

        return tot