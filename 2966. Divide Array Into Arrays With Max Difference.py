# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            if i + 2 < len(nums):
                if nums[i + 2] - nums[i] > k:
                    return []
                res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res
                
# Another way:
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        lis=[]
        for i in range(0,len(nums)-2,3):
            if nums[i+2]-nums[i]<=k:
                lis.extend([[nums[i],nums[i+1],nums[i+2]]])
        return lis if len(lis)==len(nums)//3 else []