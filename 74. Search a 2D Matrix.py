# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import chain


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def BinarySearch(resCol, low, high, target):
            while low <= high:
                mid = (low+high) // 2
                if resCol[mid] == target:
                    return True
                elif resCol[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                resCol = matrix[mid]
                return BinarySearch(resCol, 0, len(resCol), target)
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

# Another way:
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return target in list(chain.from_iterable(matrix))