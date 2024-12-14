# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List
from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()
        start = 0
        total_subarrays = 0
        for end in range(n):
            sorted_window.add(nums[end])
            while sorted_window[-1] - sorted_window[0] > 2:
                sorted_window.remove(nums[start])
                start += 1
            total_subarrays += end - start + 1
        return total_subarrays
    
# ANother way:
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i = res = 0
        d = dict()
        for j, num in enumerate(nums):
            t = d.copy()
            for k, v in t.items():
                if abs(k - num) > 2:
                    i = max(i, v + 1)
                    d.pop(k)
            d[num] = j
            res += j - i + 1
        return res