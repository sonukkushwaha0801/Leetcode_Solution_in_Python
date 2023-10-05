# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from  collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        element_count = Counter(nums)
        majority_elements = []
        threshold = len(nums) // 3
        
        for element, count in element_count.items():
            if count > threshold:
                majority_elements.append(element)
        return majority_elements

# One Liner solution: 
class Solution:
    def majorityElement(self, nums):
        return [num for num, count in Counter(nums).items() if count > len(nums) // 3]