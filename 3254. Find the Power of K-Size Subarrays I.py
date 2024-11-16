# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            sorted_subarray = sorted(subarray)
            is_consecutive = all(sorted_subarray[j] - sorted_subarray[j - 1] == 1 for j in range(1, k))

            if is_consecutive and subarray == sorted_subarray:
                result.append(sorted_subarray[-1])  # Max element
            else:
                result.append(-1)

        return result
    
# Another way:
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        def is_consecutive_and_sorted(subarray):
            return all(subarray[i] + 1 == subarray[i + 1] for i in range(len(subarray) - 1))

        n = len(nums)
        result = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if is_consecutive_and_sorted(subarray):
                result.append(max(subarray))
            else:
                result.append(-1)
        
        return result