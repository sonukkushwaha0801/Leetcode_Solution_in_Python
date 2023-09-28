# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]

# Type Two:
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_numbers = []
        odd_numbers = []
        for num in nums:
            if num % 2 == 0:
                even_numbers.append(num) 
                odd_numbers.append(num)
        result = even_numbers + odd_numbers
        
        return result  