# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        R, C = len(grid), len(grid[0])

        def isOutside(i, j):
            return i < 0 or i >= R or j < 0 or j >= C

        def idx(i, j):
            return i * C + j

        N = R * C
        time = [2**31] * N
        pq = [0]

        time[0] = 0
        while len(pq):
            tij = heappop(pq)
            t, ij = tij >> 32, tij & ((1 << 30) - 1)
            i, j = divmod(ij, C)
            if i == R - 1 and j == C - 1:
                return t

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, s = i + di, j + dj
                if isOutside(r, s):
                    continue

                w = 0 if (grid[r][s] - t) & 1 else 1
                nextTime = max(t + 1, grid[r][s] + w)

                rs = idx(r, s)
                if nextTime < time[rs]:
                    time[rs] = nextTime
                    heappush(pq, (nextTime << 32) + rs)
        return -1

# Another way:
from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        pq = []
        heappush(pq, (0, 0, 0))

        visited = [[False] * col for _ in range(row)]
        visited[0][0] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            time, x, y = heappop(pq)

            if x == row - 1 and y == col - 1:
                return time

            for dx, dy in directions:
                newX, newY = x + dx, y + dy

                if 0 <= newX < row and 0 <= newY < col and not visited[newX][newY]:
                    diff = abs(grid[newX][newY] - time)
                    waitingTime = 1 if diff % 2 == 0 else 0
                    newTime = max(grid[newX][newY] + waitingTime, time + 1)
                    heappush(pq, (newTime, newX, newY))
                    visited[newX][newY] = True

        return -1