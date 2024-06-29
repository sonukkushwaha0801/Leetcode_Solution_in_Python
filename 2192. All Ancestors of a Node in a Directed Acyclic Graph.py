# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        map = [set() for _ in range(n)]
        res = [[] for _ in range(n)]
        visited = [False] * n

        def dfs(v: int, p: int):
            visited[v] = True
            if v != p:
                res[v].append(p)
            for x in map[v]:
                if not visited[x]:
                    dfs(x, p)

        for u, v in edges:
            map[u].add(v)

        for i in range(n):
            visited = [False] * n
            dfs(i, i)

        return res
    
# Another way:
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for _ in range(n)]
        g = [[] for _ in range(n)]
        for f, t in edges:
            g[t].append(f)

        q0 = []
        q1 = []
        for start, ancestors in enumerate(answer):
            for prev in g[start]:
                q0.append(prev)
            while q0:
                for cur in q0:
                    if cur not in ancestors:
                        ancestors.add(cur)
                        for prev in g[cur]:
                            q1.append(prev)
                q1, q0 = q0, q1
                q1.clear()
        for i, ancestors in enumerate(answer):
            answer[i] = sorted(ancestors)
        return answer