# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(x[11:13]) > 60 for x in details)
    

# Another way:
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for s in details:
            if int(s[11:13]) > 60:
                ans += 1
        return ans
        