# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter, List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=[0]*201
        for x in nums:
            freq[x+100]-=1 
        return sorted(nums, key=lambda x:(freq[x+100], x), reverse=True)
        

# One liner
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:(Counter(nums)[x],-x))