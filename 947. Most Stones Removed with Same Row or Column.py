# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}
        for x, y in stones:
            if x not in graph:
                graph[x] = []
            if ~y not in graph:
                graph[~y] = []
            graph[x].append(~y)
            graph[~y].append(x)
        visited = set()
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
        components = 0
        for x, y in stones:
            if x not in visited:
                dfs(x)
                components += 1
        return len(stones) - components
    
# Another way:
class Solution(object):
    def dfs(self, n, idx, visited, stones):
        visited[idx] = True
        for i in range(n):
            if not visited[i]:
                if stones[idx][0] == stones[i][0]:
                    self.dfs(n, i, visited, stones)
                if stones[idx][1] == stones[i][1]:
                    self.dfs(n, i, visited, stones)
    def removeStones(self, stones):
        n = len(stones)
        group = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                group += 1
                self.dfs(n, i, visited, stones)
        return n - group 