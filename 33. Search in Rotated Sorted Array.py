# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from bisect import bisect_left

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        rotation = bisect_left(nums[:-1], True, key=lambda n: n < nums[-1])
        idx = bisect_left(nums, target, **{'lo' if target <= nums[-1] else 'hi': rotation})

        return idx if nums[idx] == target else -1
    
#Another way:
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low , high = 0 , len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[low]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1