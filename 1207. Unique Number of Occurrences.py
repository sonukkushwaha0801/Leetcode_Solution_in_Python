# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values()))==len(Counter(arr).values())
    
# Another way:
class Solution(object):
    def uniqueOccurrences(self, arr):
        hashMap = {}
        
        # Count occurrences of each element in arr
        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        hashSet = set()
        flag = True
        
        # Check if there are unique occurrences
        for count in hashMap.values():
            if count in hashSet:
                flag = False
                break
            else:
                hashSet.add(count)
        
        return flag

        