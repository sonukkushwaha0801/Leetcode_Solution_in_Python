# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck_sorted_desc = sorted(deck, reverse=True)
        ordered_deck = deque()
        for card in deck_sorted_desc:
            if len(ordered_deck) > 1:
                ordered_deck.rotate(1)
            ordered_deck.appendleft(card)
        return list(ordered_deck)

# Another way:
class Solution:
    def deckRevealedIncreasing(self, d: list[int]) -> list[int]:
        q = deque()
        for v in sorted(d)[::-1]:
            q.rotate()
            q.appendleft(v)
        return q