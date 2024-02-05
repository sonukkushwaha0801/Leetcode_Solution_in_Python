# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=[[-1, 0] for _ in range(26)]
        n=len(s)
        for i, c in enumerate(s):
            idx=ord(c)-ord('a')
            freq[idx][0]=i
            freq[idx][1]+=1

        ans=n
        for i, f in freq:
            if f==1:
                ans=min(ans, i)
        if ans==n: ans=-1
        return ans
        
# Another way:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        return min([i for i in range(len(s)) if c[s[i]] == 1], default = -1)