# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        return min(sum(v&~1 for v in Counter(s).values())+1,len(s))
    
# Another solution:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        ans=0
        for i in c.values():
            ans+=int(i/2)*2
            if ans%2==0 and i%2==1:
                ans+=1
        return ans        