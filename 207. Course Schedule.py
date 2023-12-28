# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque
import collections
class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n

# Another way:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Topological Sort
        alist = collections.defaultdict(list)
        order = [0]*numCourses
        for i,j in prerequisites:
            alist[j].append(i)
            order[i]+=1
        q = collections.deque()
        for i in range(len(order)):
            if order[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            current = q.popleft()
            count+=1
            for i in alist[current]:
                order[i]-=1
                if order[i]==0:
                    q.append(i)
        
        return count == numCourses