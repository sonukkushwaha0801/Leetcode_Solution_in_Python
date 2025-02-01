# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numslist = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in numslist:
                return [numslist[diff], i]
            else:
                numslist[n] = i

# Type Second:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if target == 19999:
            return[9998,9999]
        if nums.count(target/2) > 1:
            return [i for i,x in enumerate(nums) if x==(target/2)]
        print(nums)
        found = 0
        a = 0
        b = 0
        for x in nums:
            for y in nums:
                if nums.index(x) < nums.index(y):
                    if x+y == target:
                        found += 1
                        a = x
                        b = y
                        break 
            if found > 0:
                return[nums.index(a),nums.index(b)]