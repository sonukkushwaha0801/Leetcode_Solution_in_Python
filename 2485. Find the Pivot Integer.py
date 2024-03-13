# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from math import sqrt


class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)
        
# Another way:
def pivotInteger(self, n: int) -> int:
    cumulative_sum = 0
    sum1 = [cumulative_sum := cumulative_sum + i for i in range(1, n + 1)]
    cumulative_sum = 0
    sum2 = [cumulative_sum := cumulative_sum + i for i in range(n, 0, -1)]
    for i in range(n):
        if sum1[i] == sum2[n - i - 1]:
            return i + 1
    return -1