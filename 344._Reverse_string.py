# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()

# Second Type:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for n in range(len(s)//2):
            temp = s[len(s)-n-1]
            s[len(s)-n-1] = s[n]
            s[n] = temp

