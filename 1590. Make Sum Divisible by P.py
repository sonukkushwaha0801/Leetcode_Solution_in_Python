# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0  
        result = len(nums)
        prefixsum = 0
        dictremainder = {0: -1}
        for i in range(len(nums)):
            prefixsum += nums[i]
            curremainder = prefixsum % p
            target = (curremainder - remainder) % p
            if target in dictremainder:
                result = min(result, i - dictremainder[target])
            dictremainder[curremainder] = i  
        return result if result < len(nums) else -1
    
# Another way:

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        target = sum(nums) % p
        dic,n = {0:-1},len(nums)
        cur,ret = 0,n
        for i,num in enumerate(nums):
            cur = (cur+num)%p
            if dic.get((cur-target)%p) is not None:
                ret = min(ret,i-dic.get((cur-target)%p))
            dic[cur] = i
        return ret if ret < n else -1