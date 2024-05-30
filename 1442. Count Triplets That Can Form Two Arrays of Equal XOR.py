# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def countTriplets(self, arr):
        
        n = len(arr)
        count = 0
        prefixXOR = [0] * (n + 1)
        
        for i in range(n):
            prefixXOR[i+1] = prefixXOR[i] ^ arr[i]
        
        for i in range(n):
            for j in range(i + 1, n):
                if (prefixXOR[i] == (prefixXOR[j+1])):
                    count += j - i
        
        return count