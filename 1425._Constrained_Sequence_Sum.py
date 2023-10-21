# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque
from copy import copy
class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        dp = copy.deepcopy(nums)
        q = deque()
        q.append(0)
        for i in range(1,len(nums)):
            while(q[-1] < i-k ):
                q.pop()
            dp[i] = max(dp[i],dp[q[-1]]+nums[i])
            while( len(q)>0 and dp[q[0]] <= dp[i] ):
                q.popleft()
            q.appendleft(i)
        return max(dp)
    
#Another Way:
import heapq

class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:

        dp = [float('-inf')] * (len(nums))
        heap = []
        for i in range(len(nums) - 1, -1, -1):
            maxi = nums[i]
            terminal = i + k

            while heap and heap[0][1] > terminal:
                heapq.heappop(heap)

            if heap: 
                add = max(0, -heap[0][0])
                maxi += add
            
            dp[i] = maxi
            heapq.heappush(heap, [-maxi, i])
        return max(dp)