# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

import random
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
    
# Another way:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        flag = True
        def partition(arr, low, high):
            nonlocal flag
            pivot = arr[low + (high - low) // 2]
            if flag:
                pivot = arr[random.randint(low , high)]
            flag ^= True
            left = low
            right = high
            while left <= right:
                while arr[left] < pivot:
                    left += 1
                while arr[right] > pivot:
                    right -= 1
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
            return left, right

        def quickSort(arr, low, high):
            if low < high:
                mid_left, mid_right = partition(arr, low, high)
                quickSort(arr, low, mid_right)
                quickSort(arr, mid_left, high)
            return arr

        return quickSort(nums, 0, len(nums) - 1)