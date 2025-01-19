# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        minHeap = []

        # Add boundary cells
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(minHeap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                if not visited[i][j]:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        waterTrapped = 0

        while minHeap:
            height, x, y = heapq.heappop(minHeap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    waterTrapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return waterTrapped
    
# Another way:
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        boundary = [(heightMap[i][j], i, j) for i in range(m) for j in (0, n - 1)] + \
                   [(heightMap[i][j], i, j) for j in range(1, n - 1) for i in (0, m - 1)]
        for _, i, j in boundary:
            heightMap[i][j] = -1

        heapify(boundary)
        ans, water_level = 0, 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while boundary:
            h, i, j = heappop(boundary)
            water_level = max(water_level, h)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and heightMap[ni][nj] != -1:
                    ans += max(0, water_level - heightMap[ni][nj])
                    heappush(boundary, (heightMap[ni][nj], ni, nj))
                    heightMap[ni][nj] = -1

        return ans
            