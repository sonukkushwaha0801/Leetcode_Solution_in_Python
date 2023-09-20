# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
"""#type first
class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		if int(num**0.5)*int(num**0.5)==num:
			return True
		else:
			return False
"""
# Second Type:

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
    
# Third Solution Type:
class Solution(object):
    def isPerfectSquare(self, num):
        low, high = 1, num
        while low <= high:
            mid = (low + high) / 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
    
# Fourth Type:
class Solution(object):
    def isPerfectSquare(self, num):
        x = num
        while x * x > num:
            x = (x + num / x) / 2
        return x * x == num