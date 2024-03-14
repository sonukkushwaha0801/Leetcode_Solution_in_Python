# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return self.atMost(nums, goal)- self.atMost(nums, goal-1)

    def atMost(self, nums: list[int], goal: int) -> int:
        head, tail, total, result = 0, 0, 0, 0
        for head in range(len(nums)):
            total += nums[head]
            while total > goal and tail <= head:
                total -= nums[tail]
                tail += 1
            result += head - tail + 1
        return result
    
# Another way:
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0  
        prefix_sum = 0 
        sum_counts = {0: 1}  

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in sum_counts:
                count += sum_counts[prefix_sum - goal]
            sum_counts[prefix_sum] = sum_counts.get(prefix_sum, 0) + 1

        return count