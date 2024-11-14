# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import math
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(maxProducts):
            storesNeeded = 0
            for quantity in quantities:
                storesNeeded += math.ceil(quantity / maxProducts)
                if storesNeeded > n:
                    return False
            return storesNeeded <= n

        low, high = 1, max(quantities)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if canDistribute(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

# Another way:
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start = 1
        end = max(quantities)
        
        while start <= end:
            mid = start + (end - start) // 2
            total = sum((element // mid) + (1 if (element % mid) > 0 else 0) for element in quantities)
            
            if total <= n:
                end = mid - 1
            else:
                start = mid + 1
        return start