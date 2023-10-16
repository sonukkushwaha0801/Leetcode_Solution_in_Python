# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
  def jump(self, nums: list[int]) -> int:
    ans = 0
    end = 0
    farthest = 0

    for i in range(len(nums) - 1):
      farthest = max(farthest, i + nums[i])
      if farthest >= len(nums) - 1:
        ans += 1
        break
      if i == end:     
        ans += 1       
        end = farthest  
    return ans
  
# Another way:
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        next = 0
        current = 0
        i = 0
        n = len(nums)
        for i in range(0, n-1):
            next = max(next, i + nums[i])

            if current == i:
                jumps += 1
                current = next
        
        return jumps