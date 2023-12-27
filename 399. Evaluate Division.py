# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import collections


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        adjacencylist = collections.defaultdict(list)  
        for i,eq in enumerate(equations):
            a,b = eq   
            adjacencylist[a].append([b,values[i]]) 
            adjacencylist[b].append([a,1/values[i]])

        print(adjacencylist)
        def bfs(src,trg):
            if src not in adjacencylist or trg not in adjacencylist:
                return -1
            
            q = deque()
            visited = set()

            q.append([src,1]) 
            visited.add(src)
            
            while q:
                n , w = q.popleft() 

                if n == trg:
                    return w

                for neighbor,weight in adjacencylist[n]:
                    if neighbor not in visited:
                        q.append([neighbor, w * weight])
                        visited.add(n)

            return -1

        return [bfs(query[0],query[1]) for query in queries]
    
# Another way:
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        seen = set()

        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]


        def divide(a, b):
            if a == b:
                return 1.00000

            seen.add(a)
            for key, value in graph[a].items():
                if key in seen:
                    continue

                res = divide(key, b)
                if res > 0:
                    return float(res * value)
            return -1.000

        ans = []
        for q in queries:
            a, b = q[0], q[1]

            if a not in graph or b not in graph:
                ans.append(-1.000)
                continue

            seen = set()
            ans.append(divide(a, b))

        return ans