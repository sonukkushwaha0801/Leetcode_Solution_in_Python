# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        window = 0
        for i in range(min(3, len(arr))):
            window += arr[i] % 2
        if window == 3:
            return True
        for i in range(3, len(arr)):
            window += arr[i] % 2
            window -= arr[i - 3] % 2
            if window == 3:
                return True
        return False

# Another way:
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr)-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False