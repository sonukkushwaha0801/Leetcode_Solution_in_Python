# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num[:next((i for i in range(len(num)-1, -1, -1) if ord(num[i]) &1==1), -1) + 1]


# Another way:
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
            
        return ""
