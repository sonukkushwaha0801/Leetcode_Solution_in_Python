# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        first = second = 0
        
        while first < len(version1) or second < len(version2):
            num1 = num2 = 0
            while first < len(version1) and version1[first] != '.':
                num1 = num1 * 10 + int(version1[first])
                first +=1
            while second < len(version2) and version2[second] != '.':
                num2 = num2 * 10 + int(version2[second])
                second += 1
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

            first +=1 
            second +=1
            
        return(0)
    
# Another way:
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        m = len(v1)
        n = len(v2)
        for i in range(max(m, n)):
            i1 = int(v1[i]) if i < m else 0 
            i2 = int(v2[i]) if i < n else 0
            if i1 > i2:
                return 1
            if i1 < i2:
                return -1
        return 0 