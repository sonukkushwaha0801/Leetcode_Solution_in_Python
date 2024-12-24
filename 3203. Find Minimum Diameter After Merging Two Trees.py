# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :

from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        g = []
        neighborCount = []
        leaves0 = []
        leaves1 = []
        def getTreeDiameter(edges):
            nonlocal g, neighborCount, leaves0, leaves1
            n = len(edges) + 1
            g.clear()
            neighborCount.clear()
            for _ in range(n):
                g.append([])
                neighborCount.append(0)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
                neighborCount[u] += 1
                neighborCount[v] += 1

            leaves0.clear()
            leaves1.clear()
            for u, neighCnt in enumerate(neighborCount):
                if neighCnt == 1:
                    leaves0.append(u)
            result = 0
            while len(leaves0) > 1:
                result += 2
                for u in leaves0:
                    for v in g[u]:
                        neighborCount[v] -= 1
                        if neighborCount[v] == 1:
                            leaves1.append(v)
                leaves0, leaves1 = leaves1, leaves0
                leaves1.clear()
            return result - (1 - len(leaves0))
        d1 = getTreeDiameter(edges1)
        d1h = (d1 + 1) >> 1
        d2 = getTreeDiameter(edges2)
        d2h = (d2 + 1) >> 1

        return max(d1, d2, 1 + d1h + d2h)
    

# Another way:
from collections import deque
class Solution:
    def buildAl(self, edges):
        al = {} 
        for edge in edges:
            if edge[0] not in al:
                al[edge[0]] = []
            if edge[1] not in al:
                al[edge[1]] = []
            
            al[edge[0]].append(edge[1])
            al[edge[1]].append(edge[0])
        return al
    
    def prunesUntilRoot(self, graph):
        n = len(graph)

        queue = deque() 
        edge_count = {}
        for node in graph.keys():
            edge_count[node] = len(graph[node])
            if edge_count[node] == 1:
                queue.append(node)

        levels = 0
        while queue: 
            if n == 2: 
                return (levels + 1, (levels * 2) + 1) 
            elif n == 1: 
                return (levels, levels * 2) 
            
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for neighbor in graph[cur]: 
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        queue.append(neighbor)
                n -= 1
            levels += 1
        return 0, 0 

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        al1 = self.buildAl(edges1)
        al2 = self.buildAl(edges2)

        prunes1, diameter1 = self.prunesUntilRoot(al1)
        prunes2, diameter2 = self.prunesUntilRoot(al2)
        return max(prunes1 + prunes2 + 1, diameter1, diameter2) 
        
        
        