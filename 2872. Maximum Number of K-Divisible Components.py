# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        visited = set()
        self.components = 0 
        
        def dfs(node):
            visited.add(node)
            subtree_sum = values[node]
            
            for neighbor in tree[node]:
                if neighbor not in visited:
                    child_sum = dfs(neighbor)
                    if child_sum % k == 0:
                        self.components += 1
                    else:
                        subtree_sum += child_sum
            
            return subtree_sum
        
        total_sum = dfs(0)
        if total_sum % k == 0:
            self.components += 1
        
        return self.components