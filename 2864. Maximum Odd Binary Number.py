# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")
        zeros_count = len(s) - ones_count

        return "1" * (ones_count - 1) + "0" * zeros_count + "1"
    
# Another way:
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1"*(n1:=s.count('1')-1)+"0"*(len(s)-n1-1)+"1"
        