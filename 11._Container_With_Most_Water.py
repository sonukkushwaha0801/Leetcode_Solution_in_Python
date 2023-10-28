# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxArea(self, height):
        left = 0            
        right = len(height) - 1 
        maxWater = 0        
        
        while left < right:
            width = right - left
            
            h = min(height[left], height[right])
            
            water = width * h
            
            maxWater = max(maxWater, water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater
    
# Another way:
class Solution:
    def maxArea(self, hit) -> int:
        mx = 0
        i = 0
        size = len(hit) - 1
        while i < size:
            dif = size - i
            mn = min(hit[i], hit[size])
            mx = max(mx, dif * mn)
            
            if hit[i] < hit[size]:
                i += 1
            else :
                size -= 1
        return mx