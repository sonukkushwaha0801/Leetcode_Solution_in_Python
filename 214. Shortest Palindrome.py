# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#Solution:
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def getLpsArray(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        temp = s + "#" + s[::-1]
        lps = getLpsArray(temp)
        longest = lps[-1]
        toAdd = s[longest:][::-1]
        return toAdd + s
    
# Another way:
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s