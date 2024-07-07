# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
    
# Another way:
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            total_drunk += new_bottles
            empty_bottles = empty_bottles % numExchange + new_bottles
        
        return total_drunk