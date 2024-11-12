# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        max_beauty_at_price = []
        current_max_beauty = 0
        
        for price, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            max_beauty_at_price.append((price, current_max_beauty))
        
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        result = [0] * len(queries)
        
        for query, original_index in sorted_queries:
            idx = bisect_right(max_beauty_at_price, (query, float('inf'))) - 1
            if idx >= 0:
                result[original_index] = max_beauty_at_price[idx][1]
            else:
                result[original_index] = 0
        return result
    
# Another way:
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        beuties = [0]*len(queries)
        items = sorted(items, key = lambda x : (x[1], x[0]), reverse=True)
        for x in range(len(queries)):
            for y in range(len(items)):
                if queries[x] >= items[y][0]:
                    beuties[x] = items[y][1]
                    break            
        return beuties   

        