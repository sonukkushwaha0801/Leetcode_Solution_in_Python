# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
import collections
import math
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])      

# Another Type: 
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    print(nums[i],nums[j])
                    count += 1
        return count

Obj=Solution()
nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
print(Obj.numIdenticalPairs(nums))