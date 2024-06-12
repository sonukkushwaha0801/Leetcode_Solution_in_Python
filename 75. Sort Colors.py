# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

# Type two:
class Solution:
    def sortColors(self, nums):
        count_map = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count_map[num] += 1
    
        index = 0
        for color in range(3):
            while count_map[color] > 0:
                nums[index] = color
                index += 1
                count_map[color] -= 1