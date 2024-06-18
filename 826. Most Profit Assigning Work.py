# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res, j, best, temp = 0, 0, 0, []
        
        for i in range(len(worker)):
            temp.append((difficulty[i], profit[i]))
        
        temp.sort()
        worker.sort()
        
        for work in worker:
            while j < len(temp) and work >= temp[j][0]:
                best = max(best, temp[j][1])
                j += 1
            
            res += best
        
        return res

# Another way:
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
            sorted_worker=sorted(worker)
            jobs=zip(difficulty,profit)
            sorted_jobs=sorted(jobs)
            n=len(sorted_jobs)
            best_profit=0
            total_best_profit=0
            i=0
            for skill in sorted_worker:
                while i<n and skill>=sorted_jobs[i][0]:
                    best_profit=max(best_profit, sorted_jobs[i][1])
                    i+=1
                total_best_profit+=best_profit
            return total_best_profit        