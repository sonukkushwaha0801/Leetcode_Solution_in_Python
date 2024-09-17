# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s: str, t: str) -> List[str]:
        return [w for w,f in Counter((s+' '+t).split()).items() if f<2]
    
# Another way:
class Solution:
    def uncommonFromSentences(self, s: str, t: str) -> List[str]:
        return (p:={*(q:=(s+' '+t).split())})-{*Counter(q)-Counter(p)}