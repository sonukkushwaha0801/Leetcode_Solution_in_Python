# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        mp = {}
        for char in s:
            mp[char] = mp.get(char, 0) + 1
        for char in order:
            if char in mp:
                result += char * mp[char]
                del mp[char]
        for char, count in mp.items():
            result += char * count
        return result
    
# Another way:
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ctr = Counter(s)
        ans = [ch*ctr[ch] for ch in order]
        ans.extend(filter(lambda x: x not in order,s))
        return ''.join(ans)
        