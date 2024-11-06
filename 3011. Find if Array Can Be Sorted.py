# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from itertools import groupby
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        grouped_list = [sorted(group) for _, group in groupby(nums, lambda x: bin(x).count('1'))]        
        for i in range(1, len(grouped_list)):
            if grouped_list[i - 1][-1] > grouped_list[i][0]:
                return False
        return True
        
# Another way:
from sortedcontainers import SortedList
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        groups = []
        group = SortedList()
        setbits = bin(nums[0]).count('1')
        for n in nums:
            if (bits := bin(n).count('1')) != setbits:        
                groups.append(group.copy())
                group.clear() 
                setbits = bits
            group.add(n)
        groups.append(group)
        for i in range(1, len(groups)):
            if groups[i - 1][-1] > groups[i][0]:
                return False
        return True