# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size, max_index = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        result = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1

        return result

# Another way:
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))

