# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        left = 0
        right = n - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score
    
# Another way:
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        n = len(tokens)
        if n == 0:
            return 0
        elif n == 1:
            if power >= tokens[0]:
                return 1
            else:
                return 0
        tokens.sort()
        up = 0
        down = n-1
        score = 0
        curr_score = 0
        played = [False] * n
        while up<=down:
            if up==down and played[up]==True:
                break
            if tokens[up]<=power and played[up]==False:
                curr_score += 1
                score = max(score, curr_score)
                power -= tokens[up]
                played[up] = True
                up += 1 
            elif curr_score >= 1:
                curr_score -= 1
                score = max(score, curr_score)
                power += tokens[down]
                played[down] = True
                down -= 1
            else:
                break
        return score
