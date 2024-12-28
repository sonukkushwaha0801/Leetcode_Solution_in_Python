# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ksums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            ksums.append(ksums[-1] + nums[i] - nums[i-k])

        dp = {}
        def get_max_sum(i, cnt):
            if cnt == 3 or i > (len(nums) - k):
                return 0

            if (i, cnt) in dp :
                return dp[(i, cnt)]

            include = ksums[i] + get_max_sum(i+k, cnt+1)
            skip = get_max_sum(i+1, cnt)
            dp[(i, cnt)] = max(include, skip)
            return dp[(i, cnt)]

        def get_indices():
            i = 0
            indices = []
            while i <= len(nums) - k and len(indices) < 3:
                include = ksums[i] + get_max_sum(i+k, len(indices)+1)
                skip = get_max_sum(i+1, len(indices))
                if include >= skip:
                    indices.append(i)
                    i += k
                else :
                    i += 1
            return indices

        return get_indices()



        