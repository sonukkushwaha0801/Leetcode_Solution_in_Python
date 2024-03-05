# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque
from itertools import groupby


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1
        
        return right - left + 1
    
# Another way:
class Solution:
    def minimumLength(self, s: str) -> int:
        Q = deque((k, len(list(v))) for k, v in groupby(s))
        while len(Q) > 2 and Q[0][0] == Q[-1][0]:
            Q.popleft(), Q.pop()
        return sum(q[1] for q in Q) if len(Q) > 1 else int(Q[0][1] == 1)