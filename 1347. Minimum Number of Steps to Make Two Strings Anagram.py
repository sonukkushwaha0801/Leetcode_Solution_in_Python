# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s)-Counter(t)).values()) 

# Another way:
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq=[0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1
        for c in t:
            freq[ord(c)-ord('a')]-=1
        ans=0
        for i in range(26):
            if freq[i]>0:
                ans+=freq[i]
        return ans