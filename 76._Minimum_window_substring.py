# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case 
        if t =="" or len(s) < len(t): return ""

        # Intialize and set needmap(string t) and havemap(window)
        needmap , havemap = {} , {} 
        for c in t:
            needmap[c] = needmap.get(c,0) + 1 # t char count 
            havemap[c] = 0 # intialize with t chars and 0 as value for all keys
         
        need , have  = len(needmap) , 0 
        l = 0 
        res , resLen = "" , float("infinity")
        for r in range(len(s)):
            if s[r] in needmap: # check if it is a char in t 
                havemap[s[r]] += 1 # update count in window 
                if havemap[s[r]] ==  needmap[s[r]] : # compare the count of window and t's counter 
                    have += 1 
            while(have == need) : # to reduce window size to optimal value until valid 
                if resLen > r-l+1:
                    resLen = r-l+1  # update results 
                    res = s[l:r+1]
                if s[l] in havemap :
                    havemap[s[l]] -= 1 # update window counter 
                    if needmap[s[l]] > havemap[s[l]] : 
                        have -= 1
                l+=1 # increment left pointer of the window 
        return res 
            
# Another way:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = [0] * 128
        for c in t:
            m[ord(c)] += 1
        start = 0
        end = 0
        counter = len(t)
        minStart = 0
        minLen = float('inf')
        size = len(s)
        while end < size:
            if m[ord(s[end])] > 0:
                counter -= 1
            m[ord(s[end])] -= 1
            end += 1
            while counter == 0:
                if end - start < minLen:
                    minStart = start
                    minLen = end - start
                m[ord(s[start])] += 1
                if m[ord(s[start])] > 0:
                    counter