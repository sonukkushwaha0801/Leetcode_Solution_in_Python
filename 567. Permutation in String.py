# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        if s1_count == window_count:
            return True
        for i in range(len(s1), len(s2)):
            window_count[s2[i]] += 1
            window_count[s2[i - len(s1)]] -= 1
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            if window_count == s1_count:
                return True
        return False
    

# Another way:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1, dic2 = {}, {}
        
        for i in s1: 
            dic1[i] = dic1.get(i, 0) + 1
        
        m, n = len(s1), len(s2)
        
        if m > n:
            return False
        
        for i in range(m):
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        
        for i in range(m, n):
            if dic1 == dic2:
                return True

            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
            
            dic2[s2[i - m]] -= 1
            if dic2[s2[i - m]] == 0:
                del dic2[s2[i - m]]
        
        return dic1 == dic2