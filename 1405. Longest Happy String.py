# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ''
        while a > 0 or b > 0 or c > 0:
            if a >= b and a >= c:
                if len(s) >= 2 and s[-2:] == 'aa':
                    if b > c:
                        s += 'b'
                        b -= 1
                    elif c > 0:
                        s += 'c'
                        c -= 1
                    else:
                        break
                else:
                    s += 'a'
                    a -= 1

            elif b >= a and b >= c:
                if len(s) >= 2 and s[-2:] == 'bb':
                    if a > c:
                        s += 'a'
                        a -= 1
                    elif c > 0:
                        s += 'c'
                        c -= 1
                    else:
                        break
                else:
                    s += 'b'
                    b -= 1

            elif c >= a and c >= b:
                if len(s) >= 2 and s[-2:] == 'cc':
                    if a > b:
                        s += 'a'
                        a -= 1
                    elif b > 0:
                        s += 'b'
                        b -= 1
                    else:
                        break
                else:
                    s += 'c'
                    c -= 1

        return s
    
# Another way:
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        pq = []
        
        if a > 0: heapq.heappush(pq, (-a, 'a'))
        if b > 0: heapq.heappush(pq, (-b, 'b'))
        if c > 0: heapq.heappush(pq, (-c, 'c'))
        
        while pq:
            cnt1, char1 = heapq.heappop(pq)
            
            # If adding the current char would create a sequence of 3, use the second most frequent
            if len(res) >= 2 and res[-1] == char1 and res[-2] == char1:
                if not pq:
                    break
                cnt2, char2 = heapq.heappop(pq)
                res.append(char2)
                if cnt2 + 1:
                    heapq.heappush(pq, (cnt2 + 1, char2))
                heapq.heappush(pq, (cnt1, char1))
            else:
                res.append(char1)
                if cnt1 + 1:
                    heapq.heappush(pq, (cnt1 + 1, char1))
        
        return ''.join(res)