# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        extended_code = code * 2
        if k > 0:
            return [sum(extended_code[i + 1:i + 1 + k]) for i in range(n)]
        else:
            k = abs(k)
            return [sum(extended_code[i + n - k:i + n]) for i in range(n)]
        
# Another way:
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k>0:
            final=code+code[:k]
            for i in range(len(code)):
                code[i]=sum(final[i+1:k+1+i])
            return code
        if k==0:
            new=[0]*len(code)
            return new
        else:
            final=code[k:]+code
            for i in range(len(code)):
                code[i]=sum(final[i:i-k])
            return code