# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#Solution:
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(0,len(nums)-1-i):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        result = list(map(str, nums))
        return ''.join(result) if nums[0] != 0 else "0"
    
