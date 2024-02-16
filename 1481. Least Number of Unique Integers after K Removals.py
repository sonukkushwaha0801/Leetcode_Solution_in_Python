# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freq_map = Counter(arr)

        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1])

        for num, freq in sorted_freq:
            if k >= freq:
                k -= freq
                del freq_map[num]
            else:
                break

        return len(freq_map)
    
# Another way:
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        a=Counter(arr)  
        li=sorted(arr, key=lambda x:(a[x],x))
        li=li[k:]
        return len(set(li))