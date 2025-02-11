# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i_value = values[0] + 0
        for j in range(1, len(values)):
            max_score = max(max_score, max_i_value + values[j] - j)
            max_i_value = max(max_i_value, values[j] + j)

        return max_score
    
# Another way:
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        if len(values)==2:
            return values[0]+values[1]-1
     
        first_max,second_max=values[0]-1,values[1]
        result=first_max+second_max

        for k in range(2,len(values)):
            first_max-=1
            second_max-=1
            
            if values[k]>first_max or values[k]>second_max:
                if first_max>second_max:
                    second_max=values[k]
                else:
                    first_max=values[k]

            result=max(result,first_max+second_max)

        return result
