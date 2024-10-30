# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

class Solution(object):
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        
        lis = [1] * n
        temp = []
        for i in range(n):
            pos = bisect_left(temp, nums[i])
            if pos < len(temp):
                temp[pos] = nums[i]
            else:
                temp.append(nums[i])
            lis[i] = pos + 1
        lds = [1] * n
        temp = []
        for i in range(n - 1, -1, -1):
            pos = bisect_left(temp, nums[i])
            if pos < len(temp):
                temp[pos] = nums[i]
            else:
                temp.append(nums[i])
            lds[i] = pos + 1

        max_mountain_len = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1: 
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)

        return n - max_mountain_len
    
# Another way:
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)

        right = [1 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        
        y = n
        for i in range(n):
            if left[i] > 1 and right[i] > 1:
                y = min(y, n - left[i] - right[i] + 1)
        
        return y