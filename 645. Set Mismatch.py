# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sumtoN = n*(n+1)//2
        missingNum = sumtoN - sum(set(nums))
        duplicateNum = sum(nums) - (sumtoN - missingNum)
        return [duplicateNum,missingNum]

# Another way:
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        return [sum(nums)-sum(set(nums)), len(nums)*(len(nums)+1)//2-sum(set(nums))]
        