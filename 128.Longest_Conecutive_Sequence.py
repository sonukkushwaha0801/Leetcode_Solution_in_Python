#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map=set()
        for i in nums:
            map.add(i)

        m=0

        for i in nums:
            if i-1 not in map:
                j=0
                while i+j in map:
                    j+=1
                m=max(m,j)
        return m
# Another way:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map=set()
        for i in nums:
            map.add(i)
        
        m=0
        
        for i in range(len(nums)):
            s=0
            if nums[i]-1 not in map:
            
                for j in range(len(nums)):
                    if nums[i]+j in map:
                        s+=1
                    else:
                        break

                m=max(m,s)
        
        return m
        
        