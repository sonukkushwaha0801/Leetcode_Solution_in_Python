#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict
import heapq
class Graph:
    def __init__(self, n, edges):
        self.graph = {}
        for edge in edges:
            from_node, to_node, cost = edge
            if from_node not in self.graph:
                self.graph[from_node] = []
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        heap = [(0, node1)]
        visited = set()

        while heap:
            cost, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == node2:
                return cost

            if current_node in self.graph:
                for neighbor, edge_cost in self.graph[current_node]:
                    heapq.heappush(heap, (cost + edge_cost, neighbor))

        return -1
    

# Another way:
class Graph:
    def __init__(self, n: int, edges: list[list[int]]):

        self.graph = defaultdict(list)
        for edge in edges: self.addEdge(edge)


    def addEdge(self, edge: list[int]) -> None:

        frm, to, edgeCost = edge
        self.graph[frm].append((to, edgeCost))


    def shortestPath(self, s: int, t: int) -> int:
        
        d, queue = defaultdict(lambda:-1, {s:0}), [(0,s)]
 
        while queue:
            a,b = heapq.heappop(queue)
            if d[b] == a:
                for to, edgeCost in self.graph[b]:
                    if d[to] > a + edgeCost or d[to] < 0:
                        d[to] = a + edgeCost
                        heapq.heappush(queue, (d[to], to))
        return d[t]