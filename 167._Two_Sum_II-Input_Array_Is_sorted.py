# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) -1
        
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
               i+=1 
        
        return []
    
# Another way:
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,len(numbers)-1
        while(l<r):
            sum=numbers[l]+numbers[r]
            if(sum==target):return [l+1,r+1]
            elif sum>target:r-=1
            else:l+=1