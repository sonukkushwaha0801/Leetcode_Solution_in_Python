# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from sys import maxsize


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def find2min(p):
            min1=min2= maxsize
            for num in grid[p]:
                if num < min1:
                    min2 = min1
                    min1 = num
                elif num < min2:
                    min2 = num
            return min1,min2


        for i in range(n-2,-1,-1):
            min1,min2 = find2min(i+1)
            for j in range(n):
                if grid[i+1][j]==min1:
                    grid[i][j]+=min2
                else:
                    grid[i][j]+=min1
         
        return min(grid[0])
    
# Another way: Using Dijkstra
import heapq
from collections import defaultdict



class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        distances = defaultdict(lambda: 100*200)
        distances[(-1,-1)] = 0 # start node

        pq = [(0, (-1,-1))]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue
            x, y = current_vertex
            if x == len(grid) - 1: # final row connects to end node only
                neighbours = [((201, 201), 0)]
            elif x == y == 201: # end node
                neigbours = []
            else:
                neighbours = [((x+1, j), grid[x+1][j]) for j in range(len(grid[0])) if j != y]

            for neighbor, weight in neighbours:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
            
        return distances[(201,201)]