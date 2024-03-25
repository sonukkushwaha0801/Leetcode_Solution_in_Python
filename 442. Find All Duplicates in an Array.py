# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n=len(nums)
        p=10**5+3
        ans=[]
        for x in nums:
            next=(x%p)-1
            if nums[next]>p:
                ans.append(next+1)
            nums[next]+=p
        return ans
        
# Another way: 
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        mapNums = {}
        for num in nums:
            if num in mapNums:
                mapNums[num] += 1
            else:
                mapNums[num] = 1
        return [k for k, v in mapNums.items() if v == 2]
        