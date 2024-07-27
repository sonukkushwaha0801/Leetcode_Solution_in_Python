# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        INF = float('inf')
        NUM_LETTERS = 26
        dist = [[INF] * NUM_LETTERS for _ in range(NUM_LETTERS)]
        for i in range(NUM_LETTERS):
            dist[i][i] = 0
        
        for o, c, z in zip(original, changed, cost):
            dist[ord(o) - ord('a')][ord(c) - ord('a')] = min(dist[ord(o) - ord('a')][ord(c) - ord('a')], z)
        
        for k in range(NUM_LETTERS):
            for i in range(NUM_LETTERS):
                for j in range(NUM_LETTERS):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if dist[s_idx][t_idx] == INF:
                return -1
            total_cost += dist[s_idx][t_idx]
        
        return total_cost