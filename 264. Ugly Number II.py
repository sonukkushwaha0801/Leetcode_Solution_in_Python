# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        
        i2 = i3 = i5 = 0
        
        while len(ugly) < n:
            next_ugly_2 = ugly[i2] * 2
            next_ugly_3 = ugly[i3] * 3
            next_ugly_5 = ugly[i5] * 5
            
            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)
            ugly.append(next_ugly)
            
            if next_ugly == next_ugly_2:
                i2 += 1
            if next_ugly == next_ugly_3:
                i3 += 1
            if next_ugly == next_ugly_5:
                i5 += 1
        
        return ugly[n-1]