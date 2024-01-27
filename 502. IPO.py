# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        cap_pro,executable_pro = [],[]
        for p,c in zip(profits,capital): heapq.heappush(cap_pro,(c,-p)) 
        for _ in range(k):
            while cap_pro: 
                cur_project = heapq.heappop(cap_pro)                   
                if cur_project[0]>w:
                    heapq.heappush(cap_pro,cur_project)                         
                    break
                heapq.heappush(executable_pro,cur_project[1])
            if executable_pro: w += -heapq.heappop(executable_pro)
        return w

# Another way:
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        unavailableProjects = []
        availableProjects = []
        currentCapital = w
        for i in range(len(profits)):
            if (capital[i] <= w):
                heapq.heappush(availableProjects, -profits[i])
            else:
                heapq.heappush(unavailableProjects, (capital[i], -profits[i]))
        projectNumber = 0
        while (projectNumber < k):
            if (len(availableProjects) == 0):
                return currentCapital
            currentCapital -= heapq.heappop(availableProjects)
            while (len(unavailableProjects) != 0 and unavailableProjects[0][0] <= currentCapital):
                heapq.heappush(availableProjects, heapq.heappop(unavailableProjects)[1])
            projectNumber += 1
        return currentCapital
        