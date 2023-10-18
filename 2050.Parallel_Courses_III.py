# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import defaultdict
import heapq

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * n

        for relation in relations:
            prev_course, next_course = relation
            graph[prev_course - 1].append(next_course - 1)
            in_degree[next_course - 1] += 1

        min_heap = []
        for i in range(n):
            if in_degree[i] == 0:
                heapq.heappush(min_heap, (time[i], i))

        while min_heap:
            course_time, current_course = heapq.heappop(min_heap)

            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    heapq.heappush(min_heap, (course_time + time[next_course], next_course))

        return course_time

# Another way:
import heapq
from collections import defaultdict, Counter

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        vs = defaultdict(list)
        n_prev_courses = [0] * n
        for u, v in relations:
            vs[u - 1].append(v - 1)
            n_prev_courses[v - 1] += 1
        
        h = [
            (time[u], u)
            for u in range(n)
            if n_prev_courses[u] == 0
        ]
        heapq.heapify(h)

        while h:
            dt, u = heapq.heappop(h)
            for v in vs[u]:
                n_prev_courses[v] -= 1
                if n_prev_courses[v] == 0:
                    heapq.heappush(h, (dt + time[v], v))
        
        return dt