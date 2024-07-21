# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import defaultdict, deque
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order1 = self.generate_topological_sort(rowConditions, k)
        order2 = self.generate_topological_sort(colConditions, k)
        
        if len(order1) < k or len(order2) < k:
            return []
        
        m = {order2[i]: i for i in range(k)}
        ans = [[0] * k for _ in range(k)]
        
        for i in range(k):
            ans[i][m[order1[i]]] = order1[i]
        
        return ans

    def generate_topological_sort(self, A: List[List[int]], k: int) -> List[int]:
        deg = [0] * k
        order = []
        graph = defaultdict(list)
        q = deque()
        
        for c in A:
            graph[c[0] - 1].append(c[1] - 1)
            deg[c[1] - 1] += 1
        
        for i in range(k):
            if deg[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            order.append(x + 1)
            for y in graph[x]:
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)
        
        return order
    
# Another way:
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            graph = defaultdict(list)
            indegree = {i: 0 for i in range(1, k + 1)}
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            zero_indegree = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            order = []
            
            while zero_indegree:
                node = zero_indegree.popleft()
                order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree.append(neighbor)
            
            if len(order) != k:
                return []
            
            return order
        
        row_order = topological_sort(rowConditions)
        if not row_order:
            return []
        
        col_order = topological_sort(colConditions)
        if not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix