# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import Counter, defaultdict


class Solution:
    def reverse(self, num: int) -> int:
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10
        return rev

    def countNicePairs(self, nums: list[int]) -> int:
        mod = 1000000007

        nums = [num - self.reverse(num) for num in nums]
        nums.sort()

        res = 0
        i = 0
        while i < len(nums) - 1:
            cont = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                cont += 1
                i += 1
            res = (res % mod + (cont * (cont - 1)) // 2) % mod
            i += 1

        return int(res % mod)
        
# Another way:
class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        res, d = 0, defaultdict(int)
        for i, n in enumerate(nums):
            k = n - int(str(n)[::-1])
            res += d[k]
            d[k] += 1
        return res % (10**9 + 7)

# Additional One:
class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        return sum(v*(v-1)//2 for v in Counter(n - int(str(n)[::-1]) for n in nums).values()) % (10**9 + 7)