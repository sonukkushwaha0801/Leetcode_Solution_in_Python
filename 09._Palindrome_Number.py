# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one
class Solution:
    def isPalindrome(self, x):
        if x < 0:
         return False
        rev_x = 0
        temp = x
        while temp != 0:
            curr = temp % 10
            rev_x = rev_x * 10 + curr
            temp = temp // 10
        if rev_x == x:
            return True
        else:
            return False

# type second
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if (x==x[::-1]):
            return True
        return False