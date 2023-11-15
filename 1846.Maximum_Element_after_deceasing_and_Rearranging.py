#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from cv2 import reduce


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        return reduce(lambda r, n: min(r + 1, n), sorted(arr)[1:], 1)

# Another way:
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        prev = 1
        for num in sorted(arr)[1:]:
            prev = min(prev + 1, num)
        
        return prev