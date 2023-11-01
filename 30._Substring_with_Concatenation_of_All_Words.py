# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        wordcount={}
        for word in words:
            wordcount[word]=1+wordcount.get(word,0)
        result=[]
        substringlength=len(words)*len(words[0])
        for i in range(len(s)-substringlength+1):
            substr=s[i:i+substringlength]
            substrcount={}
            for j in range(0,len(substr),len(words[0])):
                word=substr[j:j+len(words[0])]
                substrcount[word]=1+substrcount.get(word,0)
            if substrcount==wordcount:
                result.append(i)
        return result

# Another way:
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        count = {}
        for word in words:
            count[word] = count.get(word,0) + 1
        
        lw = len(words[0])
        fin = []
        
        for i in range(lw):
            l = r = i
            window = {}
           
            while r < len(s):
                curr_w = s[r:r+lw]
                
                if curr_w not in count:
                    window.clear()
                    r += lw
                    l = r
                else:
                    window[curr_w] = window.get(curr_w,0) + 1
                    
                    if window[curr_w] <= count[curr_w]:
                        r += lw

                    else:
                        while l <= r and window[curr_w]>count[curr_w]:
                            w = s[l:l+lw]
                            window[w] -= 1
                            l += lw
                        r += lw
                   
                    if window == count:
                            fin.append(l)
        return fin