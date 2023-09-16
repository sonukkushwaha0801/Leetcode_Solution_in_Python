# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        strList = stripped.split(" ")
        return len(strList[-1])
    

# Second Type:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr1 = 0
        ptr2 = 0

        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                ptr1 = i+1
                print(ptr1)
                break
        
        for i in range(ptr1-1,-1,-1):
            if s[i] == " ":
                ptr2 = i
                break
            if i==0:
                ptr2 = i-1
                break
        
        result = ptr1-ptr2-1
        return result