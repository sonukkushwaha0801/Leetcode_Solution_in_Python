# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            x=nums.index(min(nums))
            nums[x]*=multiplier
        return nums
    
# Another way:
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = []
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        while k > 0:
            lowest_num, index = heapq.heappop(heap)
            heapq.heappush(heap, (lowest_num * multiplier, index))
            k -= 1
        while heap:
            num, index = heapq.heappop(heap)
            res[index] = num

        return res 