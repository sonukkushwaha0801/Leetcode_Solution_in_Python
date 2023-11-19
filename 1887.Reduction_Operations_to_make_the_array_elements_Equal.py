#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution(object):
    def reductionOperations(self, nums):
        n = len(nums)
        freq = [0] * 50001
        for num in nums:
            freq[num] += 1
        res, operations = 0, 0
        for i in range(50000, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                res += operations - freq[i]
        return res
        
# Another way:
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        return sum([i*cnt for i, (num, cnt) in enumerate(sorted(Counter(nums).items()))])