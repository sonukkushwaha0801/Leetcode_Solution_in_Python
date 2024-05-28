# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        currentCost = 0
        maxLength = 0
        
        for end in range(len(s)):
            currentCost += abs(ord(s[end]) - ord(t[end]))
            
            while currentCost > maxCost:
                currentCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
    
# Another way:
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = ans = curr = 0
        for i in range(len(s)):
            curr += abs(ord(s[i]) - ord(t[i]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, i - left + 1)
        return ans