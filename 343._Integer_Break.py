# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        
        count_of_3s, remainder = divmod(n, 3)
        print(count_of_3s,remainder)
        
        if remainder == 0:
            return 3 ** count_of_3s
        elif remainder == 1:
            return 3 ** (count_of_3s - 1) * 4
        else:  
            return 3 ** count_of_3s * 2

# Another Way:
class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1
        if n == 2:
            return 1
        elif n == 3:
            return 2
        while n > 4:
            res = res * 3
            n-=3
        return res*n
