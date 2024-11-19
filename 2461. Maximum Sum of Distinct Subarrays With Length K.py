# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        ws = 0
        max_sum = 0

        for i in range(n):
            # Add the current element to the window
            mp[nums[i]] += 1
            ws += nums[i]

            # If the window size exceeds 'k', slide the window
            if i >= k:
                le = nums[i - k]
                mp[le] -= 1
                ws -= le
                if mp[le] == 0:
                    del mp[le]

            # Check if the window has exactly 'k' distinct elements
            if i >= k - 1 and len(mp) == k:
                max_sum = max(max_sum, ws)

        return max_sum
    
# Another way:
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        ans = window_sum = 0

        # Pre calculate the sum of the first k elements
        for i in range(k):
            window_sum += nums[i]
            if freq.__contains__(nums[i]):
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        if len(freq) == k:
            ans = max(ans, window_sum)

        # Calculate the sum of the remaining elements
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if freq.__contains__(nums[i]):
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]

            if len(freq) == k:
                ans = max(ans, window_sum)
        
        return ans