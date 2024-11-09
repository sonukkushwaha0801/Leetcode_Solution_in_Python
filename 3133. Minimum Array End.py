# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        mask_x, mask_n = 1, 1
        while mask_n < n:    
            if not(mask_x & x):
                if mask_n & (n-1):
                    x |= mask_x
                mask_n <<= 1
            mask_x <<= 1
        return x

# Another way:

class Solution:
    def output(self, n: int, x: int) -> int:
        output = n-1
        for i in range(30):
            if x & (1 << i):
                right = output & ((1 << i) - 1)
                left = output - right
                left = (left << 1) + (1 << i)
                output = right + left
        return output
        