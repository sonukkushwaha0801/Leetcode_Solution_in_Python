# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(str(1^int(n)) for n in f'{num:b}'), 2)
    
# Another way:
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1
        
        return num ^ mask