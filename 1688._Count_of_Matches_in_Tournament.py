# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
        
# Another way:
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n % 2 == 0:
                matches += (n // 2)
                n = (n //2)
            else:
                matches += ((n-1)//2)
                n = ((n-1)//2) + 1
        return matches