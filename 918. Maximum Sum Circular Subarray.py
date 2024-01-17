# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import math
from typing import List


class Solution:
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    maxSum = -math.inf
    minSum = math.inf

    for a in A:
      totalSum += a
      currMaxSum = max(currMaxSum + a, a)
      currMinSum = min(currMinSum + a, a)
      maxSum = max(maxSum, currMaxSum)
      minSum = min(minSum, currMinSum)

    return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)
  
# Another way:
class Solution:
 def maxSubarraySumCircular(self, A):
     total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
     for a in A:
         curMax = max(curMax + a, a)
         maxSum = max(maxSum, curMax)
         curMin = min(curMin + a, a)
         minSum = min(minSum, curMin)
         total += a
     return max(maxSum, total - minSum) if maxSum > 0 else maxSum