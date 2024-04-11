# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        remain = len(num) - k
        for c in num:
            while k and stk and stk[-1] > c:
                stk.pop()
                k -= 1
            stk.append(c)
        return ''.join(stk[:remain]).lstrip('0') or '0'
    
# Another way:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if k >= n:
            return "0"

        result = []

        for i in range(n):
            digit = num[i]

            while k > 0 and result and result[-1] > digit:
                result.pop()
                k -= 1

            result.append(digit)

        result = result[:-k] if k > 0 else result

        result_str = ''.join(result).lstrip('0')

        return result_str if result_str else '0'
