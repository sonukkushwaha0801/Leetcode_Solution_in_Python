# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for i, num in enumerate(arr2):
            order[num] = i
        return list(sorted(arr1, key=lambda x: (order.get(x, 1000), x)))
    
# Another way to solve:
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return (lambda order=(dict((num, i) for i, num in enumerate(arr2))): sorted(arr1, key=lambda x: (order.get(x, 1000), x)))()