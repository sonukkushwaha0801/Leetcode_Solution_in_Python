# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        if l==0:
            return 0
        dicts={}
        max_len=0
        start=0
        for i in range(l):
            if s[i] in dicts and start<=dicts[s[i]]:
                start = dicts[s[i]]+1
            else:
                max_len=max(max_len,i-start+1)
            dicts[s[i]]=i
        return max_len
        
#Another way:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_sub=[]
        prev=""
        cnt=0
        i=0
        while i <len(s):
            j=i
            cnt=0
            while(j<len(s) and (s[j] not in prev)):
                prev=prev+s[j]
                cnt+=1
                j+=1
            prev=""
            i+=1
            len_sub.append(cnt)
        print(len_sub)
        if(len_sub==[]):
            return 0

        return max(len_sub)
                