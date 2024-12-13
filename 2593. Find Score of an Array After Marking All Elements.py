# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from heapq import heappush, heappop
from typing import List

class Solution:
    def findScore(self, nums):
        n = len(nums)
        pq = []
        for i, val in enumerate(nums):
            heappush(pq, (val, i))
        
        sum_ = 0
        vis = [False] * n
        while pq:
            val, ind = heappop(pq)
            if vis[ind]:
                continue
            sum_ += val
            vis[ind] = True
            if ind - 1 >= 0:
                vis[ind - 1] = True
            if ind + 1 < n:
                vis[ind + 1] = True
        return sum_
    
# Another way:
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        sum, r=0, 0
        while r<n:
            l=r
            while r+1<n and nums[r]>nums[r+1]:
                r+=1
            for i in range(r, l-1, -2):
                sum+=nums[i]
            r+=2
        return sum
        