# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
 
from typing import Counter, List


class Solution:
    def maxEqualRowsAfterFlips(self, g: List[List[int]]) -> int:
        return max(Counter(tuple(v^r[0] for v in r) for r in g).values())

# Another way:

class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        pat_freq = Counter() 
        
        for r in mat:
            pattern = tuple(r) if r[0] == 0 else tuple(bit ^ 1 for bit in r) 
            pat_freq[pattern] += 1  
            
        return max(pat_freq.values())  