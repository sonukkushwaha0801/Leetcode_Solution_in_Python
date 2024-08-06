# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import heapq
from typing import Counter


class Solution:
    def minimumPushes( self, word: str) -> int:
        # Count frequency of each character
        frequency_map = Counter(word)

        # Create a max heap based on character frequency
        max_heap = [(-freq, char) for char, freq in frequency_map.items()]
        heapq.heapify(max_heap)
        print(max_heap)

        count = 0
        j = 1
        
        # Calculate minimum pushes based on character priority
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq = -freq  # Convert back to positive frequency
            
            if j <= 8:
                count += freq
                
            elif j <= 16:
                count += freq * 2
            elif j <= 24:
                count += freq * 3
            else:
                count += freq * 4
            print(count)
            j += 1
        
        return count
    
# Another way:
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(f*(i//8+1) for i, f in enumerate(sorted(Counter(word).values(), reverse=True)))
        