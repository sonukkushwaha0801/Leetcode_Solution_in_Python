# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution(object):
    def isHappy(self, n):
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        return n == 1

# Another Way:
class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4: n = sum(int(i)**2 for i in str(n))
        return n == 1