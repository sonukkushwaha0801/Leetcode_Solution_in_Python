# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        nums.append(n+1)
        has1=False
        for i in range(n+1):
            if nums[i]==1: has1=True
            elif nums[i]<=0 or nums[i]>n:
                nums[i]=1
        
        if has1==False: return 1
        bitMask=(1<<17)-1

        for x in nums:
            seen=x & bitMask
            nums[seen]|=(1<<17)

        for i in range(1, n+1):
            if (nums[i]>>17)==0:
                return i
        return n+1
        
# Another way:
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums=set(nums)
        for i in range(1,2147483647):
            if i not in nums:      return i