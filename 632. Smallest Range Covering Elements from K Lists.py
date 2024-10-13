# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0)) 
            current_max = max(current_max, nums[i][0])
        
        result_range = [-10**5, 10**5]
        
        while min_heap:
            current_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            if current_max - current_min < result_range[1] - result_range[0]:
                result_range = [current_min, current_max]
            
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            next_elem = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
            
            current_max = max(current_max, next_elem)
        
        return result_range
    
# Another way:
from collections import defaultdict

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        allNums = [(num, i) for i, sublist in enumerate(nums) for num in sublist]
        allNums.sort()
        count = defaultdict(int)
        total_lists = len(nums)
        lists_in_window = 0
        l = 0
        min_range = float('inf')
        result = [-1, -1]
        for r in range(len(allNums)):
            num, idx = allNums[r] 
            count[idx] += 1
            if count[idx] == 1:
                lists_in_window += 1
            while lists_in_window == total_lists:
                current_range = allNums[r][0] - allNums[l][0]
                if current_range < min_range:
                    min_range = current_range
                    result = [allNums[l][0], allNums[r][0]]
                count[allNums[l][1]] -= 1
                if count[allNums[l][1]] == 0: 
                    lists_in_window -= 1
                l += 1 
        return result