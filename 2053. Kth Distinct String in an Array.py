# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter, List


class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str:
        return (f:=lambda i,k,c=Counter(a):(q:=c[a[i]]<2) and k<2 and a[i] or f(i+1,k-q) if a[i:] else '')(0,k)
    
# Another way:
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        print(counter)
        for v in arr:
            print(counter[v])
            if counter[v] == 1:
                k -= 1
                if k == 0:
                    return v
        return ''