# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        prev_max = 0
        for idx, x in enumerate(arr):
            prev_max = max(prev_max, x)
            if prev_max == idx:
                ans += 1
        return ans
    
# Another way:
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk_max = deque()
        for i in arr:
            temp = i
            if (len(chunk_max) > 0) and (i < chunk_max[-1]):
                temp = chunk_max.pop()
                while (len(chunk_max) > 0) and (i < chunk_max[-1]):
                    chunk_max.pop()
            chunk_max.append(temp)
        return len(chunk_max)



        