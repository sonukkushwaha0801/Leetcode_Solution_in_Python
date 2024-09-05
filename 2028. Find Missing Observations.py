# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
from typing import List


class Solution:
    def missingRolls(self, rolls, mean: int, n: int):
        m = len(rolls)
        sumM = sum(rolls)
        total_sum = mean * (n + m)
        missing_sum = total_sum - sumM
        base_value = missing_sum // n
        remainder = missing_sum % n

        if base_value <= 0 or base_value > 6 or (base_value == 6 and remainder > 0):
            return []

        result = [base_value] * n
        for i in range(remainder):
            result[i] += 1
        return result
    
# Another way:
class Solution:
    def missingRolls(self, a: List[int], q: int, n: int) -> List[int]:
        return (n<=(p:=q*(n+len(a))-sum(a))<=n*6)*(p%n*[p//n+1]+(n-p%n)*[p//n])