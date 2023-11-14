#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        count = 0
        for i in range(26):
            l, r = s.find(chr(i + 97)), s.rfind(chr(i + 97))
            if l != -1 and r != -1:
                count += len(set(s[l + 1:r]))
        return count
    
# Another way:
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        characters = {chr(x) for x in range(97,123,1)}
        for k in characters:
            first,last = s.find(k),s.rfind(k)
            if first!=-1:
                res+=len(set(s[first+1:last]))
        return res