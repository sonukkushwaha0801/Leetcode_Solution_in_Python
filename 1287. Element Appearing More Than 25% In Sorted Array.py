# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
import bisect


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        return next(i for i in arr if arr.count(i) / len(arr) > 0.25)
    
# Another way:
class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n=len(arr)
        if n<4: return arr[0]
        q=[0, n//4, n//2, 3*n//4, n-1]
        x=[arr[0], arr[q[1]], arr[q[2]], arr[q[3]], arr[-1]]
        for i in range(4):
            if x[i]==x[i+1]: return x[i]
        print("binary search")
        for i in range(1,4):
            a=arr[q[i-1]:q[i+1]+1]
            r=bisect.bisect_right(a, x[i])-1
            l=bisect.bisect_left(a, x[i])
            if (r-l+1>n//4): return x[i]
        return -1
        