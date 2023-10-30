# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: [x.bit_count(), x])
        
# Another way:
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def custom_sort_key(num):
            bit_count = bin(num).count('1')
            return (bit_count, num)
        arr.sort(key=custom_sort_key)
        return arr