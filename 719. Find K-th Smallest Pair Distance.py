# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def smallestDistancePair(self, numbers: List[int], k: int) -> int:
        numbers.sort()
        minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            if self.countPairsWithinDistance(numbers, midDistance) < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance
        
        return minDistance

    def countPairsWithinDistance(self, numbers: List[int], targetDistance: int) -> int:
        count = left = 0
        for right in range(1, len(numbers)):
            while numbers[right] - numbers[left] > targetDistance:
                left += 1
            count += right - left
        return count
    
# Another way:
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        
        def count_pairs(mid):
            count = 0
            i = 0
            for j in range(n):
                while nums[j] - nums[i] > mid:
                    i += 1
                count += j - i
            return count
        
        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left