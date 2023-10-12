#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n =mountain_arr.length()
    
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) <mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left 
        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            mid_val =mountain_arr.get(mid)
            
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = peak, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val =mountain_arr.get(mid)
            
            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1