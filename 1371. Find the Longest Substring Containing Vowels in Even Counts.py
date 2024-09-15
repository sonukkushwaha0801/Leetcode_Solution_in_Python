# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        D = {
            'a':0b00001,
            'e':0b00010,
            'i':0b00100,
            'o':0b01000,
            'u':0b10000
        }
        M = {}
        s = " " + s
        cur = 0b00000
        res = 0
        for i, c in enumerate(s):
            cur ^= D.get(c, 0b00000)
            if cur in M:
                res = max(res, i - M[cur])
            else:
                M[cur] = i
        return res

# One Liner
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        return (d:={}) or max(i-d.setdefault(p,i) for i,p in enumerate(accumulate(s, lambda p,c: 1<<'aeiou'.find(c)+1^1^p, initial=0),-1))