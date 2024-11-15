# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # sentinel
        arr.append(float("inf"))
        arr.insert(0, 0)
        left = 0
        right = len(arr) - 1
        shortest = float("inf")
        while left < len(arr) - 2 and arr[left] <= arr[left + 1]:
            left += 1
        while left >= 0:
            while right - 1 > left and arr[right - 1] >= arr[left] and arr[right] >= arr[right - 1]:
                right -= 1
            shortest = min(shortest, right - left - 1)
            left -= 1
        return shortest
        
# Another way:
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
            
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
            
        if left == n - 1: 
            return 0
            
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        result = min(n - left - 1, right)
        
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
                
        return result