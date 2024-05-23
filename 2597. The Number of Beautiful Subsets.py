# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter, List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(start, current_subset):
            nonlocal count
            
            if current_subset:
                count += 1
            
            for i in range(start, len(nums)):
                can_add = True
                for num in current_subset:
                    if abs(num - nums[i]) == k:
                        can_add = False
                        break
                        
                if can_add:
                    current_subset.append(nums[i])
                    backtrack(i + 1, current_subset)
                    current_subset.pop()
        
        nums.sort()
        count = 0
        backtrack(0, [])
        return count
        
# Another way:
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        buckets = [[] for _ in range(k)]
        for n in nums:
            buckets[n % k].append(n)
        
        def dp(bu):
            cnt = Counter(bu)
            arr = sorted((key, val) for key, val in cnt.items())
            dp_y, dp_n = 2**arr[0][1]-1, 1
            for i, (key, val) in enumerate(arr[1:], start=1):
                tmp = 2**val-1
                if key - arr[i-1][0] == k:
                    dp_y, dp_n = dp_n*tmp, dp_y+dp_n
                else:
                    dp_y, dp_n = (dp_y+dp_n)*tmp, dp_y+dp_n
            return dp_y + dp_n
        
        ans = 1
        for bu in buckets:
            if bu:
                ans *= dp(bu)
        return ans - 1