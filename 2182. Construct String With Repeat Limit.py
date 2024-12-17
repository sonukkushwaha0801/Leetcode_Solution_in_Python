# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        freq = Counter(s)
        pq = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(pq)
        
        result = []
        while pq:
            ch, count = heapq.heappop(pq)
            ch = chr(-ch)
            used = min(k, count)
            result.append(ch * used)
            count -= used
            
            if count > 0:
                if not pq: break
                next_ch, next_count = heapq.heappop(pq)
                result.append(chr(-next_ch))
                next_count -= 1
                
                if next_count > 0:
                    heapq.heappush(pq, (next_ch, next_count))
                heapq.heappush(pq, (-ord(ch), count))
        
        return "".join(result)
    
