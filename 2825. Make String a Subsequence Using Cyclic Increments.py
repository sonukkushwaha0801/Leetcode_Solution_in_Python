# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def canMakeSubsequence(self, source: str, target: str) -> bool:
        targetIdx, targetLen = 0, len(target)  
        for currChar in source:
            if targetIdx < targetLen and (ord(target[targetIdx]) - ord(currChar)) % 26 < 2:
                targetIdx += 1  
        return targetIdx == targetLen
    
# Another way:
class Solution:
    def canMakeSubsequence(self, source: str, target: str) -> bool:
        src_len = len(source)
        tgt_len = len(target)
        src_idx = 0
        tgt_idx = 0
        
        while src_idx < src_len and tgt_idx < tgt_len:
            if (source[src_idx] == target[tgt_idx] or 
                (source[src_idx] == 'z' and target[tgt_idx] == 'a') or 
                (ord(source[src_idx]) + 1 == ord(target[tgt_idx]))):
                src_idx += 1
                tgt_idx += 1
            else:
                src_idx += 1
                
        return tgt_idx == tgt_len