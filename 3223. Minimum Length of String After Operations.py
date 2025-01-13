# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if x % 2 else 2 for x in Counter(s).values())
    
# Another way:
class Solution:

    def minimumLength(self, s: str) -> int:
        s_set = set(s)
        ans = 0
        for ch in s_set:
            if s.count(ch) & 1:
                ans += 1
            else:
                ans += 2
        return ans