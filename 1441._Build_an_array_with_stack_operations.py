# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        lst=[]
        for i in range(1,n+1):
            if i in target:
                lst.append("Push")
            else:
                lst.append("Push")
                lst.append("Pop")
            if i==target[-1]:
                break
        return lst

#Another way:
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        target_set = set(target)
        result = []
        
        for i in range(1, target[-1] + 1):
            if i in target_set:
                result.append("Push")
            else:
                result.append("Push")
                result.append("Pop")
                
        return result
    
