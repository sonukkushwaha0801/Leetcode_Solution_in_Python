# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        last = [0] * n
        last[-1] = n - 1 
        for i in range(n - 2, -1, -1):
            if num_str[i] > num_str[last[i + 1]]:
                last[i] = i
            else:
                last[i] = last[i + 1]
        for i in range(n):
            if num_str[i] != num_str[last[i]]:
                num_str[i], num_str[last[i]] = num_str[last[i]], num_str[i]
                return int(''.join(num_str))
        return num
    
# Another way:
class Solution:
    def maximumSwap(self, v: int) -> int:
        return int(max([s:=str(v)]+[s[:i]+s[j]+s[i+1:j]+c+s[j+1:] for i,c in enumerate(s) for j in range(i+1,len(s))]))