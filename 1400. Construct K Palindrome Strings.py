# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n=len(s)
        if n<k: return False
        freq=[False]*26
        for c in s:
            freq[ord(c)-97]^=1
        return freq.count(True)<=k
        

# Another way:
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        from collections import Counter
        freq = Counter(s)
        
        odds = sum(1 for count in freq.values() if count % 2 != 0)
        
        return odds <= k