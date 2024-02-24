# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import defaultdict, deque
import heapq


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        known_set = set([0, firstPerson])
        
        sorted_meetings = []
        meetings.sort(key=lambda x:x[2])

        seen_time = set()
        
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)
            
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            queue = deque((people_know_secret))
        
            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        return list(known_set)
    
#Another way:
class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        graph = defaultdict(list)

        for x,y,t in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))

        heap = [(0,firstPerson)] #time,person
        for nei,time in graph[0]:
            heapq.heappush(heap,(time,nei))
        
        visited = set([0])

        while heap:
            time,person = heapq.heappop(heap)

            if person in visited:
                continue

            visited.add(person)

            for nei,t in graph[person]:
                if t>=time:
                    heapq.heappush(heap,(t,nei))

        return visited