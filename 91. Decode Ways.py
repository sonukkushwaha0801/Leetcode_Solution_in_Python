# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def numDecodings(self, s):
        if s == "0":
            return 0
        dp_2 = 1
        dp_1 = int(s[-1] != "0")

        i = len(s) - 2
        while i >= 0:
            if s[i] == "0":
                dp_0 = 0
            else:
                dp_0 = dp_1
                if (s[i] == "1") or (s[i] == "2" and eval(s[i + 1]) < 7):
                    dp_0 += dp_2
            i -= 1
            dp_0, dp_1, dp_2 = 0, dp_0, dp_1
        
        return dp_1
    
# ANother way:
class Solution(object):
    def numDecodings(self, s):
        def decode_helper(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0 
            ways = decode_helper(index + 1)
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ways += decode_helper(index + 2)
            return ways
        return decode_helper(0)
        