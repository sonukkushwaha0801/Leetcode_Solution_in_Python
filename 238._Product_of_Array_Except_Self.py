# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    left_product = [1] * n 
    right_product = [1] * n 
    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]

    result = [left_product[i] * right_product[i] for i in range(n)]

    return result

# Another way:
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res