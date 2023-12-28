# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import collections


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        values = [[0]*(k+1) for _ in range(n+1)]
        data = []

        length = 0 
        block_char = None
        block_start = 0
        prev_blocks_length = 0 
        block_number = -1 
        block_numbers = {} 
        
        for i, ch in enumerate(s):
            if ch != block_char:
                block_number += 1
                block_char = ch
                if block_char not in block_numbers:
                    block_numbers[block_char] = []
                
                block_numbers[block_char].append((block_number, i+1))
                block_start = i 
                data.append(1) 
                prev_blocks_length = length
                length += 1 
            
            else:
                data[-1] += 1
                if data[-1] == 100 or data[-1] == 10 or data[-1] == 2:
                    length += 1
            values[i+1][0] = length
            for j in range(1, k+1):
                minimum = values[i][j-1]
                minimum = min(minimum, values[block_start][j] + (length - prev_blocks_length))
                if ch in block_numbers:
                    b = len(block_numbers[ch]) - 1
                    merge_k = 0
                    num_chars = data[block_numbers[ch][b][0]] 

                    while b > 0 and merge_k < j:
                        right, _ = block_numbers[ch][b]
                        left, idx = block_numbers[ch][b-1]
                        num_chars += data[left]

                        b -= 1
                            
                        for m in range(left+1, right): 
                            merge_k += data[m]
                        
                        if merge_k <= j: 
                            summation = 1
                            if num_chars >= 100:
                                summation += 1
                            if num_chars >= 10:
                                summation += 1
                            if num_chars >= 2:
                                summation += 1
                            minimum = min(minimum, values[idx-1][j - merge_k] + summation)
                
                values[i+1][j] = minimum 
        return values[-1][-1]

       
# Another way:
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        def getLength(maxFreq: int) -> int:
            if maxFreq == 1:
                return 1  
            if maxFreq < 10:
                return 2  
            if maxFreq < 100:
                return 3 
            return 4   

        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def dfs(i: int, k: int) -> int:
            if k < 0:
                return float('inf')
            if i == n or n - i <= k:
                return 0
            if dp[i][k] != -1:
                return dp[i][k]

            ans = float('inf')
            maxFreq = 0
            count = collections.Counter()

            for j in range(i, n):
                count[s[j]] += 1
                maxFreq = max(maxFreq, count[s[j]])
                ans = min(ans, getLength(maxFreq) + dfs(j + 1, k - (j - i + 1 - maxFreq)))

            dp[i][k] = ans
            return ans
        return dfs(0, k)