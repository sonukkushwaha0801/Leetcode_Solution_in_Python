# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import defaultdict, deque


class Solution:
  def checkIfPrerequisite(self,numCourses: int,prerequisites: list[list[int]],queries: list[list[int]]) -> list[bool]:
    graph = [[] for _ in range(numCourses)]
    isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
    for u, v in prerequisites:
      graph[u].append(v)
    for i in range(numCourses):
      self._dfs(graph, i, isPrerequisite[i])
    return [isPrerequisite[u][v] for u, v in queries]

  def _dfs(self, graph: list[list[int]], u: int, used: list[bool]) -> None:
    for v in graph[u]:
      if used[v]:
        continue
      used[v] = True
      self._dfs(graph, v, used)

    
# Another way:
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:

        n = numCourses
        hasPrereq = [0 for _ in range(n)]
        inDegree = [0 for _ in range(n)]
        adjList = defaultdict(list)

        for a, b in prerequisites:
            inDegree[b] += 1
            adjList[a].append(b)
        
        q = deque()
        for i in range(n):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            currNode = q.popleft()
            for nextNode in adjList[currNode]:
                hasPrereq[nextNode] = hasPrereq[nextNode] | hasPrereq[currNode] 
                hasPrereq[nextNode] = hasPrereq[nextNode] | (1 << currNode) 

                inDegree[nextNode] -= 1
                if inDegree[nextNode] == 0: 
                    q.append(nextNode)
        
        ans = []
        for u, v in queries:
            ans.append(hasPrereq[v] & (1 << u) != 0) 
        return ans