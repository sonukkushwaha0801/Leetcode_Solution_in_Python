# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key= lambda n: int(''.join(str(mapping[int(i)]) for i in str(n))))
    
# Another solution:
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        null=[]
        for num in nums:
            curr=0
            num=str(num)
            for i in range(len(num)):
                curr=curr*10+mapping[int(num[i])]
            null.append(curr)
        print(null)

        idx=[i for i in range(len(null))]
        idx.sort(key=lambda x:null[x])
        print(idx)
        res=[]
        for index in idx:
            res.append(nums[index])
        return res