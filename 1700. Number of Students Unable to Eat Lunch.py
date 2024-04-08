# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from collections import Counter


class Solution:
    def countStudents(self, st: list[int], sw: list[int]) -> int:
        return next((len(st) for q in sw if q not in st or st.remove(q)),0)
    
# Another way:
class Solution:
    def countStudents(self, st: list[int], sa: list[int]) -> int:
        ct = Counter(st)
        for s in sa:
            if ct[s] > 0: 
                ct[s] -= 1
            else:
                return ct.total()
        return 0