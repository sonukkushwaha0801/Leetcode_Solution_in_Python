# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        v1, v2, ans = [], [], []
        
        for num in nums:
            if num > 0:
                v1.append(num)
            else:
                v2.append(num)
        
        ind1, ind2 = 0, 0
        
        while ind2 < len(nums) // 2:
            ans.append(v1[ind1])
            ind1 += 1
            ans.append(v2[ind2])
            ind2 += 1
        
        return ans

# Another way:
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos,neg = deque(),deque()

        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)

        for i in range(0,len(nums),2):
            nums[i],nums[i+1]=pos.popleft(),neg.popleft()

        return nums

nums = [3,1,-2,-5,2,-4]
Obj= Solution()
print(Obj.rearrangeArray(nums))