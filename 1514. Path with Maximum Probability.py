# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [0] * n
        dist[start] = 1
        
        for _ in range(n - 1):
            updated = False
            for i, (u, v) in enumerate(edges):
                if dist[u] * succProb[i] > dist[v]:
                    dist[v] = dist[u] * succProb[i]
                    updated = True
                if dist[v] * succProb[i] > dist[u]:
                    dist[u] = dist[v] * succProb[i]
                    updated = True
            if not updated:
                break
        
        return dist[end]
    
# Another way:
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Adjacency list
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append((v, p))
            adj[v].append((u, p))

        dist = [0.0] * n
        dist[start] = 1.0

        queue = deque([start])

        while queue:
            curr = queue.popleft()

            for node, prob in adj[curr]:
                new_prob = dist[curr] * prob

                if new_prob > dist[node]:
                    dist[node] = new_prob
                    queue.append(node)

        return dist[end]