# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import collections
from typing import List
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        sorted_cards = sorted(card_count)
        
        for card in sorted_cards:
            if card_count[card] > 0:  # there are still some of this card left to use
                count = card_count[card]
                for i in range(card, card + groupSize):
                    if card_count[i] < count:
                        return False
                    card_count[i] -= count

        return True
    
# Another way to solve:
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c=collections.Counter(hand)
        n=sorted(c)
        for i in n:
            if c[i]>0:
                for j in range(groupSize)[::-1]:
                    c[i+j]-=c[i]
                    if c[i+j]<0:
                        return False
        return True                