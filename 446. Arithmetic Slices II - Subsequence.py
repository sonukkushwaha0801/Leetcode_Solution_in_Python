# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter, defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count, memo  = Counter(nums), Counter()  
        diff, res, d = defaultdict(Counter), 0, 0 

        for num in reversed(nums):
            if num in diff:
                res += sum(diff[num].values())

                for dif in diff[num]:
                    if count[(d := num + dif)]: 
                        diff[d][dif] += diff[num][dif] 

            for used in memo:
                d = num + (dif := num - used)  
                if count[d]: diff[d][dif] += memo[used] 

            memo[num]  += 1  
            count[num] -= 1  

        return res
    
#Another way:
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total, n = 0, len(nums)
        dp = [defaultdict(int) for _ in nums]
        for i in range(1, n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
        return total