# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
from cmath import inf
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        adjs = [{} for _ in range(n)]

        for edge in edges:
            adjs[edge[0]][edge[1]] = edge[2]
            adjs[edge[1]][edge[0]] = edge[2]

        distTo = [float('inf')] * n
        distTo[source] = 0

        pq = [(0, source)]
        heapq.heapify(pq)

        self.dijkstra(adjs, distTo, pq)

        if distTo[destination] == target:
            return self.fill(edges)
        elif distTo[destination] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1
                adjs[edge[0]][edge[1]] = 1
                adjs[edge[1]][edge[0]] = 1

                pq = [(distTo[edge[0]], edge[0]), (distTo[edge[1]], edge[1])]

                self.dijkstra(adjs, distTo, pq)

                if distTo[destination] == target:
                    return self.fill(edges)
                elif distTo[destination] < target:
                    edge[2] += target - distTo[destination]
                    adjs[edge[0]][edge[1]] = edge[2]
                    adjs[edge[1]][edge[0]] = edge[2]
                    return self.fill(edges)

        return []

    def fill(self, edges):
        for edge in edges:
            if edge[2] == -1:
                edge[2] = int(2e9)
        return edges

    def dijkstra(self, adjs, distTo, pq):
        while pq:
            curr_dist, curr = heapq.heappop(pq)

            for next_node, weight in adjs[curr].items():
                if weight > 0:
                    if distTo[next_node] - weight > distTo[curr]:
                        distTo[next_node] = distTo[curr] + weight
                        heapq.heappush(pq, (distTo[next_node], next_node))

# Another way:
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        def dijkstra(source, adj, skip_negative):
            pq = [[0, source]]
            dist = defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heapq.heappush(pq, [d2, nei])

            return dist, parent
        
        distR, parentR = dijkstra(destination, adj, skip_negative=True)
        if distR.get(source, inf) < target:
            return []
        dist, parent = dijkstra(source, adj, skip_negative=False)
        if dist[destination] > target:
            return []
        
        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path = path[::-1]
        
        edges = {(min(u,v), max(u,v)) : w for u, v, w in edges}
        
        walked = 0
        for u, v in zip(path, path[1:]):
            e = (min(u, v), max(u, v))
            if edges[e] == -1:
                edges[e] = max(target - distR.get(v, inf) - walked, 1)
                if edges[e] > 1:
                    break
            walked += edges[e]
        
        for e, w in edges.items():
            if w == -1:
                edges[e] = 2 * (10 ** 9)
        
        return [[u,v,w] for (u,v), w in edges.items()]