# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def josephus(n, k):
            if n == 1:
                return 0
            else:
                return (josephus(n - 1, k) + k) % n
        
        return josephus(n, k) + 1
    
# Another way:
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        current_index=0 
        while len(friends)>1 :
            elimination_index = (current_index + k - 1) % len(friends)
            del friends[elimination_index] 

            current_index = (current_index + k - 1) % (len(friends) + 1)
            
        return friends[0]
        