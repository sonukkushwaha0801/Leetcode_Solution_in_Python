# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n) -> int:
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        num_max_tasks = sum(1 for count in task_counts.values() if count == max_count)
        intervals = (max_count - 1) * (n + 1) + num_max_tasks
        return max(intervals, len(tasks))
    
# Another way:
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        ans=[0]*26
        for task in tasks:
            ans[ord(task)-ord('A')]+=1
        ans.sort()
        chunk=ans[25]-1
        idle=chunk*n
        for i in range(24,-1,-1):
            idle-=min(chunk,ans[i])
        if idle>=0:
            return len(tasks)+idle
        else:
            return len(tasks)        